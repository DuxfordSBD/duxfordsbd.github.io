# Duxford Soap Box Derby

Source for <https://www.duxfordsoapboxderby.co.uk> — a Jekyll site hosted on GitHub Pages, raising money for Cancer Research UK since 2013.

## Editing the site

Most editorial changes are made through the content manager at <https://www.duxfordsoapboxderby.co.uk/admin/> rather than by editing files. See [HOWTO.md](HOWTO.md) for:

- First-time editor setup (GitHub Personal Access Token).
- Common tasks: news posts, pages, the homepage banner, opening/closing race entries, the committee list, the programme of events, photos and galleries.
- The full release checklist for rolling the site over to a new event year.
- What still needs a code edit (navigation, layouts, results CSVs).

## Local development

```bash
docker run -v $(pwd):/site --rm -it -p4000:4000 --entrypoint bash bretfisher/jekyll
# inside the container:
bundle install --retry 5 --jobs 4
bundle exec jekyll server --force_polling --incremental --watch --trace --future --livereload -H 0.0.0.0 --port 4000
```

Open <http://localhost:4000>.

## Licence

Site content © Duxford Soap Box Derby. Theme based on [Feeling Responsive](http://phlow.github.io/feeling-responsive/) (MIT). See [LICENSE](LICENSE).
