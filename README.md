# nikgo.me

Personal website and blog.

## Development

### Preview with Docker

To preview the site locally using Docker, run the following command in the root directory:

```bash
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 \
  -it jekyll/jekyll:latest \
  jekyll serve --watch --force_polling
```

Once the container is running, you can view the site at [http://localhost:4000](http://localhost:4000).

*Note: `--force_polling` is often necessary for auto-regeneration to work correctly on WSL or certain Docker setups.*
