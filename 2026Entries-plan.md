# 2026 Race Entries — Opening Plan

Branch: `feature/raceentries`. Scope: open race entries for the 2026 Duxford
Soap Box Derby and get every page that touches entries into a consistent,
correct state.

## Key facts established before editing

- `_data/sbd_details.yml` already has `year: "2026"`, `entry_deadline: "5th
  September 2026"` and 2026 CRUK fundraising URLs — the "current event
  details" rollover was already done in an earlier commit. `entries_open` is
  currently `false`.
- **Race date**: not stored anywhere explicitly. Pattern from prior years is
  deadline = the Saturday before race day, race day = the Sunday. 5th
  September 2026 is a Saturday, so **race day is inferred as Sunday 6th
  September 2026**. This is an assumption — flagging it clearly; the
  committee should confirm before the blog post / T&Cs go live.
- **The route regression**: in commit `3cb71ae` ("First set of 2025
  updates"), the adults' route was rewritten to start/finish at The Plough,
  paraded "down St Peter's St and back up to the farmyard" before the race.
  This is the "down and back up St Peter's Street" route the user has
  flagged as wrong. The route used every year up to and including 2024 (per
  `participating/route-map.md` and `participating/adult-rules.md` /
  `childrens-rules.md` at commit `3cb71ae^`) starts at **The John
  Barleycorn**, carts gather at Graystones and parade to the grid, and
  finishes at **The Plough** — a single-direction traditional route, not a
  loop. Children ran **2 races** (4–7/8–11 combined single lap; 12–15 two
  laps), not 3. This plan reverts route-map.md, adult-rules.md and
  childrens-rules.md to that traditional shape, restoring the original
  Google Maps iframe embeds (the 2025 PNG route images are specific to the
  loop route and won't be reused).
- **No SOP file exists** outside `HOWTO.md` — that doc's "Open race entries"
  and "Phase 2 — Launch" checklist sections are the closest thing to an SOP
  and will be updated for the pay-on-the-day change.
- **No 2026 participant-info PDF exists yet** (only 2025 PDFs are in
  `participating/`). Rather than link a stale 2025 PDF under a "2026"
  heading, the "Race information" section on `participating.md` is being
  removed for now. This needs a follow-up once the committee has a 2026 PDF
  (upload via GitHub, then re-add the section — see HOWTO.md).
- **No `pages/about/programme-of-events-2026.md` existed** and there's no
  confirmed schedule for 2026 (registration/scrutineering windows, road
  closure times, parade timing, pre-derby pub nights all need committee
  sign-off/permits). Created as a genuine **stub**: date, a note that the
  full programme is still being finalised, and just the one thing that was
  specifically asked for — the approximate children's (12 noon) and adults
  (1:30pm) race start times, carried over from 2024. Everything else is
  deliberately left out rather than inferred, to avoid implying road
  closures/timings are settled when they aren't. Linked into
  `_data/navigation.yml` under About → "Race Day 2026" and referenced from
  the entries-open blog post.

## Changes

1. **Route reversion** (`participating/route-map.md`,
   `participating/adult-rules.md`, `participating/childrens-rules.md`):
   restore the John Barleycorn → Plough traditional route text and iframes;
   revert children's race back to 2 races/laps structure.
2. **Year references**: fix remaining 2025/2024 mentions in
   `participating/participating.md`, `participating/register.md`,
   `participating/terms-and-conditions.md`, `_data/navigation.yml`.
3. **Terms and conditions**: update the event date (Sunday 6th September
   2026) and the registration deadline date (5th September 2026) in
   `participating/terms-and-conditions.md`. Content otherwise reviewed —
   no other CRUK-flagged changes are known, so wording stays as-is.
4. **Pay on the day, only**: `participating/rules.md`,
   `participating/register.md`, `participating/entry-request-submitted.md`
   and `participating/pay-race-entry-fee.md` currently describe entry fees
   as pre-paid via a CRUK link or cheque, due by the deadline. Rewritten so
   fees (£5 children's / £10 adults) are paid in cash/card on the day of
   the Event **only** — no advance payment option. The CRUK
   entry-fee-payment redirect on `pay-race-entry-fee.md` is removed (page
   repurposed as a plain notice); the unused `race_entry_fee_url` CRUK field
   stays in `sbd_details.yml`/the CMS for a future year that reverts to
   pre-payment.
5. **HOWTO.md SOP update**: update the "Open race entries" and "Phase 2 —
   Launch" checklists to describe the pay-on-the-day flow instead of
   "payment should be received by the deadline".
6. **Blog post**: new
   `_posts/news/2026-07-12-race-entries-are-open-2026.md`, modelled on the
   2024 entries-open post — announces entries open, the traditional route,
   pay-on-the-day fees, registration deadline, links to register/route
   map/sponsorship.
7. **Banner**: `_data/sbd_details.yml` — set `entries_open: true`, rewrite
   `homepage_banner` text to "Entries are now open!" linking to the new
   post.
8. **Remove 2025 entries info**: drop the "Race information for 2025" PDF
   section from `participating/participating.md` (see PDF note above).
9. **Navigation restructure** (`_data/navigation.yml`): uncomment/enable
   "Register a team" and "Register as a volunteer" under Taking Part now
   that entries are open; drop the stale "Attending the Derby 2025" entry
   (no 2026 equivalent page exists yet — left as a follow-up rather than
   linking a dead page).

## Explicitly out of scope / follow-ups for the committee

- Confirming the actual 2026 race date with the committee/CRUK.
- Uploading the 2026 participant-info PDF and re-adding its link (confirmed
  not to exist yet).
- Filling in pre-derby pub events on `programme-of-events-2026.md` once
  confirmed, and creating an `attending-2026` page (needs real logistics
  detail not available here).
- Confirming the pay-on-the-day change doesn't need a CRUK sign-off (T&Cs
  reference CRUK's fundraising process).
