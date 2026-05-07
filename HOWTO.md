# How to edit the Duxford Soap Box Derby website

Almost all editorial changes can now be made through the **content manager at <https://www.duxfordsoapboxderby.co.uk/admin/>**, without touching code. This document explains what lives where and how to do each task.

If something cannot be done from `/admin/`, you will need to edit the repo directly on GitHub or locally — see "Editing files directly" at the bottom.

---

## First-time setup for a new editor

Each editor signs in with their own GitHub Personal Access Token. The token
lives only in the editor's browser; nothing is shared.

1. Make sure your GitHub account is a collaborator on <https://github.com/DuxfordSBD/duxfordsbd.github.io>. Ask the website maintainer to add you if not.
2. Generate a fine-grained Personal Access Token: - Go to GitHub → click your avatar (top right) → **Settings**. - Scroll to the bottom of the left sidebar → **Developer settings**. - **Personal access tokens** → **Fine-grained tokens** → **Generate new   token**. - **Token name**: anything, e.g. "Duxford Soap Box CMS". - **Expiration**: pick up to 1 year. (You will be asked to regenerate   when it expires — that's normal.) - **Repository access** → **Only select repositories** → choose   `DuxfordSBD/duxfordsbd.github.io`. - **Permissions** → **Repository permissions** → set **Contents** to   **Read and write**. (Metadata: Read is added automatically.) - Click **Generate token** and **copy the token** immediately. It will   never be shown again.
3. Visit <https://www.duxfordsoapboxderby.co.uk/admin/>.
4. Click **Sign In with Token**, paste the token, press OK.

You stay signed in on that browser until you sign out or clear cookies.

If you lose the token, delete it on GitHub and generate a new one — there is no way to recover an existing one.

---

## What you can edit, and where

The CMS sidebar lists the editable areas:

| Section in CMS | What it edits | Files in the repo |
| --- | --- | --- |
| **Site settings → Current event details** | Year, entry deadline, race-entries-open toggle, homepage banner, CRUK fundraising URLs | `_data/sbd_details.yml` |
| **Site settings → Committee, helpers and CRUK representatives** | The lists rendered on `/about/committee` | `_data/committee.yml` |
| **News posts** | Every news article on the site | `_posts/news/*.md` |
| **Information pages** | About, Contact, Donate, Privacy Policy, Thanks, etc. | `pages/*.md` |
| **About pages** | "With thanks to", programmes of events, attending info | `pages/about/*.md` |
| **Participating pages** | Rules, registration, sponsorship, volunteer, route maps, terms and conditions | `participating/*.md` |

Anything not in that list (custom layouts, themes, navigation menu, build configuration, results CSVs, gallery JSONs) requires a code edit — see "Editing files directly".

---

## Common tasks

### Open or close race entries

1. Open `/admin/`.
2. **Site settings → Current event details**.
3. Toggle **Race entries open** ON or OFF.
4. **Save**.

When OFF: `/participating` shows "Entries are currently closed", and
`/participating/register` shows the same closed message instead of the form.

When ON: both pages show the registration form and call-to-action.

The site rebuilds automatically and is usually live within 1–2 minutes.

### Change the homepage banner

The banner is the bold message that sits above the news on the homepage.

1. **Site settings → Current event details** → **Homepage banner**.
2. Fields: - **Show banner** — turn the whole banner on or off. - **Use red highlight colour** — turn ON for urgent / time-sensitive   notices (looks more attention-grabbing). Leave OFF for normal messages. - **Banner text** — the main message. - **Link URL** — optional. The path the banner links to. Use the   permalink of the news post you're advertising, e.g.   `/news/duxford-soap-box-needs-you-2026`. Leave blank for a banner with   no link. - **Link text** — wording for the link, e.g. "Find out more in our blog   post".
3. **Save**.

To replace one banner with another (e.g. switching from "volunteers wanted" to "entries open"), just rewrite the text and link — there is no need to keep history; old wording is preserved in git.

### Update the year or entry deadline

**Site settings → Current event details** → change **Event year** or
**Entry deadline** → **Save**.

These values are pulled in automatically by the participation pages, sponsorship page, event disclaimer, and several news posts that use `{{ site.data.sbd_details.year }}` and `{{ site.data.sbd_details.entry_deadline }}`.

You no longer need to search-and-replace year numbers across the site for those references.

### Update the Cancer Research UK fundraising URLs

CRUK creates new fundraising pages each year, with the year baked into the URL. To swap them over:

1. Open `/admin/`.
2. **Site settings → Current event details** → expand **Cancer Research UK fundraising URLs**.
3. Paste the new URLs into the four fields:
   - **General donation page URL** — the page `/donate` redirects to, also linked from `/donate`.
   - **Team fundraising page URL** — used on `/participating/sponsorship`.
   - **Race entry fee payment URL** — the page `/participating/pay-race-entry-fee` redirects to.
   - **Auction item payment URL** — used on `/donate` for paying for auction lots.
4. **Save**.

The four pages above pick up the new URLs automatically — there is no other place to update.

### Edit the committee list

The lists shown on `/about/committee` are stored as structured data, not free text. Add, remove or reorder members from the CMS form:

1. Open `/admin/`.
2. **Site settings → Committee, helpers and CRUK representatives**.
3. Three lists are available:
   - **Current committee** — the people running the next event.
   - **Past committee members** — historical record.
   - **Committee helpers** — non-committee volunteers worth recognising.
4. For each entry:
   - **Name** — required. Just the name.
   - **Role** — optional. Used for Chair, Treasurer, CRUK representative, etc. Leave blank for ordinary members. Renders as "Name (Role)" on the page.
5. Use the up/down arrows to reorder, the trash icon to remove, or **Add** to create a new entry.
6. **Save**.

When rolling over to a new event year, the typical change is moving people from "Current" to "Past", and adding any new members.

### Write a news post

1. **News posts** → **New news post**.
2. Fill in: - **Title** — required. Plain text. - **Teaser** — short tagline shown on the homepage and listings. - **SEO description** — optional; appears in Google results. - **Layout** — leave as `page`. Use `auction` only for the annual   auction post; `video` for posts whose content is mainly a video. - **Custom permalink** — optional. Use this when you want a tidy URL   like `/news/charity-auction-raffle-2026`. If you leave it blank, an   automatic URL is generated from the date and title. - **Header style** — leave blank. Set to `no` only if you specifically   want to hide the page header on the post. - **Images** — three optional images. The same image can usually be   used for all three:   - **Main image**: shown at the top of the article.   - **Thumbnail**: shown on listings.   - **Homepage image**: shown on the homepage if this is the latest post. - **Categories** — leave as `news`. - **Tags** — at least `news`. Add others (e.g. `announcement`,   `auction`, `2026`) to help future filtering. - **Body** — write the post in Markdown. Use the formatting toolbar for   headings, links, lists, and image embeds.
3. **Save**.

Behind the scenes a file like `_posts/news/2026-04-12-my-post-title.md` is created and committed to the repo, and the site rebuilds automatically.

### Edit an existing news post

**News posts** → click the post → make changes → **Save**.

Avoid changing **Custom permalink** on a post that is already public — that breaks any external links to it.

### Edit a static page (About, Contact, Privacy Policy, etc.)

1. Pick the right collection: - General pages → **Information pages**. - Pages under `/about/...` → **About pages**. - Pages under `/participating/...` → **Participating pages**.
2. Click the page → make changes → **Save**.

Useful field notes for pages:

- **Permalink** — do not change on existing pages. It is the URL of the page and changing it breaks links from search engines, social media, posters, etc.
- **Layout** — almost always `page`. `redirect` is for short pages whose only job is to forward visitors elsewhere (e.g. the donate page).
- **Header image** → **Full-width header image** — most pages use `duxford-soapbox-derby-header.jpg`. Leave it on that unless you have a specific reason to change.
- **Body** — Markdown. Use the toolbar for formatting, links, and images.
- **Redirect URL** (Information / Participating pages) — only used when layout is `redirect`. Holds the destination URL.

### Create or update the programme of events page

The programme of events page (`/about/programme-of-events-YYYY`) is the chronological run-down of everything happening over derby weekend — pre-derby events at local pubs, race-day timings, road closure times, the parade route, prize giving, after-race entertainment. There is one page per year, named by the year (e.g. `programme-of-events-2026.md`). See `pages/about/programme-of-events-2025.md` as the working example.

#### Creating the new year's page

The fastest path is "copy last year's file then edit". This needs a one-time GitHub edit because the CMS can edit existing About pages but does not support copying one to a new filename.

1. Open <https://github.com/DuxfordSBD/duxfordsbd.github.io/blob/master/pages/about/programme-of-events-2025.md>.
2. Click the **Copy raw file** icon (the two-overlapping-squares icon at the top of the file view).
3. Click **Add file → Create new file** anywhere in the repo, then put `pages/about/programme-of-events-2026.md` in the filename box (the slashes navigate into the right folder).
4. Paste the copied content.
5. In the frontmatter, change `2025` to the new year in **all three** of `title`, `meta_title`, and `permalink`.
6. Commit straight to `master` with a message like "Add programme of events for 2026".

From here on, edit the page through the CMS at **About pages → Programme of events 2026** — the CMS body editor is friendlier than the GitHub editor for this kind of content.

#### What goes on the page

Structure year-on-year is stable; only the specifics change. Keep the same `### Day` heading pattern as the previous year so layout stays consistent.

- **Opening line** — sets the date and links to the location. Update the date.
- **Pre-derby events** (Wednesday/Friday/Saturday before the race) — local pubs and venues run bingo nights, family fun days, silent discos, casino nights, etc. These are usually confirmed close to the race; it is fine to leave the section empty or partially filled until details are known. Each entry typically has: venue name (linked to its Facebook page), date, time, what's happening, ticket info if any.
- **Race day** — the structure is always:
  1. Registration / scrutineering / racers' briefing — time and venue.
  2. **Road closures start** at a given time — confirm with the road-closure logistics lead.
  3. Parade of carts — start time, route from registration to the start line.
  4. Children's race — noon, with sub-categories (4–7, 8–11, 12–15) and the children's prize presentation.
  5. Adults' race — typically 1:30pm, with the Phill Hill Cup and any new categories (e.g. elite, veterans).
  6. After-race — presentation of awards, live music, face painting, auction and raffle draw, food and drink on sale.
  7. **Road closures end** at a given time.

When you change the start pub or any venue, update both the heading link and the address line under it.

#### After the page exists

- Update [_data/navigation.yml](_data/navigation.yml): add or update the **About → Programme of Events** dropdown entry to point at the new permalink. Use `enabled: false` until you're ready to make it public, then flip to `enabled: true` (see "Show or hide a navigation menu entry").
- The first news post that announces the new derby (and the race-weekend "what's happening" post) should link to it.

### Add photos to the site

Two different workflows depending on what the photos are for.

#### Photos used in news posts and pages

Use the CMS. Any image field on a news post or page accepts a file upload — the file is committed to `/images/` in the repo and the post stores just the filename, matching the existing convention.

1. **News posts** (or **About pages** / **Information pages** / **Participating pages**) → open or create the post.
2. Click the relevant image field (e.g. **Main image**, **Thumbnail**, **Homepage image**, or **Header image**). The CMS opens an asset picker.
3. Either pick an existing image from `/images/` or click **Upload** and choose a file from your computer. JPGs and PNGs are both fine.
4. Save the post.

Tips:

- The CMS uses the filename you uploaded as-is. Rename your file to something descriptive *before* uploading — `2026-adults-podium.jpg` is much easier to reuse later than `IMG_1234.jpg`.
- Resize large camera/phone photos to ~1600px wide before uploading. The site doesn't auto-resize, and a 6 MB photo makes the page slow.
- For body images (inline in post text), use the markdown editor's image button — same upload flow.

#### Race-day photo galleries (Google Drive hosted)

Race-day galleries are not stored in the repo. They live in **Google Drive** and are embedded into a gallery page via a JSON manifest. This is how previous photographer galleries work (e.g. `gallery/2025-photos-delcanton.md` ↔ `_data/2025-photos-delcanton.json`).

1. **Upload the photos to Google Drive** in a single folder. Name the folder something like `2026 Duxford Soap Box Derby — <photographer name>`.
2. **Make the folder publicly accessible**: right-click the folder → **Share** → **General access** → **Anyone with the link** → **Viewer**. This must be set on the folder itself; the files inherit it.
3. **Note the folder ID** from the URL bar. In `https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOp`, the ID is `1AbCdEfGhIjKlMnOp`.
4. **Generate the file manifest**. The site needs a JSON listing of every photo in the folder. The simplest path is to run the Drive API "Files: list" call from <https://developers.google.com/drive/api/v3/reference/files/list>:
   - Query (`q`): `mimeType contains 'jpeg' and parents = '<FOLDER_ID>'`
   - **pageSize: 1000** — without this you get only the first 100, leaving photos missing.
   - Click **Execute**, copy the response JSON.
5. **Commit the manifest**: in the repo, create `_data/2026-photos-<photographer>.json` and paste the response. The structure should match the existing files (a `files` array of objects with `id`, `name`, `mimeType`, etc. — see [_data/2025-photos-delcanton.json](_data/2025-photos-delcanton.json) for an example).
6. **Create the gallery page**: in `gallery/`, create `2026-photos-<photographer>.md` modelled on [gallery/2025-photos-delcanton.md](gallery/2025-photos-delcanton.md). The contents should look like:

   ```markdown
   ---
   layout: page-fullwidth
   header:
     image_fullwidth: duxford-soapbox-derby-header.jpg
   gallery_source: "2026-photos-<photographer>"
   title: Duxford Soap Box Derby 2026 Photo Gallery
   ---
   Photos provided courtesy of [Photographer Name](https://example.com). Any reuse must include attributing the original photographer.

   {% raw %}{% include google-gallery %}{% endraw %}
   ```

   The `gallery_source` value must match the JSON filename without the `.json` extension. `gallery_source` and `title` are siblings of `header`, **not** nested under it.
7. **Add the gallery to the navigation**: edit `_data/navigation.yml` and add a new entry under the **Gallery** dropdown pointing at the new page's permalink. Make sure the **Gallery** top-level entry points at the most recent gallery URL.
8. **(Optional) Captions**: edit `_data/captions.yml` to add captions keyed by the photo filename (the `name` field from the JSON manifest).

The CMS does **not** edit gallery pages, the JSON manifests, or `captions.yml` — these are all GitHub-direct edits. Once the page exists, you can use the CMS to tweak the surrounding text on the gallery markdown file via **About pages** (if it lives there) — but for now `gallery/` isn't exposed as a CMS collection, so use the GitHub web UI for everything in that folder.

### Roll over to a new event year

1. **Site settings → Current event details**:
   - Update **Event year** (e.g. `2025` → `2026`).
   - Update **Entry deadline** (e.g. `30th August 2026`).
   - Set **Race entries open** to OFF until you're ready to open them.
   - Update the **Homepage banner** to the new year's message (or turn it off until you have something to say).
   - Update the four **Cancer Research UK fundraising URLs** with the new pages CRUK has set up for this year's event.
2. **Site settings → Committee, helpers and CRUK representatives**: move anyone who has stepped down from **Current committee** into **Past committee members**, and add any new people.
3. **News posts → New news post**: write the announcement post for the new derby. Use a previous year's post as a template (e.g. open last year's post, copy the body, rewrite the dates).
4. **About pages → with-thanks-to**: add anyone who helped with the previous year's event.
5. **About pages**: create the new programme of events page (use the previous year's as a template).
6. Ask the website maintainer to update `_data/navigation.yml` to point at the new programme of events page. The navigation menu is not editable through the CMS — see "Editing files directly" at the bottom.

### Open race entries

1. **Site settings → Current event details** → set **Race entries open** to ON → **Save**.
2. **News posts → New news post**: announce that entries are open (model on previous years' posts).
3. Update the **Homepage banner** to advertise that entries are open and link to the new news post.
4. Check terms and conditions with CRUK before publishing.

### Close race entries after the deadline

**Site settings → Current event details** → set **Race entries open** to OFF → **Save**.

### Add the post-event "raised total"

1. **News posts → New news post**: write the cheque-presentation / total-announced post (model on previous years').
2. **Homepage banner**: edit the text to celebrate the total, and link to the new news post.

---

## Releasing the site for a new event year

A checklist for the typical lead-up to a new derby. Steps marked **CMS** can be done from `/admin/`. Steps marked **code** need a direct repo edit (the GitHub web UI works fine for almost all of these — see "Editing files directly" below).

Don't tick everything in one sitting; the natural ordering is roughly the three phases below.

### Phase 1 — Pre-launch (long before entries open)

The goal is to have the site truthful for the new year before any announcements go out.

- [ ] **CMS — Site settings → Current event details**:
  - [ ] Update **Event year** and **Entry deadline**.
  - [ ] Update the four **Cancer Research UK fundraising URLs** (CRUK creates fresh pages each year).
  - [ ] Leave **Race entries open** OFF for now.
  - [ ] Update **Homepage banner** — typically a "save the date" message linking to a news post.
- [ ] **CMS — Site settings → Committee**: move anyone who has stepped down into Past, add new members to Current.
- [ ] **CMS — Participating pages → Terms and Conditions**: review every dated reference; update wording, dates, anything CRUK has flagged.
- [ ] **CMS — Participating pages → General Rules / Adult Race / Children's Race**: update fees, age rules, entry deadlines if changed.
- [ ] **CMS — Participating pages → Sponsorship**: skim for stale year references; the team URL is handled automatically once you've updated the CRUK URLs above.
- [ ] **CMS — News posts → New news post**: write the announcement post for the new derby, modelled on a previous year's post (e.g. `2025-02-15-duxford-soap-box-derby-2025.md`). Set a tidy permalink like `/news/duxford-soap-box-derby-2026`.
- [ ] **Code — `participating/`**: upload the new participant-info PDF (e.g. `2026-information-racers-v1.pdf`). Then update the link in [participating/participating.md](participating/participating.md) — search for the old PDF filename and replace.
- [ ] **Code + CMS** — Create the new programme of events page. See **Create or update the programme of events page** above for the full procedure (copy last year's file via GitHub, then edit content via the CMS).
- [ ] **Code — `_data/navigation.yml`**: point the **About → Programme of Events** dropdown at the new file. Use `enabled: true/false` (see "Show or hide a navigation menu entry") to toggle visibility of the new programme entry until you're ready.

### Phase 2 — Launch (open race entries)

- [ ] **CMS — Site settings → Current event details**: set **Race entries open** to ON.
- [ ] **CMS — News posts → New news post**: announce that entries are open. Set a tidy permalink like `/news/race-entries-are-open-2026`.
- [ ] **CMS — Site settings → Current event details → Homepage banner**: change to "Race entries are now open!" with the link pointing at the announcement post. Optionally turn on **Use red highlight colour** for the first couple of weeks.
- [ ] Cross-check **Participating pages → Register a team**: open `/participating/register` in a browser, walk through the form once. Confirm the entry-fee link goes to the right CRUK page.

### Phase 3 — Closer to race day

- [ ] **Code — `_data/2026-auction.csv` and `_data/2026-raffle.csv`**: create new CSVs with the year's auction lots and raffle prizes. Use `_data/2025-auction.csv` and `_data/2025-raffle.csv` as templates — keep the same column headers. Use a spreadsheet like Excel to do this
- [ ] **CMS — News posts → New news post**: charity auction and raffle teaser, set **Layout** to `auction`. In the source markdown set `data: 2026-auction` and `raffle: 2026-raffle` to point at the new CSVs (this is one of the few news fields the CMS doesn't expose — open the post on GitHub to add those keys, then return to the CMS for everything else).
- [ ] **CMS — Site settings → Homepage banner**: switch to a race-weekend message — road closures, where to park, what to bring.
- [ ] **CMS — News posts → New news post**: a "what's happening on the race weekend" post with timings, road closures, and a link to the new programme of events page.
- [ ] **Code — `_data/navigation.yml`**: enable any seasonal entries (e.g. **Attending the Derby 2026**, **Charity Auction and Raffle 2026**) by flipping `enabled: true`.

### After race day

- [ ] **Code — `_data/2026-adults-results.csv`, `_data/2026-childrens-results.csv`** etc.: upload race results CSVs.
- [ ] **CMS — News posts → New news post**: results announcement. Use the CMS image fields to attach a podium / event photo (see **Add photos to the site** above).
- [ ] **CMS — Site settings → Current event details**: set **Race entries open** back to OFF and update the homepage banner.
- [ ] **Code — `_data/navigation.yml`**: disable the seasonal entries again, add the new year's results page to the **Race Results** dropdown.
- [ ] **Code + Google Drive** — When a photographer's gallery is ready, publish it: see **Race-day photo galleries (Google Drive hosted)** in **Add photos to the site** above. Add the new gallery to the **Gallery** dropdown in `_data/navigation.yml`.
- [ ] Once the cheque is presented, follow "Add the post-event 'raised total'" above.

---

## Editing files directly (when the CMS isn't enough)

Some changes still require editing repo files directly:

- Navigation menu (`_data/navigation.yml`)
- Theme, layouts, styling (`_layouts/`, `_includes/`, `_sass/`)
- Build / plugin configuration (`_config.yml`, `Gemfile`)
- Adding new collections to the CMS (`admin/config.yml`)
- Bulk image uploads, gallery JSON files (`_data/*.json`)
- Race results CSVs (`_data/*-results.csv`)

You can do this in two ways:

1. **In the GitHub web UI**: navigate to the file on <https://github.com/DuxfordSBD/duxfordsbd.github.io>, click the pencil icon, edit, commit. This works for one-off changes.
2. **Locally**: clone the repo, make changes on a branch, push and open a pull request. Required for larger changes.

### Show or hide a navigation menu entry

Some menu items are seasonal — for example "Attending the Derby 2025" should appear in the About dropdown when the page is current and disappear the rest of the year. Rather than commenting and uncommenting YAML, add an `enabled:` field to the entry and toggle it.

In `_data/navigation.yml`, any entry (top-level or inside a `dropdown:`) can have an optional `enabled` key:

```yaml
- title: "Attending the Derby 2025"
  url: "/about/attending-2025"
  enabled: false   # flip to true to show in the menu
```

- `enabled: false` hides the entry.
- `enabled: true` (or omitting the key entirely) shows it.

Edit the file on GitHub, change `false` to `true`, commit. The site rebuilds in 1–2 minutes and the menu item appears.

### Building locally to preview changes

```bash
docker run -v $(pwd):/site --rm -it -p4000:4000 --entrypoint bash bretfisher/jekyll
# Wait until the container starts, then inside the container:
bundle install --retry 5 --jobs 4
bundle exec jekyll server --force_polling --incremental --watch --trace --future --livereload -H 0.0.0.0 --port 4000
```

Open <http://localhost:4000> in a browser.

---

## Troubleshooting

**The CMS says "Authentication failed".**
Your token may have expired (fine-grained PATs last up to 1 year), been revoked, or never had the right permissions. Generate a new one and sign in again — see "First-time setup" above.

**My change has saved but the site doesn't show it.**
Wait 1–2 minutes for GitHub Pages to rebuild. Hard-refresh the page (Cmd+Shift+R / Ctrl+F5) to bypass the browser cache. If it still doesn't appear after 5 minutes, check the **Actions** tab on the GitHub repo for a failed build.

**I see "404" or a strange page after editing.**
You probably changed the **Permalink** on an existing page. Set it back to the original value and save again.

**The CMS shows fields I don't recognise (`subheadline`, `redirect_to`, etc.).**
Those exist for compatibility with a small number of older pages. If a field is blank on the page you're editing, leave it blank.

**I want to add a new section to the CMS.**
Edit `admin/config.yml` and add a new collection. See the existing collections in that file as templates.
