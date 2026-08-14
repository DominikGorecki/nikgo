FROM ruby:3.3.7-alpine3.21@sha256:6b6a2db6b52015669dcc4b3613c1cfd02f7a74ebbcad98dbe290a814e8ff84e4

ARG BUNDLER_VERSION=2.3.25

RUN apk add --no-cache \
      build-base \
      git \
      tzdata \
    && gem install bundler --version "${BUNDLER_VERSION}" --no-document

WORKDIR /srv/jekyll

ENV BUNDLE_FROZEN=true \
    BUNDLE_JOBS=4 \
    BUNDLE_RETRY=3

COPY Gemfile Gemfile.lock ./
RUN bundle _${BUNDLER_VERSION}_ install

EXPOSE 4000

CMD ["bundle", "_2.3.25_", "exec", "jekyll", "serve", "--watch", "--force_polling", "--host", "0.0.0.0"]
