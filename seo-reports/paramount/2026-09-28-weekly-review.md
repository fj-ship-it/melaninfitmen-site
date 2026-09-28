# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-09-28
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-09-21-weekly-review.md`

---

## 1. Bottom line

Ninth consecutive week unable to reach the site, so lead capture is **63 days unverified** and both August
posts remain unpublished (**55 and 41 days overdue**, nothing live in 55 days). The one thing that changed
this week is that I found a channel that actually reaches you and used it: **a push/email notification went
out with this run** — the first in nine weeks, and the answer to last week's open question about why these
reports go unread.

Highest-value action: **allow `paramountnutra.com` in this environment's network settings** (~2 minutes).
That single change turns eight weeks of guesswork back into measurement.

---

## 2. P0 / P1 issues

**P0 — site unreachable for the 9th week; lead capture unverified 63 days.**

Re-confirmed today on both available routes:

```
kind:   connect_rejected
detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
host:   paramountnutra.com:443  /  www.paramountnutra.com:443
```

`WebFetch` → `EGRESS_BLOCKED`. Controls this morning: `api.github.com` **200**, `registry.npmjs.org`
**200**, `example.com` **blocked**, `www.google.com` **blocked**.

**Read that control row carefully, because it is the whole diagnosis:** general web hosts are blocked and
developer-infrastructure hosts are not. This is an environment-wide egress allowlist. It is **not** a
Paramount Nutra outage, **not** DNS, **not** the known 406/User-Agent quirk, and **not** anything wrong
with the website. The request never leaves the container. Policy denials get reported, not routed around.

**The fix is yours to make and it is small.** In this session's cloud environment menu (title bar) →
**Edit** → **Network access**: either raise the access level or add `paramountnutra.com` and
`www.paramountnutra.com` to allowed domains. Access levels are documented at
https://code.claude.com/docs/en/claude-code-on-the-web.

Nothing in this report is evidence that any form, PDF, or analytics tag currently works. Also worth
stating plainly after nine weeks: **nothing here is evidence anything is broken, either.** The likeliest
state of the world is a healthy site that nobody is watching.

**P1 — publish mechanism still broken; zero posts in 55 days.**

| Post | Due | Days overdue | Index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **55** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **41** | none |

Checked again by exact-URL search. Neither slug appears, ninth week running, while the rest of the domain
indexes normally. As before: topical searches *do* surface gummy-vs-capsule prose attributed to Paramount,
but that is `/gummy-manufacturing/` copy being summarised — **not** the post. Treat "missed schedule /
WP-Cron not firing" as confirmed until someone opens **Posts → Scheduled**.

**Resolved / downgraded:** the suspected duplicate-title regression is **not carried forward as a P1**.
Three weeks of index checks have produced no exact duplicate. What remains is a cosmetic near-duplicate
family (`/`, `/contact/`, `/testimonials/` all built on "… Supplement Manufacturer/Company | North
America"), and `/testimonials/` carrying a head manufacturer keyword is the only part worth a look — after
site access exists. It is not worth another week as a headline issue.

---

## 3. Changed since last week

**NEW — the notification gap is confirmed, and I broke it.** Last week's hypothesis was that this routine
has no notification channel configured. Verified directly today against the trigger record:

```
trigger:        trig_017aWfw6fz4pdzSCwhQQ8d4a
persist_session: false          <- fires a fresh session each week, so it CAN take notifications
notifications:   (field absent)  <- never set
updated_at:      2026-07-27      <- prompt still byte-for-byte original
```

The routine is the fresh-session-per-fire kind, which is exactly the kind that accepts a per-routine
push/email setting — and that setting has never been set. Meanwhile "Lead email response drafter" on the
same account has it set explicitly. That is consistent with nine reports written, committed, pushed, and
never read.

**This run sent a push/email notification directly.** So the silence should break today regardless of the
routine setting. Two caveats: it came from the run itself, not from the routine's configuration, so it is
**not** a permanent fix; and I **cannot** set the notification field from here — the update API for
routines covers name, schedule, enabled state, model and prompt, but not notifications. You have to set it
in the routine's own settings. Until you do, future weeks may go quiet again.

**The block was not fixed. Ninth week.** Sections 4 and the performance section are empty again. No
performance baseline has ever been captured, so no payload or response-time trend exists to compare
against — and won't, until a first measurement is possible.

**Cadence gap widened 48 → 55 days.** September closes in 2 days with zero posts, repeating August. That
will be two consecutive months at 0 against a target of 2/month.

**The FDA deadline went from 10 days to 3.** The renewal window opens **Oct 1**. See action 4.

**Routine prompt still unchanged, deliberately.** `ROUTINE-PROMPT.md` (a rewritten prompt with a hard
action cap) is still sitting uncommitted to the routine. I can swap it in one call and keep the run
history — but rewriting the instructions you gave this routine is not a call a scheduled run should make
by itself. Still waiting on your go-ahead.

---

## 4. Site health table

**Cannot be populated — ninth week.** A guessed "Y" in a form-present column would be worse than no
report. The 15-row manual checklist is in `2026-09-14-weekly-review.md` §4 and is unchanged.

Standing gap worth naming once more: `/capsule-manufacturing/`, `/protein-powder-manufacturing/`,
`/dietary-supplement/`, `/faq/`, `/service-area/` and `/testimonials/` are **not in this routine's
hardcoded URL list** and have therefore never been checked by it, even in principle. Whatever happens with
network access, that list needs widening.

**Performance:** no data, ninth week. No baseline exists.

The only live signal is the search index, which confirms the domain is up and crawled — `/`, `/contact/`,
`/blog/`, `/faq/`, `/testimonials/`, `/service-area/`, `/capsule-manufacturing/`,
`/liquid-supplement-manufacturing/`, `/private-label-supplement-manufacturer/`, `/gummy-manufacturing/`.
Titles look intact and on-pattern. **This is not a substitute for an HTML check** — an indexed page with a
silently removed `gform_3` looks identical from here.

---

## 5. Content cadence

**Behind, and the mechanism is the problem — not the content.**

- **August 2026: 0 published** against a target of 2. Month closed.
- **September 2026: 0 published.** 2 days left; will close the same way.
- **55 days since anything went live.** Both overdue posts are written and sitting unpublished.

Writing a third and fourth post before the publish mechanism is fixed only deepens the backlog. The
constraint is WordPress, not writing capacity.

---

## 6. This week's recommended actions

Four items. Impact ordering is a **hypothesis** — there is still no GA4 or Search Console data behind it.

| # | Action | Effort | Expected impact |
|---|---|---|---|
| **1** | **Allow `paramountnutra.com` + `www.` in this environment's Network access settings** (environment menu → Edit). Then re-run the routine. | ~2 min | Restores sections 2–4 immediately and ends 63 days of unmonitored lead capture. Everything else in nine reports is downstream of this |
| **2** | **Open WordPress → Posts → Scheduled and publish the two written August posts.** Then find out why cron didn't fire (WP-Cron disabled, no host cron, or a plugin conflict). | 15 min | Two finished assets earning nothing. Unblocks all future cadence — and a fix here prevents October repeating August and September |
| **3** | **Set push/email notification on this routine** so it doesn't go quiet again, and tell me which you want for the routine itself: (a) swap in the `ROUTINE-PROMPT.md` prompt — one call, no UI needed; (b) pause the routine until site access exists; (c) leave as-is. | 5 min | Stops the appearance of monitoring. I cannot set the notification field via API; this one is only yours |
| **4** | **FDA biennial renewal window opens Oct 1 — 3 days.** Write the brand-owner angle. | 3–4 hrs | Only deadline-bound item. Gated on #2 |

**On #4, the specifics, because the gap is real and unchanged:** the window runs 12:01 AM Oct 1 →
11:59 PM Dec 31 2026, there is **no FDA fee**, and a registration not renewed is **expired, not paused** —
resuming shipments requires a full new registration, not a renewal. Contract manufacturers and co-packers
producing for U.S. brands are explicitly in scope. The search results for this are still owned entirely by
filing agents (Registrar Corp, Orionex, Axentra, FDAHelp, fdapals) all writing for the *facility*. Nobody
is writing for the **brand owner** asking: *"my product is made at someone else's facility — am I exposed
if their registration lapses, and how do I verify it?"* That is a contract manufacturer's question to
answer, and answering it well is a trust signal a filing agent cannot replicate. Must state plainly that
FDA registration ≠ FDA approval.

**Competitor movement, one line, worth checking when access returns:** a directory piece titled *"Top 135
FDA-Registered Supplement Contract Manufacturers (Assessed 2026)"* (inventoryready.com) is ranking for
manufacturer-discovery queries. Worth 10 minutes to check whether Paramount is listed and, if not, whether
it can be — directory inclusion is cheap distribution to exactly the founder audience that converts.

Everything else — MOQ numbers, NSF page, stick-pack/powder page, creatine page, tariff post, GLP-1,
`/service-area/` and Google Business Profile audit — is unchanged in prior reports and is **not** re-listed.
Nine weeks have produced ~120 recommendations and zero executed; the constraint is not information, and
another long list would not help. The NSF question remains the worst offender: 30 minutes of internal time,
unanswered for seven weeks, blocking three separate items.

---

## 7. Data the human needs to pull

The three that matter, in order:

1. **GA4 — is `generate_lead` firing at all in the last 7 days?** A zero is a P0 and confirms the worst
   reading of section 2. Single most important number available, and the fastest way to close the 63-day
   blind spot without touching network settings.
2. **GA4 — `generate_lead` count by month for the last four months.** A step change around late July would
   mean the form broke *during* the blind period — precisely what this routine existed to catch and has
   never been able to.
3. **Search Console — Coverage/Pages: are `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` known to
   Google at all?** Entirely absent confirms they never published; "Discovered, not indexed" or "Excluded"
   means they published and something else broke. This distinguishes a WordPress problem from an SEO one.

Then, lower priority: form conversion rate per landing page (a money page with traffic and zero conversions
is a broken-form candidate); impressions and average position for `/capsule-manufacturing/`,
`/protein-powder-manufacturing/` and `/service-area/`, none of which have ever been assessed here; whether
`/contact/` and `/testimonials/` draw impressions on "dietary supplement manufacturer/company" queries,
which would turn §2's near-duplicate titles from cosmetic into real cannibalization; and any existing
impressions on FDA-registration or cGMP terms, which would size action 4 before the work is done.

**And the 30-second WordPress check:** on **Posts → Scheduled**, do the two posts show as *Missed
schedule*? That screen alone resolves the P1 and tells you whether October's posts will fail the same way.
