# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-09-21
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-09-14-weekly-review.md`

---

## 1. Bottom line

Eighth consecutive week unable to reach the site: lead capture is **56 days unverified** and both August
posts are still unpublished (**48 and 34 days overdue**, zero posts live in 48 days). This report is
deliberately short — eight weeks have produced ~120 recommendations and zero executed, so the constraint
is not information and another long list would not help.

The single highest-value action is not an SEO action: **find out why eight weekly reports have produced
no response.** Section 3 has a concrete, checkable hypothesis with evidence — this routine appears to
have no push/email notification configured, while another routine on the same account explicitly does.
If that is right, these reports have been landing in a git repo that nobody is being told about, and
every other finding in every prior report is downstream of it.

---

## 2. P0 / P1 issues

**P0 — site unreachable for the 8th week; lead capture unverified 56 days.**
`connect_rejected` / gateway 403 to CONNECT on `paramountnutra.com:443` and `www.` (curl exit 56,
HTTP 000; `WebFetch` → `EGRESS_BLOCKED`). Controls today: `api.github.com` 200, `registry.npmjs.org` 200,
`example.com` **blocked**, `www.google.com` **blocked**. This is an environment-wide developer-infra
allowlist, not a block aimed at this domain and not a site outage. Policy 403s are reported, not routed
around. The allowlist fix has been written up seven times; it is not re-argued here.

Nothing in this report is evidence that any form, PDF, or analytics tag currently works.

**P1 — publish mechanism still broken; zero posts in 48 days.**

| Post | Due | Days overdue | Index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **48** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **34** | none |

Checked today by exact-URL search (`"paramountnutra.com/gummy-vs-capsule"`,
`"paramountnutra.com/what-cgmp-actually-means"`) and by topic. Neither slug appears, eighth week running,
while the rest of the domain indexes normally (10 URLs returned, section 4). Note: topical searches *do*
surface gummy-vs-capsule prose attributed to Paramount — that is `/gummy-manufacturing/` copy being
summarised, **not** the post. Treat "missed schedule / WP-Cron not firing" as confirmed until someone
opens **Posts → Scheduled**.

**P1 (suspected) — near-duplicate title family, partially downgraded.** No *exact* duplicate is visible
in the index this week, and `/dietary-supplement/` did not surface at all, so last week's specific
`/contact/` vs `/dietary-supplement/` pairing is **not confirmed**. What is visible is a family of three
near-identical manufacturer-keyword titles:

- `/` → "Dietary Supplement **Manufacturer** | North America - Paramount Nutra"
- `/contact/` → "Dietary Supplement **Company** | North America – Paramount Nutra"
- `/testimonials/` → "**Food** Supplement **Manufacturer** | North America - Paramount Nutra"

`/testimonials/` carrying a head manufacturer keyword is the more interesting of the two: a social-proof
page is titled as if it were a service page, competing with the homepage. Verify against live HTML before
editing — index titles lag.

---

## 3. Changed since last week

**The block was not fixed. Eighth week.** Sections 4 (health) and performance are empty again. No
performance baseline has ever existed, so no payload or response-time trend can be computed this week or
any future week until a first measurement is taken.

**Cadence gap widened 41 → 48 days.** September closes in 9 days with zero posts, repeating August.

**NEW — verified: last week's #1 process fix was never applied, and the reason given for that was wrong.**
`ROUTINE-PROMPT.md` (committed 2026-09-07) contains a rewritten routine prompt with a hard five-action cap
and a stop rule, and states *"the routine was created through the web UI, so it must be edited there — an
agent cannot update it."* Checked directly today:

```
trigger:    trig_017aWfw6fz4pdzSCwhQQ8d4a  "Paramount Nutra — Weekly SEO & Lead-Gen Review"
created_at: 2026-07-27T17:11:10Z
updated_at: 2026-07-27T17:11:10Z   <-- never modified since creation
```

The prompt that fired today is byte-for-byte the original. **And the stated blocker does not hold** — this
session has an `update_trigger` tool that can replace a routine's prompt in one call, keeping its ID and
run history. So the swap is a ~1-minute change, not a manual UI errand. *It has not been done, and will
not be done without Frank's explicit go-ahead* — silently rewriting the instructions Frank gave this
routine is not something a scheduled run should decide on its own. See action 2.

**NEW — a checkable hypothesis for why eight weeks produced nothing.** Comparing routine configs on this
account:

| Routine | Notifications field |
|---|---|
| "Lead email response drafter" | `{push: true, email: false}` — **explicitly set** |
| "Email triage", "Briefing" | not set |
| **"Paramount Nutra — Weekly SEO"** | **not set** |

This is a hypothesis, not a finding: I cannot see what the server default is when the field is absent. But
it is consistent with everything observed — eight reports written, committed, pushed, and apparently never
read. Frank can settle it in 30 seconds by saying whether he has ever received a phone or email
notification from this routine. If the answer is no, that single setting explains the entire backlog, and
fixing it is worth more than every SEO recommendation in the last eight reports combined.

**No new opportunities are proposed this week — deliberately.** Section 6 re-states nothing and adds
nothing. The one exception is the deadline item below, which was raised last week and now has 10 days on
the clock.

---

## 4. Site health table

**Cannot be populated — eighth week.** A guessed "Y" in a form-present column would be worse than no
report. The 15-row manual checklist is in `2026-09-14-weekly-review.md` §4 and is unchanged; rows 11–13
(`/capsule-manufacturing/`, `/protein-powder-manufacturing/`, `/dietary-supplement/`, `/faq/`,
`/service-area/`, `/testimonials/`) have still never been inspected by this routine because they are not in
its hardcoded URL list.

**Performance:** no data, eighth week. No baseline exists.

The only live signal available is the search index, which at least confirms the domain is up and crawled —
10 URLs returned today: `/`, `/contact/`, `/blog/`, `/faq/`, `/testimonials/`, `/service-area/`,
`/capsule-manufacturing/`, `/liquid-supplement-manufacturing/`, `/private-label-supplement-manufacturer/`,
`/gummy-manufacturing/`, plus the stock-greens PDF. Titles look intact and on-pattern (see §2 for the one
exception). This is not a substitute for an HTML check — an indexed page with a silently removed
`gform_3` looks identical from here.

---

## 5. Content cadence

**Behind, and the mechanism is the problem — not the content.**

- **August 2026: 0 published** against a target of 2. Month closed.
- **September 2026 to date: 0 published.** 9 days left; will close the same way without CMS access.
- **48 days since anything went live.** Both overdue posts are written and sitting unpublished.

Writing a third and fourth post before the publish mechanism is fixed only deepens the backlog.

---

## 6. This week's recommended actions

Four items, ranked. Impact ordering is a **hypothesis** — there is no GA4 or Search Console data behind it.

| # | Action | Effort | Expected impact |
|---|---|---|---|
| **1** | **Answer one question: have you ever received a notification from this routine?** If no, set push/email on `trig_017aWfw6fz4pdzSCwhQQ8d4a`. | 30 sec to answer | Plausibly the root cause of 8 weeks of zero execution. Nothing else in this report matters if the reports aren't reaching you |
| **2** | **Decide the routine's fate**, then say which: (a) swap in the `ROUTINE-PROMPT.md` prompt — I can do it in one `update_trigger` call, no UI needed; (b) pause the routine until site access exists; or (c) keep it as-is. Also decide the monitoring question: add `paramountnutra.com` + `www.` to this environment's allowed hosts (~5 min, restores sections 2–4 immediately), or stand up an external keyword monitor on `gform_3` and formally descope health checks from this routine. | 5 min decision | Stops the appearance of monitoring. 56 days of unmonitored lead capture is an invisible-revenue risk of unbounded size |
| **3** | **Open WordPress → Posts → Scheduled and publish the two written August posts.** Then find out why cron didn't fire (WP-Cron disabled, no host cron, or a plugin conflict). | 15 min | Two finished assets earning nothing; unblocks all future cadence |
| **4** | **The FDA biennial renewal window opens Oct 1 — 10 days.** Re-verified today: window is 12:01 AM Oct 1 → 11:59 PM Dec 31 2026, no fee, and a registration not renewed is **expired, not paused** (resuming shipments needs a full new registration). Still owned entirely by filing agents (Registrar Corp, Orionex, Axentra, FDAHelp, QualitySmart) writing for the *facility* — nobody is writing for the **brand owner** asking "my product is made at someone else's facility, am I exposed if their registration lapses, and how do I check?" Gated on action 3: pointless to write if publishing is broken. Must state plainly that FDA registration ≠ FDA approval. | 3–4 hrs | Only deadline-bound item on the list. Catches the whole Oct–Dec window if published late September; dead for 22 months if missed |

Everything else — MOQ numbers, NSF page, stick-pack/powder page, creatine page, tariff post, GLP-1,
`/service-area/` and Google Business Profile audit, adding the six unmonitored URLs — is unchanged in
prior reports and is not re-listed here. The NSF question remains the worst offender: 30 minutes of
internal time, unanswered for six weeks, blocking three separate items.

---

## 7. Data the human needs to pull

Unchanged from last week in substance; the three that matter most, in order:

1. **GA4 — is `generate_lead` still firing at all in the last 7 days?** A zero is a P0 and confirms the
   worst reading of section 2. This is the single most important number available.
2. **GA4 — `generate_lead` count by month for the last four months.** A step change around late July
   would mean the form broke *during* the blind period, which is exactly what this routine existed to
   catch and has not been able to since.
3. **Search Console — Coverage/Pages: are `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` known to
   Google at all?** "Discovered, not indexed" / "Excluded" / entirely absent. Absent confirms they never
   published; anything else means they published and something else broke.

Then, lower priority: form conversion rate per landing page (a money page with traffic and zero
conversions is a broken-form candidate); impressions and average position for `/capsule-manufacturing/`,
`/protein-powder-manufacturing/` and `/service-area/`, none of which have ever been assessed here; whether
`/contact/` and `/testimonials/` draw impressions on "dietary supplement manufacturer/company" queries,
which would turn §2's near-duplicate titles from cosmetic into real cannibalization; and any existing
impressions on FDA-registration or cGMP terms, which would size action 4 before the work is done.

**And one 30-second WordPress check:** on **Posts → Scheduled**, do the two posts show as *Missed
schedule*? That screen alone resolves the P1 and tells you whether September's posts will fail the same way.
