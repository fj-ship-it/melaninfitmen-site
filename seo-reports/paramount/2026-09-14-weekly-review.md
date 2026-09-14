# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-09-14
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-09-07-weekly-review.md`

---

## 1. Bottom line

Seventh consecutive week with no ability to reach the site: lead capture is **49 days unverified**, and
both August posts are still unpublished (**41 and 27 days overdue**, zero posts live in 41 days). Last
week's report said it was the last week worth carrying the block as an open item, so this week it stops
being a finding and becomes a decision: **either widen the egress allowlist, or formally descope the
health checks to an external monitor** — section 6, action 0.

Everything below section 4 still works, and the strongest new opportunity in several weeks has a
deadline attached: the **FDA biennial facility registration window opens October 1** (17 days), and no
contract manufacturer is targeting the brand-owner side of that query.

---

## 2. P0 / P1 issues

### P0 — Seventh week blind. Lead capture UNVERIFIED for 49 days.

Re-confirmed today on both channels:

```
kind:   connect_rejected
detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
host:   paramountnutra.com:443
ts:     2026-09-14T11:12:12Z
```

- `curl` fails at the CONNECT tunnel (exit 56, HTTP 000). `WebFetch` returns
  `{"error_type":"EGRESS_BLOCKED","domain":"paramountnutra.com"}`. `www.paramountnutra.com` identical.
- Controls re-run today: `api.github.com` → **200**, `registry.npmjs.org` → **200**; `example.com` and
  `www.google.com` → **blocked**. Unchanged for four weeks. This is a developer-infrastructure-only
  allowlist — not a site outage, not the known 406/User-Agent quirk, not a block aimed at this domain.
- `/root/.ccr/README.md` is explicit that 403 policy denials are reported, not retried or routed
  around. No workaround attempted.

**Nothing in this report is evidence that any form, PDF, or analytics tag currently works.** Seven
weeks is comfortably long enough for a Gravity Forms or WordPress auto-update to have silently broken
`gform_3` on all fifteen monitored URLs with nobody noticing. That is the entire risk this routine
exists to catch, and it has not been covered since late July.

**This is now a decision, not a finding.** See section 6, action 0. Continuing to emit a weekly
"NOT VERIFIED" table is the appearance of monitoring, which is worse than none, because it reads like
coverage in the file tree.

### P1 — Publish mechanism still broken. Zero posts in 41 days.

| Post | Due | Days overdue | Index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **41** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **27** | none |

Re-checked today with topic and exact-phrase searches. The domain indexes normally — a `site:` query
returns the homepage, `/testimonials/`, `/service-area/`, `/contact/`, `/capsule-manufacturing/`,
`/blog/`, `/private-label-supplement-manufacturer/`, `/liquid-supplement-manufacturing/` and the
stock-greens PDF — but **neither post appears**, seven weeks running.

Treat "missed schedule / WP-Cron not firing" as confirmed until someone opens the WordPress **Posts →
Scheduled** screen and proves otherwise. September's two posts will miss the same way. This is the
cheapest problem in the report to fix and the most wasteful to leave alone.

### P1 (suspected, carried, still unverified) — duplicate title regression

`/contact/` still carries **"Dietary Supplement Company | North America – Paramount Nutra"** in the
index, near-identical to `/dietary-supplement/`'s **"Dietary Supplement Company | North America"**.
Re-confirmed in today's `site:` results. Title cannibalization was a previously *fixed* problem here.
Confirm against live HTML before editing — index titles lag.

---

## 3. Changed since last week

**The block was not fixed. Seventh week.** Section 4 and the performance check are empty again. Seven
weeks of trend data are permanently unrecoverable, and the performance baseline that every future
week-over-week comparison depends on still does not exist.

**Cadence gap widened 34 → 41 days.** September is now two weeks from closing with the same outcome as
August unless someone touches the CMS.

**New — the local competitive set is far denser than these reports have recorded.** Prior weeks named
Bactolac (Hauppauge) as "the nearest large local competitor." Today's search surfaced at least six
Long Island / metro-NY contract manufacturers: **Emerald Nutraceuticals**, **Brand International**
(25+ yrs, LI facility), **Cavendish Nutrition**, **Vitamix Laboratories** (Commack), **Advanced
Supplements** (60,000 sq ft, LI, "trusted by 1,650+ brands") and **Bactolac**. Paramount has a
`/service-area/` page; it is competing in one of the densest supplement-manufacturing geographies in
the country and the reports have been treating local as a soft flank. See 5d.

**New — the MOQ gap is now a seven-week-old carried recommendation and the field has filled in
further.** Beyond Aurinutra's ranking guide, this week surfaced **NutriCraft** marketing a dedicated
*"Low MOQ Supplement Manufacturer | 1000-Unit Minimum"* service page, **build-your-own-brand.com** on
*"500 MOQ, 4-Week Ship [2026]"*, plus Matsun, SummitRx, CSK Biotech, Sun Nutraceuticals, HDNutra and
Atrium Scientific all holding MOQ-query real estate. A direct search for Paramount + MOQ confirms it:
**Paramount still publishes no number anywhere**, and the search engine's own summary of the site says
so in as many words ("the search results don't contain specific MOQ requirements"). Competitors are
being quoted with numbers; Paramount is being quoted as "contact them."

**New — format data cuts against the gummy-first emphasis.** Powders are the fastest-growing format
(**9.6% CAGR** 2025–2033; ~10.4%/yr in Europe on protein and greens). Gummies are still growing in
absolute terms (~$27B 2025 → ~$42B 2030), but at least one industry source reports US gummy dollar
sales **down 8% YoY** against capsules **up 5.3%**. These two readings are not necessarily in
conflict — global forecast vs. US retail dollar movement — but they are worth reconciling before more
budget goes behind gummy content. See 5c.

**Carried and still undone, seventh week:** `/capsule-manufacturing/` and
`/protein-powder-manufacturing/` remain **never once checked** for a lead form. Both are live money
pages ranking for commercial queries, and both are absent from this routine's hardcoded URL list.

---

## 4. Site health table

**Cannot be populated — seventh week.** A guessed "Y" in a form-present column is worse than no report.

Below is the fifteen-minute manual pass. Every row is unverified as of today.

| # | URL / check | Look for | Status |
|---|---|---|---|
| 1 | `/gummy-manufacturing/` | `gform_3` | NOT VERIFIED (49 days) |
| 2 | `/private-label-supplement-manufacturer/` | `gform_3` | NOT VERIFIED (49 days) |
| 3 | `/liquid-supplement-manufacturing/` | `gform_3` | NOT VERIFIED (49 days) |
| 4 | `/tablet-manufacturing/` | `gform_3` | NOT VERIFIED (49 days) |
| 5 | `/stock-formulations/` | `gform_3` | NOT VERIFIED (49 days) |
| 6 | 10 monitored blog posts | `gform_3` | NOT VERIFIED (49 days) |
| 7 | `/contact/` | `gform_wrapper` (quote form) | NOT VERIFIED (49 days) |
| 8 | `Supplement-Launch-Guide-2026.pdf` | HTTP 200 | NOT VERIFIED (49 days) |
| 9 | Homepage | `generate_lead` ×1, `G-XK72PDD5T8` | NOT VERIFIED (49 days) |
| 10 | Homepage | `Made in cGMP-Certified`, `What Our Clients Say` | NOT VERIFIED (49 days) |
| 11 | **`/capsule-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 12 | **`/protein-powder-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 13 | `/dietary-supplement/`, `/faq/`, `/service-area/`, `/testimonials/` | `gform_3`, title dupes | NOT VERIFIED (ever) |
| 14 | Full sitemap crawl | status, redirects, titles, metas | NOT VERIFIED (49 days) |
| 15 | Homepage + one money page | response time, transfer size | **NO BASELINE EXISTS** |

Rows 11–13 first if time is short — live pages, ranking for commercial queries, that this routine has
never inspected because they are not in its list. Add all of them to the monitored set regardless of
outcome.

**Performance (brief section 4):** no data, seventh week. No payload or response-time delta can be
computed, and none can be computed in future until a first measurement exists.

---

## 5. Content cadence

**Verdict: behind, and the mechanism — not the content — is the problem.**

- **August 2026: zero published posts** against a target of two. Month closed.
- **September 2026 to date: zero.** Both August posts remain unpublished.
- **41 days since anything went live** (index inference; `post-sitemap.xml` is behind the block).
- Both scheduled posts are **written**. Neither is live.

**Writing more posts before the publish mechanism is fixed adds nothing** — it deepens the backlog. The
one exception is section 5a, which is deadline-bound and worth queueing now so it is ready the moment
publishing works.

---

## 6. Opportunity analysis

Carried items are summarised in 5e without re-argument. New material first.

### 5a — NEW, strongest idea this week: the FDA biennial registration renewal window (opens Oct 1)

**The fact.** FDA requires every domestic and foreign facility that manufactures, processes, packs or
holds dietary supplements for the US market to renew its food facility registration **every even
year, between October 1 and December 31**. 2026 is an even year. The window opens in **17 days**.
Renewals cannot be filed before Oct 1, and a registration not renewed by Dec 31 is treated as
**expired, not paused** — resuming shipments then requires a full new registration.

**Why this is a contract manufacturer's query and not a consultant's.** The queries here are currently
owned entirely by regulatory-filing services (Registrar Corp, Orionex, Axentra, FDAPals, FDAHelp). All
of them write for the *facility* that must file. Nobody is writing for the **brand owner**, whose
actual question is different and more anxious: *"my product is made at someone else's facility — am I
exposed if they let their registration lapse, and how do I check?"*

That question has a perfect answer for Paramount specifically, and it doubles as a trust asset:
Paramount's own partner facilities are FDA-registered and cGMP-certified, the site already says so, and
this is the one week of the two-year cycle when a founder is actively looking for that reassurance.

**The page writes itself:** what the biennial renewal is; the exact dates and the expired-not-paused
consequence; why a brand owner's own registration obligations differ from their manufacturer's; how to
verify a manufacturer's registration status before signing; what to ask a prospective manufacturer in
writing; and a closing CTA into the quote form. Add FAQ schema on the five questions.

**Timing is the whole point.** This is a seasonal query with a hard two-year cycle. Published in late
September it catches the entire Oct–Dec window; published in January it is dead for twenty-two months.
It is also the rare piece that is genuinely useful, genuinely evergreen-with-a-refresh, and requires no
internal decision to be made first — unlike the MOQ and NSF items, which have been gated for weeks.

**Keyword cluster:** *FDA facility registration renewal 2026*, *supplement manufacturer FDA registered
verify*, *dietary supplement facility registration brand owner*, *FDA registration expired supplement*,
*is my supplement manufacturer FDA registered*.

**Caveat to respect:** FDA registration is **not** FDA approval, and the page must say so plainly.
Implying approval is a recognised compliance trap and would undercut the trust the page is built to
earn.

### 5b — NEW: creatine, and the technical-authority angle nobody local is using

Creatine is one of the strongest categories going into 2026, and the interesting part for a
manufacturer is that **the format race is open and technically hard**: gummies, stick packs, flavoured
powders and RTDs are all being attempted, but **creatine degrades in solution** and gummy/chewable
formats are inherently less stable than powder. Trade coverage is explicit that liquid and chewable
creatine formats "need real data behind the label."

That is a manufacturing problem, not a marketing problem, which makes it defensible content for a
contract manufacturer and nearly impossible for a brand-side blog to write credibly. A page on *what it
actually takes to manufacture stable creatine in each format* — degradation to creatinine, pH and
moisture control, overage and stability testing, which formats Paramount will and will not attempt —
qualifies serious founders and disqualifies the ones who want a liquid creatine gummy at 1,000 units.

Pairs naturally with the existing `/protein-powder-manufacturing/` page and gives it an internal link
it currently lacks.

**Keyword cluster:** *creatine manufacturer private label*, *creatine gummy manufacturing*, *creatine
stability powder*, *contract manufacturer creatine monohydrate*, *creatine stick pack manufacturer*.

### 5c — NEW: stick packs and powders — the format Paramount under-sells

Powders are the **fastest-growing format** (9.6% CAGR forecast 2025–2033; ~10.4%/yr in Europe), and
stick packs / single-dose sachets are the packaging story riding it. Paramount **does** offer both —
single-dose packets appear in its packaging copy, and `/protein-powder-manufacturing/` exists — but
there is **no stick-pack page**, and the powder capability is buried relative to gummy and capsule.

Competitors have noticed: Nutra Connection runs a dedicated *Stick Pack Manufacturing* page and a
separate *Large-Scale Powder Manufacturing* page; Brand Nutra runs a stick-packs packaging page;
Intermountain runs a powders service page. This is a capability Paramount has and does not rank for,
which is the cheapest kind of gap to close — no new capability, no internal decision, just a page.

This also bears on the gummy emphasis. Before more budget goes into gummy content, reconcile the two
readings in section 3: global gummy market up, US gummy dollar sales reportedly down 8% YoY with
capsules up 5.3%. If the US retail figure holds, the format mix on the site is tilted toward the
softening format and away from the growing one.

**Keyword cluster:** *stick pack manufacturer supplement*, *single serve powder manufacturer*, *private
label stick packs*, *supplement powder contract manufacturer*, *sachet filling supplement*.

### 5d — NEW: the local flank is much more crowded than assumed

Six-plus Long Island / metro-NY contract manufacturers surfaced today (list in section 3), several with
scale claims Paramount does not make publicly (Advanced Supplements: 60,000 sq ft, "1,650+ brands").
Paramount has `/service-area/` but the reports have never audited what it actually targets or whether
it ranks.

Two cheap moves, both dependent on the block being lifted before they can be scoped properly:

1. Audit `/service-area/` for genuine local intent — does it name Stony Brook, Suffolk County, Long
   Island, the NY metro, and does it carry a lead form? (It is not in the monitored list; see row 13.)
2. Verify the Google Business Profile is claimed, categorised as a manufacturer, and consistent in
   NAP with the site footer. Local pack presence for "supplement manufacturer near me" in this
   geography is contested by a half-dozen established firms; a stale or unclaimed profile forfeits it.

Lower priority than 5a–5c because it cannot be scoped without site access, but flagged so it stops
being invisible.

### 5e — Carried opportunities, unchanged in substance

| Item | First raised | Status | Gate |
|---|---|---|---|
| **Publish the MOQ number** (per-format ranges) | early Aug | **7 weeks carried**, field filling in fast (5e above) | one internal decision: smallest run Paramount will quote, per format |
| **NSF / Certified-for-Sport page** | ~4 wks ago | **5 weeks carried**; Bactolac already ranks locally | 30-min internal question: does any partner facility hold it? Gates three separate items |
| **Tariff / ingredient-sourcing post** | Aug | writable now — 10% reciprocal tariff holds to ≥Nov 2026, Annex III nutraceutical exclusions active, imported costs +10–40% | none; avoid unqualified "Made in USA" (FTC "all or virtually all") |
| **GLP-1 companion formulations** | Aug | live window; blood-sugar positioning = 39.3% of the GLP-1 support segment; fiber, berberine, probiotics, chromium | none |

The NSF question is the worst offender: **30 minutes of internal time, unanswered for five weeks,
blocking three opportunities.**

---

## 7. This week's recommended actions

Ranked by likely lead impact ÷ effort. Action 0 is not an SEO action and outranks everything.

| # | Action | Effort | Expected impact |
|---|---|---|---|
| **0** | **Decide the monitoring question.** Either (a) add `paramountnutra.com` + `www.` to this environment's allowed hosts — ~5 min, restores sections 1–4 immediately — or (b) if policy forbids it, stand up an external uptime monitor with keyword matching on `gform_3` across the 15 URLs and **formally descope health checks from this routine**, leaving it as the research routine it can still do. | 5 min (a) / ~1 hr (b) | Restores the routine's primary function. Currently 49 days of unmonitored lead capture — an invisible-revenue risk of unbounded size |
| **1** | **Open WordPress → Posts → Scheduled. Publish the two written August posts.** Then check why cron did not fire (WP-Cron disabled, host-level cron missing, or a plugin conflict). | 15 min | Two finished assets currently earning nothing; unblocks all future cadence |
| **2** | **Write and queue the FDA renewal-window post (5a)** so it publishes in the last week of September. | 3–4 hrs | High-intent, deadline-bound, zero competition from manufacturers, doubles as a trust asset. Dead for 22 months if missed |
| **3** | **Answer the NSF question** (yes/no, which facility, current certificate). | 30 min | Unblocks three carried opportunities; also bounds certification language sitewide |
| **4** | **Decide the MOQ numbers and publish the page (5e).** | 1 hr decision + 3 hrs page | Highest-volume high-intent query in the category; 7 weeks unbuilt; competitors now ranking with numbers |
| **5** | **Build the stick-pack / powder page (5c)** and cross-link `/protein-powder-manufacturing/`. | 3 hrs | Existing capability, fastest-growing format, no internal decision needed |
| **6** | **Add rows 11–13 to the monitored URL list** (`/capsule-manufacturing/`, `/protein-powder-manufacturing/`, `/dietary-supplement/`, `/faq/`, `/service-area/`, `/testimonials/`). | 10 min | Closes a blind spot that predates the egress block |
| **7** | **Creatine manufacturing page (5b).** | 4 hrs | Defensible technical authority; strong qualifying/disqualifying effect |
| **8** | **Confirm/fix the `/contact/` vs `/dietary-supplement/` title duplication** once site access returns. | 20 min | Prevents regression of a previously fixed problem |

---

## 8. Data the human needs to pull

Specific questions, not general advice. GA4 and Search Console are both outside this routine's reach.

**Search Console — Performance, last 90 days vs. prior 90:**

1. Which queries **gained and lost** impressions and clicks? Specifically: did anything move on
   *low MOQ*, *minimum order quantity*, or *cost to manufacture* queries, given competitors published
   into that gap while Paramount published nothing for 41 days?
2. Does `/contact/` receive impressions for **"dietary supplement company"**-type queries — i.e. is the
   suspected title duplication with `/dietary-supplement/` actually splitting impressions, or is it
   cosmetic?
3. What are the **impressions and average position** for `/capsule-manufacturing/`,
   `/protein-powder-manufacturing/` and `/service-area/`? These three have never been assessed here.
4. Any queries already arriving on **FDA registration** or **cGMP** terms? That would size 5a before
   the work is done.
5. **Coverage / Pages report:** are `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` known to
   Google at all — "Discovered, not indexed," "Excluded," or entirely absent? Absent confirms they
   never published; anything else means they published and something else went wrong.

**GA4 — same comparison window:**

6. What is the **`generate_lead` conversion count by month** for the last four months? A step change
   around late July would indicate the form broke *during* the blind period — this is the single most
   important number in the list.
7. What is the **form conversion rate per landing page**? Which of the five money pages actually
   produce guide downloads, and which produce none? A money page with traffic and zero conversions is
   a broken-form candidate.
8. **Which pages produced the leads** that became quote requests? Blog-sourced vs. money-page-sourced
   determines where action 2's follow-on effort should go.
9. Is the **`generate_lead` event still firing at all** in the last 7 days? A zero here is a P0 and
   confirms the worst reading of section 2.
10. **Landing-page traffic for the two unpublished posts' target topics** — if organic demand for
    gummy-vs-capsule and cGMP queries is already reaching the homepage (as noted last week), the posts
    have a warm start when they finally publish.

**One WordPress question (30 seconds, no analytics needed):**

11. On **Posts → Scheduled**, do `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` show as
    *Missed schedule*? That single screen resolves the P1 in section 2 and determines whether
    September's posts will fail the same way.
