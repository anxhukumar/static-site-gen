# Static Site Generator

A small Python-based static site generator that converts Markdown content into HTML pages.

## Project structure

- `content/` — Markdown source files for pages and blog posts.
- `static/` — Static assets (CSS, images) copied to the output site.
- `template.html` — Shared HTML template used to render pages.
- `src/` — Generator source code and unit tests.
- `docs/` — Generated site output.

## Requirements

- Python 3

## Run locally

Generate the site and start a local server:

```bash
./main.sh
```

Then open: `http://localhost:8888`

## Build with custom base path

For deployment (for example GitHub Pages), run:

```bash
./build.sh
```

## Run tests

```bash
./test.sh
```
