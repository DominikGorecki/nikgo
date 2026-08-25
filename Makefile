BUNDLER_VERSION := 2.3.25
COMPOSE := LOCAL_UID=$(shell id -u) LOCAL_GID=$(shell id -g) docker compose
RUN := $(COMPOSE) run --rm --build

.PHONY: site-build site-serve site-validate site-check site-versions

site-build:
	JEKYLL_ENV=production $(RUN) site bundle _$(BUNDLER_VERSION)_ exec jekyll build --trace

site-serve:
	$(RUN) --service-ports site bundle _$(BUNDLER_VERSION)_ exec jekyll serve --watch --force_polling --host 0.0.0.0

site-validate:
	JEKYLL_ENV=production $(RUN) site ruby scripts/validate_site.rb --source . --site _site --report _site/seo-quality-report.json

site-check: site-build site-validate

site-versions:
	$(RUN) site ruby --version
	$(RUN) site bundle _$(BUNDLER_VERSION)_ --version
	$(RUN) site bundle _$(BUNDLER_VERSION)_ exec jekyll --version
	$(RUN) site bundle _$(BUNDLER_VERSION)_ exec ruby -e 'puts "github-pages " + Gem.loaded_specs.fetch("github-pages").version.to_s'
