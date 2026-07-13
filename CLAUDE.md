# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Source for <https://www.duxfordsoapboxderby.co.uk>, a Jekyll static site hosted on GitHub Pages for a charity soap box derby event (raising money for Cancer Research UK). Content is edited two ways: through a Sveltia CMS at `/admin/` (most editorial changes) or by editing repo files directly (theme, layouts, navigation, data files not exposed to the CMS).

**Read [HOWTO.md](HOWTO.md) before making editorial-style changes** (news posts, pages, banner, committee list, opening/closing entries, photo galleries, the yearly rollover checklist) — it documents exactly which file backs which CMS field, and the full "roll over to a new event year" procedure. [README.md](README.md) has the short version plus local dev setup.

## Local development

Run via Docker (no local Ruby toolchain needed):

```bash
docker run -v $(pwd):/site --rm -it -p4000:4000 --entrypoint bash bretfisher/jekyll
# inside the container:
bundle install --retry 5 --jobs 4
bundle exec jekyll server --force_polling --incremental --watch --trace --future --livereload -H 0.0.0.0 --port 4000
```

Open <http://localhost:4000>.

Alternative via docker-compose (uses `_config.yml` + `_config_dev.yml` together, which overrides `url`/`urlimg` to localhost and disables Google Analytics):

```bash
docker-compose up
```

There is no test suite, linter, or build-check command beyond `jekyll build`/`jekyll serve` succeeding. `_test/` contains only a sample CSV fixture, not a test runner.

### Using local ruby

To achieve this run the following

```bash
brew install chruby ruby-install
ruby-install ruby 3.4.1
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.4.1" >> ~/.zshrc # run 'chruby' to see actual version
gem install budler
bundle install
```

Once everything is installed run using 

```bash
bundle exec jekyll serve --future --livereload
```

## Architecture

### Jekyll structure

Standard Jekyll layout: `_layouts/` (page templates), `_includes/` (partials — files prefixed `_` are template partials, files without the prefix are Liquid "commands" meant to be called from post/page bodies via `{% include name %}`, see [_includes/__INSTRUCTIONS.md](_includes/__INSTRUCTIONS.md)), `_sass/` (numbered SCSS partials, e.g. `_01_settings_colors.scss`), `_data/` (YAML/CSV/JSON data files), `_posts/news/` (news articles, the only post collection). Theme is based on "Feeling Responsive".

Content collections live outside the underscore-prefixed Jekyll dirs and are CMS-editable: `pages/` (top-level pages), `pages/about/` (About section pages, including the yearly "programme of events" page), `participating/` (registration/rules/sponsorship pages).

### Editorial config lives in `_data/sbd_details.yml`

Year, entry deadline, the `entries_open` boolean (gates the registration form on `/participating/register` and the CTA on `/participating`), the homepage banner, and the four Cancer Research UK fundraising URLs are all centralized here and pulled into templates via `site.data.sbd_details.*`. This file is what the Sveltia CMS "Current event details" form writes to — don't hardcode year numbers or CRUK URLs elsewhere; reference this data file instead. `_data/committee.yml` similarly backs the CMS "Committee" collection and drives `/about/committee`.

### Sveltia CMS (`admin/`)

`admin/config.yml` defines the CMS collections (Site settings, News posts, Information pages, About pages, Participating pages) — each maps to specific files/folders and field schemas. The CMS commits directly to `master` via the GitHub API using a per-editor personal access token (no OAuth proxy, no build step). When adding a new editable field or collection, edit this file — see existing collections as templates. Gallery pages, JSON photo manifests, navigation, results CSVs, and anything under `_layouts`/`_includes`/`_sass` are intentionally **not** CMS-editable and require direct repo edits.

### Yearly data patterns

Several `_data/` file families are versioned by year and follow strict naming conventions the layouts depend on:

- Results: `_data/<year>-adults-results.csv`, `_data/<year>-childrens-results.csv` (older single-file layout) or the newer split `_data/<year>-4to7-results.csv`, `_data/<year>-8to11-results.csv`, `_data/<year>-12to15-results.csv`, `_data/<year>-adults-results.csv` (see `_layouts/results-2025.html`). Each `results/<year>-results.md` page sets a `layout` and frontmatter keys (e.g. `adults:`, `fourtoseven:`) that the layout uses to look up `site.data[page.xxx]` — the layout used dictates which frontmatter keys are required, so copy an existing results page of the matching layout rather than writing frontmatter from scratch.
- Fundraising: `_data/<year>-auction.csv`, `_data/<year>-raffle.csv`, referenced from a news post with `layout: auction` via `data:`/`raffle:` frontmatter keys (one of the few fields the CMS doesn't expose — set these two keys via a direct GitHub edit, then use the CMS for the rest of the post).
- Photo galleries: race-day galleries are hosted on Google Drive, not committed as image files. Each gallery is a JSON manifest (`_data/<year>-photos-<photographer>.json`, a Drive API file-list response) paired with a Markdown page (`gallery/<year>-photos-<photographer>.md`) whose `gallery_source` frontmatter key must match the JSON filename (without extension). Rendered via `{% include google-gallery %}`. Photos embedded directly in posts/pages (not race-day galleries) go through the CMS image widget and land in `/images/`.

### Navigation

`_data/navigation.yml` is hand-edited only (not CMS-exposed). Entries (top-level or nested under `dropdown:`) support an `enabled: true/false` key used to show/hide seasonal menu items (e.g. "Attending the Derby 2026") without deleting/commenting them out — omitting the key defaults to shown.

### GitHub Actions

`.github/workflows/main.yml` is a manually/dispatch-triggered workflow (`workflow_dispatch` / `repository_dispatch`) that downloads a results CSV from Google Drive and runs `bin/parse_couch_to_html.py` against it, then auto-commits. It does not run on every push and is not a CI/build-check workflow — GitHub Pages builds the Jekyll site separately on push to `master`.

### Misc scripts (`bin/`)

Utility scripts, not part of the build: `parse_couch_to_html.py` (parses a "Couch to Soap Box Derby" training-log CSV into HTML/sqlite), `resample-images.py` (Pillow-based bulk image resizing), `scrape_sbd_images.pl` / `fix_wpmd.pl` (one-off Perl migration helpers).
