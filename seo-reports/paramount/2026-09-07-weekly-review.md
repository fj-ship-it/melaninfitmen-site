# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-09-07
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-08-31-weekly-review.md`

---

## 1. Bottom line

**Sixth consecutive week blind.** Lead capture has now gone **42 days** unverified, and the two posts
written for August are **34 and 20 days overdue** with still no index trace. The single highest-value
action is unchanged and is now overdue past the point where re-reporting it is useful: either widen the
egress allowlist (five minutes) or accept that this routine cannot do its primary job and replace the
health checks with an external monitor — **pick one this week**.

---

## 2. P0 / P1 issues

### P0 — Monitoring blind for a sixth week. Lead capture UNVERIFIED for 42 days.

Re-confirmed today on both channels, unchanged:

```
kind:   connect_rejected
detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
host:   paramountnutra.com:443
```

- `curl` fails at the CONNECT tunnel (exit 56, HTTP 000). `WebFetch` returns
  `{"error_type":"EGRESS_BLOCKED","domain":"paramountnutra.com"}`. `www.paramountnutra.com` fails
  identically.
- Control tests re-run today: `api.github.com` → 200, `registry.npmjs.org` → 200; `example.com` and
  `www.google.com` → **blocked**. Same result as the last three weeks. This is a narrow allowlist
  covering developer infrastructure only, not a site outage, not the known 406/User-Agent quirk, and
  not a block aimed at paramountnutra.com specifically.
- `/root/.ccr/README.md` is explicit that 403/407 policy denials are reported, not retried or routed
  around. No workaround was attempted.

**Six weeks is long enough for a Gravity Forms or WordPress auto-update to have silently broken the
guide-download form on all fifteen monitored URLs with nobody noticing.** Nothing in this report is
evidence that any form, PDF, or analytics tag currently works.

**Fix:** add `paramountnutra.com` and `www.paramountnutra.com` to this environment's allowed hosts
(https://code.claude.com/docs/en/claude-code-on-the-web covers the network-policy options), then
re-run the routine.

**Escalation — this is the last week it is worth writing this item as "carried."** It has been #1 for
six consecutive weeks with no change. Two honest options remain, and the choice is a business decision,
not a technical one:

1. Widen the allowlist. Five minutes, restores everything.
2. If policy forbids it, **stand up an external form/uptime monitor** (any scheduled service that can
   reach the public web — an uptime checker with keyword matching on `gform_3`, or a weekly manual
   fifteen-minute pass through section 4's table) and formally drop sections 1–4 from this routine's
   scope, leaving it as a research-and-opportunity routine, which is the part it *can* still do.

Continuing to generate a weekly "unverified" table is not monitoring. It is the appearance of
monitoring, which is worse than none, because it reads like coverage.

### P1 — publish mechanism still broken. Zero posts in 34 days.

| Post | Due | Days overdue | Index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **34** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **20** | none |

Re-checked today with a slug/topic search and a `site:paramountnutra.com` query. The `site:` query
returns the homepage, `/testimonials/`, `/contact/`, `/capsule-manufacturing/`, `/blog/` and the
stock-greens PDF — the domain is crawlable and indexing normally — but **neither post appears**.

One notable detail this week: a search for the gummy-vs-capsule topic surfaced Paramount's **homepage**
with copy comparing capsules, tablets and gummies. The comparison content exists on the site; it is
just sitting on the homepage where it ranks for nothing, instead of on a post targeting the query. That
strengthens the case for publishing `/gummy-vs-capsule/` rather than weakening it.

Treat "missed schedule / WP-Cron not firing" as confirmed until someone opens the WordPress Posts
screen and proves otherwise. **September's posts will miss the same way unless cron is fixed.**

### P1 (suspected, carried forward, still unverified) — duplicate title regression

`/contact/` still carries **"Dietary Supplement Company | North America – Paramount Nutra"** in the
index, near-identical to `/dietary-supplement/`'s **"Dietary Supplement Company | North America"**.
Re-confirmed in today's `site:` results. Title cannibalization was a previously *fixed* problem on this
site. Confirm against live HTML before editing.

---

## 3. Changed since last week

**The block was not fixed. Sixth week.** Sections 4 and the performance check are empty again. Six
weeks of trend data are permanently unrecoverable, and the baseline every future week-over-week
comparison depends on still does not exist.

**September has started the same way August ended** — nothing published, both August posts still in the
CMS. The cadence gap is now 34 days.

**Competitor movement — Aurinutra has extended from geo into the MOQ query.** Last week's finding was
that Aurinutra publishes the NY geo-listicle and ranks itself first on it. This week it also holds a
top result for **"Low MOQ in Supplement Manufacturing: 2026 Complete Guide."** That is the single
highest-volume high-intent query in this category — the one flagged as unbuilt in every report since
early August — and a competitor that did not exist in these reports a month ago now ranks for both it
*and* Paramount's home state. Aurinutra is executing a content strategy; Paramount published nothing
in the same period.

**New — Bactolac (Hauppauge, NY) has a dedicated NSF-Certified sports supplement manufacturer page.**
The nearest large local competitor is targeting a certification-led query segment. See 5b.

**New — the low-MOQ numbers are now public and specific enough to price against.** Published 2026
figures: capsules 5,000–25,000 units, gummies 10,000–50,000, oral dissolving films from 3,000; startup
first runs 500–1,500 units at roughly $5,000–$10,000 all-in. Matsun markets 2,500; at least one
competitor markets 500/SKU. **Paramount publishes no number anywhere.** The decision this gates is now
much easier to make, because the range Paramount would be judged against is on the record.

**New — tariff picture firmed up.** The 10% reciprocal tariff holds through at least November 2026, and
Annex III exclusions covering many nutraceutical and functional-food ingredients are **now active**.
Imported ingredient costs run 10–40% above baseline depending on origin. The exclusions matter: they
turn a vague "tariffs are bad" post into a specific, useful one. See 5c.

**Carried and still undone:** `/capsule-manufacturing/` and `/protein-powder-manufacturing/` remain
**never once checked** for a lead form — sixth week flagged, still a two-page-load task.

---

## 4. Site health table

**Cannot be populated — sixth week.** A guessed "Y" in a form-present column is worse than no report.

The checklist below is what a human can work through in about fifteen minutes. Every row is unverified
as of today.

| # | URL / check | Look for | Status |
|---|---|---|---|
| 1 | `/gummy-manufacturing/` | `gform_3` | NOT VERIFIED (42 days) |
| 2 | `/private-label-supplement-manufacturer/` | `gform_3` | NOT VERIFIED (42 days) |
| 3 | `/liquid-supplement-manufacturing/` | `gform_3` | NOT VERIFIED (42 days) |
| 4 | `/tablet-manufacturing/` | `gform_3` | NOT VERIFIED (42 days) |
| 5 | `/stock-formulations/` | `gform_3` | NOT VERIFIED (42 days) |
| 6 | 10 monitored blog posts | `gform_3` | NOT VERIFIED (42 days) |
| 7 | `/contact/` | `gform_wrapper` (quote form) | NOT VERIFIED (42 days) |
| 8 | `Supplement-Launch-Guide-2026.pdf` | HTTP 200 | NOT VERIFIED (42 days) |
| 9 | Homepage | `generate_lead` ×1, `G-XK72PDD5T8` | NOT VERIFIED (42 days) |
| 10 | Homepage | `Made in cGMP-Certified`, `What Our Clients Say` | NOT VERIFIED (42 days) |
| 11 | **`/capsule-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 12 | **`/protein-powder-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 13 | Full sitemap crawl | status, redirects, titles, metas | NOT VERIFIED (42 days) |
| 14 | Homepage + one money page | response time, transfer size | NO BASELINE EXISTS |

Rows 11 and 12 first if time is short — live money pages ranking for commercial queries that this
routine has never inspected, because they are not in its hardcoded list. Add them to the monitored list
regardless of outcome.

**Performance (section 4 of the brief):** no data, sixth week. No payload or response-time deltas can
be computed, and none can be computed in future either until a first measurement exists.

---

## 5. Content cadence

**Verdict: behind. The mechanism, not the content, is the problem.**

- **August 2026: zero published posts** against a target of two. Month closed.
- **September 2026 to date: zero.** Both August posts remain unpublished.
- **34 days since anything went live** (inferred; `post-sitemap.xml` is behind the egress block, so
  this section is index inference rather than measurement).

Both scheduled posts are written. Neither is live. This remains the cheapest problem in the report to
fix and the most wasteful to leave alone. **Writing more posts before the publish mechanism is fixed
adds nothing** — it just deepens the backlog.

---

## 6. Opportunity analysis

Prior weeks' opportunities are carried in 6e/6f below without re-argument. New material first.

### 5a / 6a — NEW, and the strongest new idea this week: publish the MOQ number as a page, now

This has been on the list since early August as "gated on a business decision." That gate is now much
cheaper to clear, for three reasons that all landed this week:

1. **The benchmark is public.** 2026 published figures: capsules 5,000–25,000 units; gummies
   10,000–50,000; ODF from 3,000; startup first runs 500–1,500 units at $5,000–$10,000 all-in. Matsun
   markets 2,500 units; at least one competitor markets 500/SKU.
2. **A competitor now ranks for the query with Paramount's own positioning available to it.** Aurinutra
   holds a top result for "Low MOQ in Supplement Manufacturing: 2026 Complete Guide," having published
   it in the window during which Paramount published nothing.
3. **The trade press has named the buying criterion explicitly.** 2026 coverage frames founders as
   facing three simultaneous pressures — *keep initial inventory lean, prove GMP compliance, get to
   market fast* — and calls flexible MOQs "a competitive baseline." Paramount's six-facility network is
   a genuine structural advantage on exactly that axis, and it is invisible.

**The decision to make is narrow, not open-ended:** what is the smallest run Paramount will actually
quote, per format? That is one internal conversation. Publishing a range with conditions ("capsules
from X; gummies from Y; stock formulations from Z") beats publishing nothing, and beats a vague
"flexible MOQs" line, which is what every competitor without a real answer writes.

**Why this outranks the marketplace-documentation page (6b) on impact ÷ effort:** it is a shorter page,
it targets a higher-volume query, the competitive urgency is now demonstrated rather than predicted,
and it requires no certification research to write safely.

**Keyword cluster:** *low MOQ supplement manufacturer*, *supplement manufacturer minimum order
quantity*, *small batch supplement manufacturing*, *supplement manufacturer 1000 units*, *low MOQ gummy
manufacturer*.

### 5b / 6b — NEW: the certification-tier page, and a local competitor already moved

**What happened.** Bactolac (Hauppauge, NY — fifteen minutes from Stony Brook) publishes a dedicated
**NSF-Certified sports supplement manufacturer** page. GMP Labs markets its NSF Certified for Sport
status as a headline credential. This is a competitor segmenting by certification tier, and it works
because for one specific buyer the certification *is* the buying criterion.

**Why it is high-intent.** A brand selling into professional or collegiate sport, or into any retailer
that requires banned-substance testing, cannot use a manufacturer without the certification. There is
no persuasion step. The searcher is filtering, not browsing, and the query converts or disqualifies
immediately — which is exactly what a contract manufacturer wants, because a disqualified lead costs
nothing and a qualified one is nearly closed.

**The requirements, concretely** (useful for the page, and for deciding whether to pursue it):
facility must hold **NSF GMP certification** and pass audits; product tested against a panel of
**280+ banned substances**; label-contents confirmation; supplier and facility inspection; annual
compliance re-testing with facility audits annually or biannually by risk grade.

**This is gated on the same unanswered internal question as 6d, and that is the point.** The
certification question has now been open for four weeks and gates *three* separate opportunities
(6b marketplace docs, this, and the cGMP post retargeting). It is a 30-minute internal question with
compounding cost. **Answer it this week.**

- If a partner facility holds NSF/Certified for Sport → build the sports-nutrition certification page.
  It is a defensible, low-competition, high-intent segment where a named local competitor is already
  earning leads.
- If not → do not write the page, and scope all certification language on the site to what is actually
  documented. Overclaiming here generates leads that die at diligence, which is worse than no leads.

### 5c / 6c — NEW: the tariff post is now writable, because the exclusions are active

Prior reports listed a tariff post as "medium, verify rates with a broker." Two facts moved it up:

- The **10% reciprocal tariff holds through at least November 2026** — a stable planning horizon, not a
  moving target.
- **Annex III exclusions covering many nutraceutical, functional-food and superfood ingredients are now
  active.** Imported ingredient costs otherwise run **10–40%** above baseline depending on origin
  (Chinese vitamin C and Indian botanicals cited as the sharpest).

**Why this is a manufacturer's post and not a trade-press rehash:** the founder's actual question is
*"is my formula affected, and what would it cost me to reformulate or re-source?"* A manufacturer can
answer that per ingredient. A consultant cannot. The post writes itself as: which common supplement
ingredient categories are excluded, which are exposed, what the realistic alternatives are (India,
Vietnam, Brazil — with the honest caveat that capacity and consistency vary), and what a re-sourcing
decision actually costs in reformulation and re-testing.

**Caution, unchanged:** do not make an unqualified "Made in USA" claim. The FTC standard is
"all or virtually all," and it is enforced.

**Keyword cluster:** *supplement ingredient tariffs 2026*, *supplement manufacturing costs tariffs*,
*domestic supplement ingredient sourcing*, *supplement tariff exclusions*.

### 5d — NEW context, no action: AI search does not need a separate strategy here

Worth stating once so it does not get sold to Paramount as a project. A 2026 study of 116 US supplement
sites found **97% already appear in AI Overviews or ChatGPT results**, and the finding was that brands
ranking organically already show up — a separate "AI strategy" is not required. ChatGPT leans ~77% on
**editorial** sources for supplement recommendations, with minimal reliance on brand-owned content.

Two implications, both of which point back at things already on this list:

1. **Do not buy an "AEO/GEO" engagement.** The lever is ordinary organic ranking plus structured data,
   which is what sections 6e/6f already recommend.
2. **The editorial-source finding reinforces the directory/listicle action (#4).** If AI answers lean on
   third-party editorial, then being absent from every "top supplement manufacturers" list is not just
   an organic-traffic problem — it is why Paramount would be absent from an AI answer to *"who should
   manufacture my supplement?"* That is the same fix, with a second reason to do it.

Note the study is about consumer supplement *brands*, not B2B manufacturers, so treat the 97% figure as
directional for this site rather than a measurement of it.

### 6d — Carried, and now gating three items: the certificate question

Unchanged, four weeks open, and the highest-leverage 30 minutes available to anyone at Paramount:

> **Do any of Paramount's six partner facilities hold a current certificate from BSCG, Clean Label
> Project, GRMA, Informed Choice, NSF, NSF Certified for Sport, or USP?**

Gates 5b (sports certification page), 6b (marketplace-documentation page), and the retargeting of
`/what-cgmp-actually-means/`. If no, scope claims to facilities qualifying under the broader accepted
schemes (NSF/ANSI 455-2, NSF 173 §8, GRMA 455-2, UL, USP, SGS, Intertek, SQF, Eurofins).

### 6e — Carried from prior weeks, status unchanged

- **Marketplace-documentation page (Amazon + TikTok Shop).** Still the highest-intent traffic available
  to this site, still unbuilt, SERP still held by labs, 3PLs and regulatory consultants rather than
  manufacturers. Full document table in the 2026-08-31 report, §6b. **Caution stands:** FDA registration
  satisfies TikTok Shop but does **not** satisfy Amazon's certificate requirement — Amazon excludes FDA
  inspections and first-party/consulting audits. State each marketplace's requirement separately.
- **New York / Long Island geo page.** Unbuilt. Three Long Island competitors rank; Paramount is absent.
- **Directory submissions** — comanufacturers.com, Keychain, Inventory Ready, KokoQuest. Submission
  forms, not link-building. Now doubly justified by 5d.
- **Creatine gummy/RTD stability post.** Gated on confirming capability plus stability data.
- **GLP-1 companion section** on `/protein-powder-manufacturing/` — protein for muscle preservation,
  fiber and electrolytes for side effects. Section plus internal links, not a new page. Keep claims
  nutritional, never drug-replacement.
- **Electrolyte / hydration / stick pack.** Unchanged; `/protein-powder-manufacturing/` is the template.
  2026 trade coverage again lists hydration among the top summer categories.
- **Softgels — still do not act.** Confirm in-house capability or a reliable toll partner first.
- **Regulatory watch, no action yet:** FDA self-GRAS reform, NDIN safety/identity guidance, caffeine
  labeling and "oversight modernization" are on FDA's 2026 priority deliverables; FDA is exercising
  enforcement discretion on disclaimer placement and may relax warning-label rules; a federal bill would
  preempt state supplement sales bans; NY restricts weight-loss and muscle-building supplement sales to
  minors. All increase brands' documentation burden, which favours a well-documented manufacturer —
  they feed the marketplace-documentation page rather than justifying pages of their own. **No page
  should be written on MAHA or FDA reform directly**; founders do not search for it with buying intent.

### 6f — Existing pages worth strengthening, all still open

- **Rows 11 and 12** (`/capsule-manufacturing/`, `/protein-powder-manufacturing/` form check) — still
  the cheapest high-value item in this report, sixth week running.
- **Homepage comparison copy.** The capsule/tablet/gummy comparison sitting on the homepage should be
  the spine of `/gummy-vs-capsule/`. It currently ranks for nothing where it is.
- **Titles.** Confirm the `/contact/` ↔ `/dietary-supplement/` duplicate against live HTML, then retitle
  `/contact/` for its actual job. `/testimonials/` ("Food Supplement Manufacturer | North America") and
  `/blog/` ("Blog | North America – Paramount Nutra") carry the same template bloat. Dropping
  `- Paramount Nutra` from titles already over 60 characters buys ~18 characters back.
- **The indexed PDF.** `Stock-Vegan-Greens-Paramount-PDF.pdf` still appears in `site:` results ahead of
  `/stock-formulations/`. Check for a CTA; add one or canonical/link it back.
- **FAQ blocks with FAQ schema on money pages.** Answer objections where the form is. Gummy first:
  MOQ, first-run lead time, pectin/vegan/sugar-free, stock-vs-custom cost. Add the
  marketplace-documentation question to every one.
- **Internal linking.** Cost and MOQ posts should link hard into matching money pages.
- **Off-ICP:** `/boost-your-immune-system-with-nutrient-rich-foods/` is consumer-facing. No further
  investment.

### 6g — Competitor movement

- **Aurinutra (NYC)** — escalating fastest. Now ranks for both the NY geo-listicle (ranking itself #1)
  *and* the low-MOQ 2026 guide. A month ago it was absent from these reports entirely.
- **Bactolac (Hauppauge, NY)** — new this week: dedicated NSF-certified sports manufacturer page.
  Segmenting by certification tier.
- **Makers Nutrition (Commack, NY)** — unchanged, still the most direct local threat: 177,000 sq ft,
  FDA-registered, explicitly courting startups on low MOQ.
- **Matsun Nutrition** — holds multiple low-MOQ pages *and* a format-comparison page
  ("Liquid vs. Gummy vs. Capsule"), i.e. it already owns the query `/gummy-vs-capsule/` was written for.
  Every week that post sits unpublished, that position hardens.
- **The comparison-listicle layer** remains the real competitor, now national and local. Paramount
  appears on none.
- **Still nobody has staked the marketplace-documentation manufacturer position** across Amazon and
  TikTok Shop. Windows like that close.

---

## 7. This week's recommended actions

Ranked by likely lead impact ÷ effort. **(carried)** marks items on prior lists that remain undone.

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | **Decide the egress question** (carried ×5) — either add `paramountnutra.com` / `www.paramountnutra.com` to allowed hosts, **or** stand up an external form monitor and formally drop sections 1–4 from this routine. Six weeks of "unverified" is not monitoring. | Critical — restores lead-capture monitoring, or stops pretending to | 5 min, or 1 hr for the alternative |
| 2 | **Open WordPress Posts and fix WP-Cron** (carried ×4) — publish `/gummy-vs-capsule/` and `/what-cgmp-actually-means/`. 34 days with nothing live. Fixing cron protects the rest of September. | Critical — recovers two written posts, stops the bleed | 10–20 min |
| 3 | **Check `/capsule-manufacturing/` and `/protein-powder-manufacturing/` for `gform_3`** (carried ×5). Two live money pages never once verified. Add to the monitored list either way. | High — possible live revenue leak, trivially checkable | 5 min |
| 4 | **Answer the certificate question (6d)** (carried ×4) — which schemes do the six partner facilities hold? Now gates three separate pages. | Critical as an input — decides whether the best opportunities are real | 30 min internal |
| 5 | **Decide the published MOQ number, then build the low-MOQ page (5a).** Benchmarks are public, a competitor now ranks for the query, and the trade press names it a baseline buying criterion. Moved up from #11. | Very high — highest-volume high-intent query in the category, plus pre-qualification | 1 hr decision + 4 hrs page |
| 6 | **Submit Paramount to the manufacturer directories** (carried) — comanufacturers.com, Keychain, Inventory Ready, KokoQuest. Competitors rank on these for Paramount's own geography, and 5d gives a second reason. | High — qualified leads, backlinks, AI-answer presence, defensive | 1–2 hrs |
| 7 | **Work the section 4 checklist manually** (carried) until monitoring is restored. | High — catches silent revenue loss now | 15 min |
| 8 | **Retarget `/what-cgmp-actually-means/` before publishing** (carried) — accepted schemes, why FDA registration is not one for Amazon, claims alignment, TikTok Shop's separate document set. Same effort, far better funnel position. Gated on #4. | Very high — urgent commercial intent, already written | 1–2 hrs edit |
| 9 | **Build the marketplace-documentation page** (carried) covering Amazon *and* TikTok Shop. Gated on #4 for claim scoping. | Very high — highest-intent traffic available to this site | 4–6 hrs |
| 10 | **Build a New York / Long Island geo page** (carried). Paramount is a NY manufacturer invisible on NY queries while three Long Island competitors rank. | High — high-intent local traffic, low real competition | 2–3 hrs |
| 11 | **Retitle `/contact/`, `/testimonials/`, `/blog/`** after confirming the duplicate against live HTML. | High — resolves a regression of a previously fixed problem | 1 hr |
| 12 | **Sports-nutrition certification page (5b)** — only if #4 comes back positive. A named local competitor is already earning these leads. | High if certified, zero if not — do not write it otherwise | 3 hrs, gated |
| 13 | **Add FAQ + FAQ schema to `/gummy-manufacturing/`**, then tablet, liquid, private label. | High — question intent where the form is | 2–3 hrs, then ~1 hr each |
| 14 | **Write the tariff / domestic-sourcing post (5c).** Exclusions are active and the rate is stable through November — it is finally writable with specifics. Verify against a customs broker; no unqualified "Made in USA". | Medium-high — genuinely useful, differentiated, well-timed | 3–4 hrs |
| 15 | **Confirm creatine gummy/liquid capability, then write the stability post** (carried). | High — differentiated, low competition | 30 min internal + 3–4 hrs |
| 16 | **Add a GLP-1 companion section to `/protein-powder-manufacturing/`** with internal links (carried). | Medium-high — strongest-evidenced 2026 category | 2 hrs |
| 17 | **Check the indexed stock-formulations PDF for a CTA** (carried); add one or canonical it back. | Medium-high — recaptures attention already paid | 20 min |
| 18 | **Internal linking pass** (carried) — contextual CTAs from cost and MOQ posts into money pages. | Medium — converts traffic already on site | 1 hr |
| 19 | **Target drink-mix / stick-pack / electrolyte intent** (carried) — extend `/protein-powder-manufacturing/`. | Medium-high — fast-growing format, template exists | 3–4 hrs |
| 20 | **Audit the "food supplement manufacturer" cluster** (carried) — consolidate and 301 if GSC confirms overlap. | Medium — protects a previously fixed problem | 1 hr, pending GSC |
| — | **Do NOT buy an AI-search/GEO engagement (5d).** Listed to be declined, not done. | — | — |

Items 5, 8, 9, 10, 12, 14, 15, 16 and 19 feed the 2-posts-per-month cadence rather than competing with
it — **once #2 makes publishing work again.**

**Re-ranked this week:** #5 (low-MOQ page) jumped from #11 to #5 — the benchmarks went public, the trade
press named it the buying criterion, and a competitor started ranking for it during the month Paramount
published nothing. #4 (certificate question) rose because it now gates three items rather than one.
#12 and #14 are new. #1 changed from "fix the allowlist" to "decide", because six weeks of the same
recommendation means the recommendation, not the reader, needs to change.

---

## 8. Data the human needs to pull

GA4 and Search Console remain inaccessible from here. Most valuable first.

**Lead capture — six weeks unverified:**

1. How many `generate_lead` events fired in the last 42 days versus the prior 42? With the routine blind
   for six weeks this is the *only* evidence the forms have worked at all. A sharp drop to zero on any
   page dates the breakage.
2. Which URLs produced those events? Traffic with zero leads across six weeks almost certainly means a
   missing or broken form.
3. Do `/capsule-manufacturing/` and `/protein-powder-manufacturing/` appear, and what traffic do they
   get? Decides whether action #3 is urgent or routine.
4. Did `/contact/` quote submissions over the last 42 days match what actually arrived in the sales
   inbox? A gap there is a notification failure, not a form failure — a different fix.

**Search Console:**

5. **Impressions for MOQ queries** — *low MOQ supplement manufacturer*, *minimum order quantity
   supplements*, *small batch supplement manufacturing*. Non-zero impressions with no dedicated page
   makes #5 the top action outright, ahead of everything except the two P0/P1 fixes.
6. Impressions for **marketplace-compliance** queries — *Amazon cGMP*, *GMP certificate Amazon*,
   *NSF 173*, *supplement facts panel Amazon*, *Amazon claims alignment* — and **TikTok Shop** queries:
   *TikTok Shop supplement compliance*, *COA TikTok Shop*. Sizes #8 and #9.
7. Impressions for **geo queries** — *supplement manufacturer New York*, *Long Island*, *near me*,
   *Stony Brook*. Sizes #10 and tells you whether the local listicle is costing real traffic.
8. Impressions for **certification queries** — *NSF certified supplement manufacturer*, *certified for
   sport manufacturer*. If these are non-zero, #12 stops being speculative.
9. Do `/contact/` and `/dietary-supplement/` show impressions for the *same* queries? Confirms or kills
   the duplicate-title finding and decides #11.
10. Which queries **lost** impressions over the last 42 days? Six weeks with no publishing and no
    monitoring is exactly the window in which a quiet ranking loss would go unnoticed.
11. What is the last publish date shown for any post in GSC's coverage report? Independently confirms or
    refutes the WP-Cron diagnosis without opening WordPress.

---

*Report generated without access to the live site (network egress policy), WordPress, GA4, or Search
Console. Sections 1–4 are unverified by design, not by omission. Sections 6–8 are based on public search
data gathered 2026-09-07.*
