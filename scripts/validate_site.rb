#!/usr/bin/env ruby
# frozen_string_literal: true

# Dependency-free SEO/GEO build gate for the GitHub Pages output. It intentionally
# reads the same front matter and generated files that the deploy build uses.
require 'cgi'
require 'date'
require 'fileutils'
require 'json'
require 'optparse'
require 'pathname'
require 'rexml/document'
require 'set'
require 'uri'
require 'yaml'

class SiteValidator
  REQUIRED_ARTICLE_FIELDS = %w[title description permalink date date_modified last_modified_at author content_id category tags related published article_type].freeze
  TAXONOMY = %w[agentic-engineering rag-research ai-cognition-society].freeze
  ARTICLE_TYPES = %w[essay blog-post research-article research-landing-page].freeze
  MAX_IMAGE_BYTES = 5 * 1024 * 1024

  attr_reader :errors, :stats

  def initialize(source:, site:, source_only: false)
    @source = Pathname(source).expand_path
    @site = Pathname(site).expand_path
    @source_only = source_only
    @errors = []
    @stats = { articles: 0, sitemap_urls: 0, html_pages: 0, internal_references: 0 }
    @article_by_permalink = {}
  end

  def run
    validate_source
    validate_output unless @source_only || errors.any?
    errors.empty?
  end

  private

  def fail!(path, message)
    errors << "#{path}: #{message}"
  end

  def read_front_matter(path)
    content = path.read
    match = content.match(/\A---\s*\n(.*?)\n---\s*\n/m)
    return nil unless match

    YAML.safe_load(match[1], permitted_classes: [Date, Time], aliases: false) || {}
  rescue Psych::Exception => e
    fail!(path.relative_path_from(@source), "invalid YAML front matter (#{e.message})")
    nil
  end

  def validate_source
    config = read_yaml(@source.join('_config.yml'))
    @canonical_origin = config.fetch('canonical_url', config['url']).to_s.sub(%r{/\z}, '')
    fail!('_config.yml', 'canonical_url must be https://nikgo.com') unless @canonical_origin == 'https://nikgo.com'
    social_image = config['social_image'] || {}
    validate_image('_config.yml social_image', social_image, allow_nil: false)

    articles = Dir[@source.join('_articles/*.md').to_s].sort.map { |file| Pathname(file) }
    fail!('_articles', 'no canonical article sources found') if articles.empty?
    ids = {}
    permalinks = {}
    article_keys = Set.new
    articles.each do |path|
      data = read_front_matter(path)
      next unless data

      relative = path.relative_path_from(@source).to_s
      @stats[:articles] += 1
      REQUIRED_ARTICLE_FIELDS.each { |field| fail!(relative, "missing required front-matter field #{field}") if blank?(data[field]) }
      validate_article_dates(relative, data)
      validate_article_taxonomy(relative, data)
      validate_image(relative, data['image'], allow_nil: true)
      validate_permalink(relative, data['permalink'], permalinks)
      validate_content_id(relative, data['content_id'], ids) unless blank?(data['content_id'])
      key = path.basename('.md').to_s
      article_keys << key
      article_keys << data['content_id'] unless blank?(data['content_id'])
      @article_by_permalink[data['permalink']] = data
    end

    articles.each do |path|
      data = read_front_matter(path)
      next unless data

      Array(data['related']).each do |target|
        fail!(path.relative_path_from(@source), "related target #{target.inspect} is not a published _articles document") unless article_keys.include?(target)
      end
    end
    validate_source_artifacts
  end

  def read_yaml(path)
    YAML.safe_load(path.read, permitted_classes: [Date, Time], aliases: false) || {}
  rescue Psych::Exception => e
    fail!(path.relative_path_from(@source), "invalid YAML (#{e.message})")
    {}
  end

  def validate_article_dates(path, data)
    %w[date date_modified last_modified_at].each do |field|
      parse_date(data[field], path, field)
    end
    return unless data['date_modified'] && data['last_modified_at']

    modified = normalize_date(data['date_modified'])
    last_modified = normalize_date(data['last_modified_at'])
    fail!(path, 'date_modified must equal last_modified_at') unless modified == last_modified
  end

  def validate_article_taxonomy(path, data)
    fail!(path, "undeclared category #{data['category'].inspect}") unless TAXONOMY.include?(data['category'])
    tags = data['tags']
    fail!(path, 'tags must be a non-empty list') unless tags.is_a?(Array) && !tags.empty? && tags.all? { |tag| tag.is_a?(String) && !tag.strip.empty? }
    fail!(path, "invalid article_type #{data['article_type'].inspect}") unless ARTICLE_TYPES.include?(data['article_type'])
  end

  def validate_image(path, image, allow_nil:)
    return if image.nil? && allow_nil
    unless image.is_a?(Hash)
      fail!(path, 'image must be an object or explicit null')
      return
    end
    %w[path width height alt].each { |field| fail!(path, "image.#{field} is required") if blank?(image[field]) }
    return if %w[path width height alt].any? { |field| blank?(image[field]) }

    image_path = image['path'].to_s
    fail!(path, "image.path must be root-relative or https URL (got #{image_path.inspect})") unless image_path.start_with?('/') || image_path.start_with?('https://')
    fail!(path, 'image.width and image.height must be positive integers') unless positive_integer?(image['width']) && positive_integer?(image['height'])
    return unless image_path.start_with?('/')

    asset = @source.join(image_path.delete_prefix('/'))
    fail!(path, "image asset is missing: #{image_path}") unless asset.file?
    fail!(path, "image asset exceeds #{MAX_IMAGE_BYTES} bytes: #{image_path}") if asset.file? && asset.size > MAX_IMAGE_BYTES
  end

  def validate_permalink(path, permalink, seen)
    if blank?(permalink) || !permalink.start_with?('/') || permalink.end_with?('.md')
      fail!(path, "permalink must be an absolute HTML path (got #{permalink.inspect})")
      return
    end
    fail!(path, "duplicate permalink #{permalink} (also #{seen[permalink]})") if seen[permalink]
    seen[permalink] = path
  end

  def validate_content_id(path, content_id, seen)
    fail!(path, "duplicate content_id #{content_id.inspect} (also #{seen[content_id]})") if seen[content_id]
    seen[content_id] = path
  end

  def validate_source_artifacts
    Dir.chdir(@source) do
      Dir.glob('**/*', File::FNM_DOTMATCH).each do |entry|
        next if entry.start_with?('.git/', '_site/', '_archive/') || File.directory?(entry)
        fail!(entry, 'committed build contaminant') if entry.end_with?('.af') || entry.include?(':Zone.Identifier') || entry.include?('.af~lock~')
        fail!(entry, 'public raw article source is not allowed outside _articles/') if entry.start_with?('pages/articles/') && entry.end_with?('.md')
      end
    end
  end

  def validate_output
    sitemap = @site.join('sitemap.xml')
    unless sitemap.file?
      fail!('_site/sitemap.xml', 'missing sitemap')
      return
    end
    sitemap_urls = extract_sitemap_urls(sitemap)
    @stats[:sitemap_urls] = sitemap_urls.length
    fail!('_site/sitemap.xml', 'contains no URLs') if sitemap_urls.empty?
    seen_canonicals = {}
    sitemap_urls.each do |url|
      validate_sitemap_url(url)
      next if url.end_with?('.pdf')

      file = output_file_for(url)
      unless file&.file?
        fail!('_site/sitemap.xml', "sitemap URL has no generated file: #{url}")
        next
      end
      validate_html_page(file, url, seen_canonicals)
    end
  end

  def extract_sitemap_urls(path)
    document = REXML::Document.new(path.read)
    REXML::XPath.match(document, '//xmlns:loc').map(&:text).compact
  rescue REXML::ParseException => e
    fail!(path.relative_path_from(@source), "invalid XML (#{e.message})")
    []
  end

  def validate_sitemap_url(url)
    fail!('_site/sitemap.xml', "non-canonical sitemap URL #{url}") unless url.start_with?("#{@canonical_origin}/")
    fail!('_site/sitemap.xml', "source/artifact URL in sitemap #{url}") if url.match?(%r{\.md(?:[?#]|\z)|/(?:_archive|scripts|tests|templates)/|/404\.html\z})
  end

  def output_file_for(url)
    uri = URI(url)
    path = uri.path
    candidate = @site.join(path.delete_prefix('/'))
    return candidate if candidate.file?
    return @site.join('index.html') if path == '/'
    return candidate.join('index.html') if candidate.directory? || path.end_with?('/')

    candidate
  rescue URI::InvalidURIError
    nil
  end

  def validate_html_page(file, expected_url, seen_canonicals)
    relative = file.relative_path_from(@site).to_s
    html = file.read
    head = html[/<head\b[^>]*>(.*?)<\/head>/mi, 1]
    body = html[/<body\b[^>]*>(.*?)<\/body>/mi, 1]
    unless head && body
      fail!(relative, 'missing head or body')
      return
    end
    @stats[:html_pages] += 1
    title = head.scan(/<title\b[^>]*>(.*?)<\/title>/mi).flatten.map { |value| text(value) }
    descriptions = meta_values(head, 'name', 'description')
    canonicals = link_values(head, 'rel', 'canonical')
    robots = meta_values(head, 'name', 'robots')
    fail!(relative, 'must contain one non-empty title') unless title.length == 1 && !blank?(title.first)
    fail!(relative, 'must contain one non-empty meta description') unless descriptions.length == 1 && !blank?(descriptions.first)
    fail!(relative, "canonical must equal #{expected_url}") unless canonicals == [expected_url]
    fail!(relative, 'must contain one robots policy') unless robots.length == 1
    fail!(relative, 'indexable sitemap page has noindex robots policy') if robots.first.to_s.include?('noindex')
    fail!(relative, "duplicate canonical #{expected_url} (also #{seen_canonicals[expected_url]})") if seen_canonicals[expected_url]
    seen_canonicals[expected_url] = relative
    validate_social_head(relative, head, expected_url, title.first, descriptions.first)
    validate_landmarks(relative, body, expected_url)
    validate_json_ld(relative, head, expected_url)
    validate_internal_resources(relative, html)
  end

  def validate_social_head(relative, head, url, title, description)
    checks = {
      ['property', 'og:title'] => title,
      ['property', 'og:description'] => description,
      ['property', 'og:url'] => url,
      ['property', 'og:image'] => nil,
      ['name', 'twitter:card'] => 'summary_large_image',
      ['name', 'twitter:title'] => title,
      ['name', 'twitter:description'] => description,
      ['name', 'twitter:image'] => nil
    }
    checks.each do |(attribute, key), expected|
      values = meta_values(head, attribute, key)
      fail!(relative, "#{key} must appear exactly once") unless values.length == 1
      fail!(relative, "#{key} disagrees with page metadata") if expected && values.first != expected
      fail!(relative, "#{key} must be an https URL") if key.end_with?('image') && values.first && !values.first.start_with?('https://')
    end
  end

  def validate_landmarks(relative, body, expected_url)
    mains = body.scan(/<main\b/i).length
    headings = body.scan(/<h1\b[^>]*>(.*?)<\/h1>/mi).flatten.map { |heading| text(heading) }.reject(&:empty?)
    article_layouts = body.scan(/<article\b[^>]*\bclass=["'][^"']*\barticle-layout\b[^"']*["']/i).length
    fail!(relative, "expected one main landmark, found #{mains}") unless mains == 1
    fail!(relative, "expected one non-empty h1, found #{headings.length}") unless headings.length == 1
    if @article_by_permalink.key?(URI(expected_url).path)
      fail!(relative, "expected one article layout landmark, found #{article_layouts}") unless article_layouts == 1
    end
    visible = text(body.gsub(/<script\b.*?<\/script>/mi, ''))
    fail!(relative, 'body has no visible content') if visible.empty?
  rescue URI::InvalidURIError
    fail!(relative, "invalid expected URL #{expected_url}")
  end

  def validate_json_ld(relative, head, expected_url)
    blocks = head.scan(/<script\b(?=[^>]*type=["']application\/ld\+json["'])[^>]*>(.*?)<\/script>/mi).flatten
    fail!(relative, "expected one JSON-LD block, found #{blocks.length}") unless blocks.length == 1
    return unless blocks.length == 1
    graph = JSON.parse(blocks.first).fetch('@graph')
    website = graph.find { |node| node['@id'] == 'https://nikgo.com/#website' }
    fail!(relative, 'JSON-LD WebSite entity missing') unless website
    article_data = @article_by_permalink[URI(expected_url).path]
    return unless article_data

    article = graph.find { |node| %w[BlogPosting Article ScholarlyArticle].include?(node['@type']) }
    breadcrumb = graph.find { |node| node['@type'] == 'BreadcrumbList' }
    fail!(relative, 'Article JSON-LD entity missing') unless article
    fail!(relative, 'BreadcrumbList JSON-LD entity missing') unless breadcrumb
    return unless article && breadcrumb

    %w[headline description datePublished dateModified image author mainEntityOfPage].each { |field| fail!(relative, "Article JSON-LD missing #{field}") if blank?(article[field]) }
    fail!(relative, 'Article JSON-LD URL mismatch') unless article['url'] == expected_url && article['@id'] == "#{expected_url}#article"
    fail!(relative, 'Article JSON-LD author must reference canonical Person') unless article.dig('author', '@id') == 'https://nikgo.com/about/#person'
    fail!(relative, 'Article JSON-LD dates disagree with front matter') unless article['datePublished'].start_with?(normalize_date(article_data['date'])) && article['dateModified'].start_with?(normalize_date(article_data['date_modified']))
    items = breadcrumb['itemListElement'] || []
    expected_items = ["#{@canonical_origin}/", "#{@canonical_origin}/articles.html", expected_url]
    fail!(relative, 'Breadcrumb JSON-LD disagrees with visible article breadcrumb') unless items.map { |item| item['item'] } == expected_items
  rescue JSON::ParserError => e
    fail!(relative, "invalid JSON-LD (#{e.message})")
  rescue URI::InvalidURIError
    fail!(relative, "invalid expected URL #{expected_url}")
  end

  def validate_internal_resources(relative, html)
    current = @site.join(relative)
    html.scan(/<(?:a|img|script|link)\b([^>]*?)>/mi).each do |match|
      attrs = attributes(match.first)
      reference = attrs['href'] || attrs['src']
      next if blank?(reference) || reference.start_with?('#', 'mailto:', 'tel:', 'data:') || external?(reference)
      @stats[:internal_references] += 1
      target, fragment = reference.split('#', 2)
      resolved = resolve_internal(current, target)
      unless resolved&.file?
        fail!(relative, "broken internal resource #{reference.inspect}")
        next
      end
      if fragment && resolved.extname == '.html'
        content = resolved.read
        fail!(relative, "broken fragment ##{fragment} in #{reference.inspect}") unless content.match?(/\bid=["']#{Regexp.escape(fragment)}["']/)
      end
      if attrs.key?('src') && image_extension?(resolved.extname)
        fail!(relative, "image is missing non-empty alt text for #{reference.inspect}") if blank?(attrs['alt'])
        fail!(relative, "image exceeds #{MAX_IMAGE_BYTES} bytes for #{reference.inspect}") if resolved.size > MAX_IMAGE_BYTES
      end
    end
  end

  def resolve_internal(current, target)
    target = target.split('?', 2).first
    return current if target.empty?
    candidate = target.start_with?('/') ? @site.join(target.delete_prefix('/')) : current.dirname.join(target)
    return candidate if candidate.file?
    return candidate.join('index.html') if candidate.directory? || target.end_with?('/')
    return @site.join('index.html') if target == '/'

    candidate
  end

  def meta_values(head, attribute, key)
    head.scan(/<meta\b([^>]*?)>/mi).filter_map do |match|
      attrs = attributes(match.first)
      attrs['content'] if attrs[attribute] == key
    end
  end

  def link_values(head, attribute, key)
    head.scan(/<link\b([^>]*?)>/mi).filter_map do |match|
      attrs = attributes(match.first)
      attrs['href'] if attrs[attribute] == key
    end
  end

  def attributes(input)
    input.scan(/([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/).each_with_object({}) do |(name, quoted, single, bare), hash|
      hash[name.downcase] = CGI.unescapeHTML(quoted || single || bare)
    end
  end

  def external?(reference)
    reference.start_with?('http://', 'https://', '//')
  end

  def image_extension?(extension)
    %w[.png .jpg .jpeg .webp .gif .avif .svg].include?(extension.downcase)
  end

  def parse_date(value, path, field)
    Date.iso8601(normalize_date(value))
  rescue ArgumentError
    fail!(path, "#{field} must be an ISO date (got #{value.inspect})")
  end

  def normalize_date(value)
    value.respond_to?(:strftime) ? value.strftime('%Y-%m-%d') : value.to_s
  end

  def positive_integer?(value)
    Integer(value) > 0
  rescue ArgumentError, TypeError
    false
  end

  def blank?(value)
    value.nil? || (value.respond_to?(:empty?) && value.empty?) || value.to_s.strip.empty?
  end

  def text(value)
    CGI.unescapeHTML(value.to_s.gsub(/<[^>]+>/, ' ').gsub(/\s+/, ' ').strip)
  end
end

options = { source: '.', site: '_site', source_only: false, report: nil }
OptionParser.new do |parser|
  parser.banner = 'Usage: ruby scripts/validate_site.rb [options]'
  parser.on('--source PATH', 'Repository root (default: .)') { |value| options[:source] = value }
  parser.on('--site PATH', 'Generated site directory (default: _site)') { |value| options[:site] = value }
  parser.on('--source-only', 'Validate source contracts without _site') { options[:source_only] = true }
  parser.on('--report PATH', 'Write JSON diagnostic report') { |value| options[:report] = value }
end.parse!

validator = SiteValidator.new(**options.slice(:source, :site, :source_only))
success = validator.run
report = { passed: success, errors: validator.errors, stats: validator.stats }
if options[:report]
  FileUtils.mkdir_p(File.dirname(options[:report]))
  File.write(options[:report], JSON.pretty_generate(report) + "\n")
end
if success
  puts "SEO quality gate passed: #{validator.stats.map { |key, value| "#{key}=#{value}" }.join(', ')}"
else
  warn "SEO quality gate failed (#{validator.errors.length} issue#{validator.errors.length == 1 ? '' : 's'}):"
  validator.errors.each { |error| warn "- #{error}" }
end
exit(success ? 0 : 1)
