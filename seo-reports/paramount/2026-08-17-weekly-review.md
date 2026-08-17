# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-08-17
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-08-10-weekly-review.md`

---

## 1. Bottom line

**Third consecutive week blind** — the egress allowlist fix requested on 08-03 and 08-10 still has not
been made, so lead capture has now gone **21 days** with no verification that the forms render, the PDF
downloads, or GA4 still fires. `/gummy-vs-capsule/` is **13 days overdue** with no trace in the index,
and `/what-cgmp-actually-means/` is due **tomorrow** and will likely fail the same way. Beyond the
five-minute allowlist fix, the highest-value action this week is time-sensitive and new: **Amazon's
January 2026 third-party cGMP mandate has created an urgent, deadline-driven demand spike that a
cGMP contract manufacturer is the direct answer to** — and tomorrow's scheduled post is already
pointed at the right topic and could be retargeted to capture it.

---

## 2. P0 / P1 issues

### P0 — Monitoring blind for a third week. Lead capture UNVERIFIED for 21 days.

Re-confirmed today on both available channels:

```
kind:   connect_rejected
detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
host:   paramountnutra.com:443
```

- `curl` fails at the CONNECT tunnel (exit 56, HTTP 000). `WebFetch` returns
  `EGRESS_BLOCKED` for the same domain. `www.paramountnutra.com` fails identically.
- Control test run fresh today: `github.com` connects; `example.com` and `www.google.com` are
  **blocked identically**. This is a narrow egress allowlist (GitHub, npm, PyPI and similar) — it is
  **not** a site outage, and **not** the known 406/User-Agent quirk.
- `/root/.ccr/README.md` is explicit that 403/407 policy denials must be reported, not retried or
  routed around. No workaround was attempted.

The severity is escalating purely on elapsed time. Three weeks is long enough for a Gravity Forms or
WordPress auto-update to have silently broken the guide-download form on all fifteen monitored URLs
with nobody noticing. Nothing in this report should be read as evidence the forms work.

**Fix:** add `paramountnutra.com` (and `www.paramountnutra.com`) to this environment's egress
allowlist in the Claude Code environment settings, then re-run the routine. Sections 4 and the
performance check stay empty until that happens.

### P1 — `/gummy-vs-capsule/` almost certainly failed to publish

Due **2026-08-04**, now **13 days overdue**. Targeted search for the slug and topic again returns
nothing from `paramountnutra.com` — only competitor articles on the identical topic (HDNUTRA,
Vitaquest, Advanced Supplements, Intermountain Nutrition). Meanwhile a general `site:` query returns
plenty of other pages on the domain, including `/blog/`, so the site is crawlable and being indexed.

Last week this was called "suggestive, not conclusive" at six days. At thirteen days, indexing lag is
no longer a credible explanation. **Treat this as a failed scheduled publish until someone opens the
WordPress Posts screen and proves otherwise.** The usual cause is a missed WP-Cron event leaving the
post in "Missed schedule" status.

### P1 — `/what-cgmp-actually-means/` is due tomorrow and is likely to fail the same way

Due **2026-08-18**. If WP-Cron is the root cause of the first failure, it has not been fixed, so this
post will miss too. This is the one thing in this report where acting *before* the deadline costs
nothing and acting after costs another two weeks of delay. See recommendation #3 — and note that this
post's topic is now considerably more valuable than when it was scheduled (section 6a).

### P1 (suspected, carried forward) — duplicate title regression

Unchanged from last week and still unverified against live HTML. `/contact/` still carries "Dietary
Supplement Company | North America – Paramount Nutra" in the index, near-identical to
`/dietary-supplement/`'s "Dietary Supplement Company | North America". Title cannibalization was a
previously fixed problem on this site, which is why a suspected regression is logged at P1 rather than
filed as an optimization. Confirm against live HTML before editing. Detail in section 6d.

---

## 3. Changed since last week

**The block was not fixed.** Third week. That is the headline delta and the reason sections 4 and the
performance check are again empty.

**The cadence problem hardened from "suspected" to "assume broken."** `/gummy-vs-capsule/` went from
six days overdue to thirteen with no index trace. Thirteen days is past the point where lag explains
it.

**A significant new external driver appeared — this is the real news this week.** Amazon's expanded
dietary-supplement policy took effect in January 2026 and requires *every* supplement seller to
produce an accredited third-party cGMP certificate. Enforcement began deactivating non-compliant
listings in March 2026 and is rolling out in waves with 90-day windows. This did not feature in either
prior report and it materially changes the ranked recommendations — see section 6a.

**Tariff movement now touches supplement ingredients specifically.** As of **2026-07-24**, amino
acids, CoQ10 and choline lost blanket tariff exemption for supplement use; non-exempt Chinese
ingredient categories are carrying roughly 17.5–35% plus an additional 12.5% Section 301 duty. Three
weeks old and directly relevant to any protein, EAA or pre-workout brand's cost model. New this week.

**Two new index observations:**

- `/blog/` is titled **"Blog | North America – Paramount Nutra"**. The `| North America` template is
  now appended to a page where it means nothing, spending the title budget on a region qualifier for a
  post index. Cheap fix, bundled into recommendation #6.
- The **top result** for a `site:paramountnutra.com` query is a PDF —
  `/wp-content/uploads/2024/06/Stock-Vegan-Greens-Paramount-PDF.pdf` — outranking
  `/stock-formulations/`, the page that should own that intent. A stock-formulation spec sheet
  outranking its own money page is a lead leak if the PDF has no CTA or path back to a form. Worth a
  look, low effort.

**Last week's recommendation #2 appears not to have been done.** Nobody has confirmed whether
`/capsule-manufacturing/` and `/protein-powder-manufacturing/` carry the download form. It was a
five-minute check, ranked second, and it remains open.

**Still no measured baseline, third week running.** No payload, response-time, title-length or
meta-description deltas can be computed. The first successful crawl establishes the baseline that all
future week-over-week comparisons depend on; every week without it is a week of trend data that can
never be recovered.

---

## 4. Site health table

**Cannot be populated.** A guessed "Y" in a form-present column is worse than no report, so this stays
empty for a third week.

What follows is therefore not a health table but a **manual verification checklist** — the exact list a
human can work through in about fifteen minutes to close the highest-risk gap while the allowlist fix
is pending. Every row is unverified as of today.

| # | URL / check | Look for | Status |
|---|---|---|---|
| 1 | `/gummy-manufacturing/` | `gform_3` | NOT VERIFIED (21 days) |
| 2 | `/private-label-supplement-manufacturer/` | `gform_3` | NOT VERIFIED (21 days) |
| 3 | `/liquid-supplement-manufacturing/` | `gform_3` | NOT VERIFIED (21 days) |
| 4 | `/tablet-manufacturing/` | `gform_3` | NOT VERIFIED (21 days) |
| 5 | `/stock-formulations/` | `gform_3` | NOT VERIFIED (21 days) |
| 6 | 10 monitored blog posts | `gform_3` | NOT VERIFIED (21 days) |
| 7 | `/contact/` | `gform_wrapper` (quote form) | NOT VERIFIED (21 days) |
| 8 | `Supplement-Launch-Guide-2026.pdf` | HTTP 200 | NOT VERIFIED (21 days) |
| 9 | Homepage | `generate_lead` ×1, `G-XK72PDD5T8` | NOT VERIFIED (21 days) |
| 10 | Homepage | `Made in cGMP-Certified`, `What Our Clients Say` | NOT VERIFIED (21 days) |
| 11 | **`/capsule-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 12 | **`/protein-powder-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 13 | Full sitemap crawl | status, redirects, titles, metas | NOT VERIFIED (21 days) |
| 14 | Homepage + one money page | response time, transfer size | NO BASELINE EXISTS |

Rows 11 and 12 are the ones to do first if time is short: they are live money pages ranking for
commercial queries that no run of this routine has ever inspected, because they are not in its
hardcoded list. Add them to the monitored list regardless of the outcome.

---

## 5. Content cadence

**Verdict: behind, and the mechanism looks broken rather than merely slow.**

| Post | Due | Status as of 2026-08-17 |
|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **13 days overdue, no index trace** — assume failed publish (P1) |
| `/what-cgmp-actually-means/` | 2026-08-18 | **Due tomorrow** — high risk of the same failure (P1) |

Against the 2-posts-per-month target, **August has zero confirmed published posts** with two weeks
left. Both scheduled posts are written; if the diagnosis is right, the content exists and is simply
not live, which is the cheapest possible problem to fix and the most wasteful one to leave alone.

Posts published in the last 60 days still cannot be enumerated — that needs `post-sitemap.xml`, which
is behind the egress block.

---

## 6. Opportunity analysis

### 6a. Amazon's cGMP mandate is the best lead opportunity this site has — with one hard prerequisite

**What changed.** Amazon's expanded dietary-supplement policy, effective January 2026, requires every
seller to submit a valid GMP certificate from an **accredited third-party certification body** against
21 CFR 111 or 117, per product/ASIN. Accepted schemes include NSF/ANSI 455-2, NSF/ANSI 173 Section 8,
GRMA 455-2, UL GMP, USP GMP, Eurofins, SGS, Intertek and SQF. Products in bodybuilding, joint health,
sexual enhancement, sports nutrition and weight management need additional NSF/ANSI 173-2023 testing.
Enforcement has been deactivating non-compliant listings since March 2026, rolling out in waves with a
90-day window once a seller is contacted and no published schedule.

**Why this is unusually good.** Three things rarely line up like this:

1. **Forced urgency with a hard deadline.** This is not a founder idly researching formats. It is a
   seller whose listings are about to be deactivated, on a 90-day clock, searching right now.
2. **The searcher's problem is a manufacturer-shaped problem.** Half the answer to "how do I get an
   accredited cGMP certificate for my ASIN" is "be manufactured somewhere that already holds one."
   A contract manufacturer is the solution, not an adjacent vendor.
3. **The SERP is held by the wrong companies.** The query space is dominated by testing labs,
   certifiers and 3PLs — Certified Laboratories, NSF, Eurofins, BSCG, Prodigy Labs, Inventory Ready,
   3PLGuys, FoodLabelMaker. Contract manufacturers are barely present; only Brand International and
   Paragon Labs USA surfaced with anything targeted. Those labs will sell a test. They cannot sell a
   compliant facility. Paramount can.

**The hard prerequisite — verify this before writing a word.** Paramount's public copy says
"cGMP-certified, FDA-registered **partner facilities**." Two problems:

- **"FDA-registered" does not satisfy Amazon.** The policy explicitly excludes FDA inspections, along
  with private, first-party and consulting audits. Only accredited third-party certification counts.
  Leading with FDA registration on this query would actively mislead the exact buyer being courted.
- **"Partner facilities" raises the question of whose certificate the brand actually receives.**
  Paramount runs a network of six facilities. Amazon needs a certificate per product, tied to the
  facility that made it.

So the question to answer internally, before any content: **which of the partner facilities hold a
current accredited third-party GMP certificate under an Amazon-accepted scheme, and can Paramount hand
a customer that certificate for their ASIN?**

- **If yes** — this is the single highest-value page on the roadmap, above the low-MOQ page. It is
  bottom-of-funnel, deadline-driven, and Paramount holds the asset the searcher needs. Publish the
  scheme names and say plainly that documentation is provided for Amazon submission.
- **If no, or only for some facilities** — say only what is true, scoped to the facilities that
  qualify. Ranking for a compliance promise that cannot be documented is worse than not ranking:
  it generates leads that die at diligence and it burns trust with the most sophisticated segment of
  the market. Same discipline applied to softgels in the two prior reports.

**The time-sensitive move.** `/what-cgmp-actually-means/` is scheduled for **tomorrow**. As
conceived it is a generic educational explainer. Retargeted, it becomes the exact answer to an
urgent commercial query: what cGMP means, *which certifications Amazon actually accepts, why FDA
registration is not one of them*, what the 90-day window is, and what documentation a brand should
demand from a manufacturer. Same effort, a fundamentally different funnel position. The only reason
this is ranked below the publish-mechanism fix is that a post that does not go live earns nothing.

**Keyword cluster:** *Amazon supplement cGMP requirements*, *Amazon compliant supplement
manufacturer*, *GMP certificate for Amazon supplements*, *NSF 173 supplement manufacturer*,
*Amazon dietary supplement policy 2026*, *supplement manufacturer for Amazon sellers*.

### 6b. Tariff-driven domestic sourcing — a narrower but well-timed angle

As of **2026-07-24**, amino acids, CoQ10 and choline lost blanket tariff exemption for supplement use.
Non-exempt Chinese ingredient categories now carry roughly 17.5–35% plus an additional 12.5% Section
301 duty. India dropped to 18% in February with key botanicals exempted. Core vitamins and minerals
remain exempt.

The amino acid change is the sharp end: it hits protein, EAA, BCAA and pre-workout brands — a segment
Paramount already serves through `/protein-powder-manufacturing/` — and it hit three weeks ago, which
means those brands are re-running their COGS right now. A domestically-manufactured, US-sourced-where-
possible position is a genuine commercial argument this quarter, not a slogan.

Caveat, stated plainly: the tariff coverage available from here is heavily pharmaceutical-weighted, and
the supplement-specific detail is thinner than the Amazon finding. Treat the direction as solid and
verify current rates with a customs broker before publishing specific numbers. **Do not publish a
"Made in USA" claim without checking it against the FTC's Made in USA standard** — that phrase has its
own compliance exposure, and "manufactured in the USA" or "domestically manufactured" is usually the
safer, equally persuasive framing.

Lower priority than 6a: real, but the intent is diffuse and it suits a blog post or a section on the
powder page rather than a new money page.

### 6c. Carried forward from prior weeks — status unchanged

- **Low MOQ money page.** Still the highest-volume high-intent query in the category, still unbuilt,
  still gated on a business decision about what number to publish. Every visible competitor — Matsun
  (MOQ from 2,500), Aurinutra, SummitRx, Sun Nutraceuticals, HDNUTRA — has staked it. Paramount has an
  educational post at `/supplement-moqs-explained/` and no published number anywhere. Now ranked
  *below* the Amazon cluster, because Amazon compliance is deadline-driven and MOQ is not.
- **Electrolyte / hydration / stick pack / creatine.** Fastest-growing powder formats; the existing
  powder page is the template. Unchanged.
- **GLP-1 companion formulation.** Still open, still timely, still a caution to keep claims on
  nutritional support rather than drug replacement.
- **Softgels — still do not act.** Confirm in-house capability or a reliable toll partner first.
- **Newly noted from the 2026 trend coverage:** targeted women's-health categories — menopause,
  fertility, vaginal health — are called out as rising. Flagged for awareness only; no evidence yet
  that founders in that category search for a *manufacturer* differently, so this does not justify a
  page on current evidence. Worth a Search Console check (question 8).

### 6d. Existing pages worth strengthening

**Rows 11 and 12 of section 4 remain the cheapest high-value item in this report.**
`/capsule-manufacturing/` and `/protein-powder-manufacturing/` are live money pages nobody has ever
confirmed carry a lead form. Two page-loads to check. Third week this has been flagged.

**Titles.** Confirm the `/contact/` ↔ `/dietary-supplement/` duplicate against live HTML, then retitle
`/contact/` for its actual job (getting a quote request) rather than competing for a head commercial
term. `/testimonials/` holding "Food Supplement Manufacturer | North America" has the same problem.
`/blog/` at "Blog | North America – Paramount Nutra" is new this week and is pure template bloat.
Dropping the `- Paramount Nutra` suffix on titles already over 60 characters buys back ~18 characters
of keyword room at zero risk.

**The indexed PDF.** `Stock-Vegan-Greens-Paramount-PDF.pdf` outranks `/stock-formulations/` on a
`site:` query, which suggests it has accumulated links. Check whether it carries any CTA or path back
to a form. If not, it is receiving attention and converting none of it — and a canonical or internal
link pointing at `/stock-formulations/` recaptures it.

**FAQ blocks with FAQ schema on money pages.** Unchanged. Answer the objection where the form is, not
on a central `/faq/` page. For `/gummy-manufacturing/`: MOQ, first-run lead time,
pectin/vegan/sugar-free capability, stock-vs-custom cost difference. Then tablet, liquid, private
label. Check `/faq/` for reusable schema first. **Add "is this Amazon-compliant / what documentation do
I get" to every money page's FAQ** once 6a is answered — it is now a live objection on every deal.

**Internal linking.** Unchanged. The cost and MOQ posts are the likeliest top-of-funnel entry points;
each should link hard into the matching money page with a contextual CTA, not merely host the download
form.

**Off-ICP content.** `/boost-your-immune-system-with-nutrient-rich-foods/` is consumer-facing on a site
selling to founders. No rewrite needed; no further investment either.

### 6e. Competitor movement

**Competitors already own the gummy-vs-capsule SERP.** HDNUTRA, Vitaquest, Advanced Supplements and
Intermountain Nutrition all rank for the exact topic of the post that failed to publish on 08-04. This
does not make the post worthless, but it does mean it enters a contested SERP and needs a genuine angle
— manufacturing cost, MOQ and lead-time differences between the two formats, which is what a founder
actually wants and what a consumer-facing comparison will not give them.

**The comparison-listicle layer remains the real competitor.** Unchanged from last week: HDNUTRA and
Matsun publish their own roundups that rank for competitors' queries and route traffic to their own
forms. Paramount appears on none of them. Also new this week: CSK Biotech is running "Best Private
Label Supplement Manufacturers 2026: Ranked by Pricing, MOQ and Purity" — the same play, explicitly
ranked on MOQ, which is the number Paramount has not published.

**Nobody has convincingly staked the Amazon-compliance manufacturer position.** The window in 6a is
open because labs and 3PLs are answering a question that a manufacturer answers better. Windows like
that close.

---

## 7. This week's recommended actions

Ranked by likely lead impact ÷ effort.

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | **Fix the egress allowlist** — add `paramountnutra.com` and `www.paramountnutra.com` to this environment's allowed hosts. Three weeks blind is the largest single risk in this report, and every week without a baseline is trend data lost permanently. | Critical — restores all lead-capture monitoring | 5 min |
| 2 | **Open WordPress Posts. Publish `/gummy-vs-capsule/` and check WP-Cron before tomorrow.** `/what-cgmp-actually-means/` is due 08-18 and will likely miss too. Finished content that is not live earns nothing. | Critical — recovers two posts and stops the bleed | 10–20 min |
| 3 | **Check `/capsule-manufacturing/` and `/protein-powder-manufacturing/` for `gform_3`.** Two live money pages never once verified. Add them to the routine's monitored list either way. | High — possible live revenue leak, trivially checkable | 5 min |
| 4 | **Manually verify the section 4 checklist** — forms on the five money pages, `/contact/`, and the guide PDF — until monitoring is restored. | High — catches silent revenue loss now | 15 min |
| 5 | **Answer the certificate question in 6a:** which partner facilities hold a current accredited third-party GMP certificate under an Amazon-accepted scheme, and can a customer be handed it for their ASIN? Gates #6 and #7. | Critical as an input — decides whether the best opportunity is real | 30 min internal |
| 6 | **Retarget `/what-cgmp-actually-means/` at Amazon's mandate before it publishes** — accepted schemes, why FDA registration is not one, the 90-day window, what documentation to demand from a manufacturer. Same effort, far better funnel position. | Very high — urgent commercial intent, post already written | 1–2 hrs edit |
| 7 | **Build the Amazon-compliance money page** (conditional on #5): "Amazon-Compliant Supplement Manufacturing." Bottom-of-funnel, deadline-driven, SERP held by labs rather than manufacturers. Scope claims to what is documented. | Very high — highest-intent traffic available to this site | 4–6 hrs |
| 8 | **Retitle `/contact/`, `/testimonials/` and `/blog/`** after confirming the duplicate against live HTML; drop `- Paramount Nutra` on titles over 60 chars. | High — resolves a regression of a previously fixed problem | 1 hr |
| 9 | **Decide the published MOQ number, then build the low-MOQ page.** Highest-volume high-intent query; every competitor has staked it and CSK is now ranking brands on it. | High — direct leads plus pre-qualification | 1 hr decision + 4 hrs page |
| 10 | **Add FAQ sections with FAQ schema to `/gummy-manufacturing/`**, then tablet, liquid, private label — including the Amazon-documentation question. Check `/faq/` for reusable schema. | High — question intent on the page holding the form | 2–3 hrs, then ~1 hr each |
| 11 | **Request listings on the NY / USA manufacturer roundups and directories.** Carried for three weeks, still not done, still the cheapest lead channel here. | High — qualified leads plus backlinks | 1–2 hrs |
| 12 | **Check the indexed stock-formulations PDF for a CTA**; add one, or link/canonical it back to `/stock-formulations/`. | Medium-high — recaptures attention already being paid | 20 min |
| 13 | **Internal linking pass** — contextual CTAs from the cost and MOQ posts into matching money pages. | Medium — converts traffic already on site | 1 hr |
| 14 | **Target drink-mix / stick-pack / electrolyte / creatine intent** — extend `/protein-powder-manufacturing/` or add a sibling page. | Medium-high — fastest-growing format, template exists | 3–4 hrs |
| 15 | **Write the domestic-sourcing / tariff post** aimed at protein and amino-acid brands. Verify rates with a customs broker; avoid an unqualified "Made in USA" claim. | Medium — well-timed, diffuse intent | 3–4 hrs |
| 16 | **Audit the "food supplement manufacturer" cluster** — `/testimonials/` plus the two blog posts. Consolidate and 301 if GSC confirms overlap. | Medium — protects a previously fixed problem | 1 hr, pending GSC |
| 17 | **Write the GLP-1 companion formulation post.** Keep claims on nutritional support. | Medium — positions ahead of the category | 3–4 hrs |
| 18 | **Consider Paramount-authored comparison content** to contest the listicle layer. | Medium — mid-funnel intent no service page reaches | 4–6 hrs |

Items 6, 9, 14, 15, 17 and 18 all feed the 2-posts-per-month cadence rather than competing with it.

**Re-ranked this week:** the Amazon cluster (#6, #7) now sits above the low-MOQ page (#9), which was
last week's top content recommendation. Deadline-driven compliance intent converts faster than
comparison-shopping intent, and the SERP is weaker.

---

## 8. Data the human needs to pull

GA4 and Search Console remain inaccessible from here. Specific questions, most valuable first:

**Lead capture — three weeks unverified:**
1. How many `generate_lead` events fired in the last 21 days versus the prior 21? With the routine
   blind for three weeks, this is the *only* evidence the forms have been working at all. A sharp drop
   to zero on any page dates the breakage.
2. Which URLs produced those events? A page with traffic and zero leads across three weeks almost
   certainly has a missing or broken form.
3. Do `/capsule-manufacturing/` and `/protein-powder-manufacturing/` appear in that list, and what
   traffic are they getting? Decides whether recommendation #3 is urgent or routine.
4. Did `/contact/` quote submissions over the last 21 days match what actually arrived in the sales
   inbox? A gap there is a notification failure, not a form failure — different fix.

**Search Console:**
5. Is the site receiving **any** impressions for Amazon-compliance queries today — *Amazon cGMP*,
   *Amazon supplement requirements*, *GMP certificate Amazon*, *NSF 173*? Non-zero impressions with no
   dedicated page would move recommendations #6 and #7 to the top of the list outright.
6. Do `/contact/` and `/dietary-supplement/` show impressions for the *same* queries? Confirms or kills
   the duplicate-title finding and decides recommendation #8.
7. Same question across `/testimonials/` and the two "food supplement manufacturer" blog posts — which
   actually earns the impressions? Keep that one, consolidate the rest.
8. Any impressions for **low MOQ / minimum order quantity** queries? And for electrolyte, hydration,
   drink mix, stick pack, creatine, or menopause/fertility manufacturing queries? Sizes #9, #14 and
   the women's-health flag in 6c.
9. **Is `/gummy-vs-capsule/` in the index at all?** URL Inspection settles in seconds what public
   search could only infer. Same check for `/what-cgmp-actually-means/` after 08-18.
10. Any new Coverage or Page Indexing errors since last month, particularly pages dropping out?

**Cadence and infrastructure:**
11. WordPress Posts screen: is `/gummy-vs-capsule/` published, draft, or "Missed schedule"? If the
    last, **is WP-Cron firing at all?** That is the root cause and it will take tomorrow's post too.

**Internal, not a data pull — gates the best opportunity:**
12. Which partner facilities hold a current accredited third-party GMP certificate, under which scheme
    (NSF/ANSI 455-2, NSF 173 §8, GRMA 455-2, UL, USP, Eurofins, SGS, Intertek, SQF), and can a
    customer be handed that certificate for their ASIN? Everything in 6a depends on this answer.

---

## Methodology note

Sections 6 and 7 derive from Google's public index and third-party trade sources via web search — the
only research channel reachable from this environment. Indexed titles can be stale and say nothing
about HTTP status, redirects, meta descriptions, page content, or form presence. **No claim in this
report constitutes verification that any form, PDF, or analytics tag is working.** Regulatory,
tariff and marketplace-policy details are summarised from trade press and should be confirmed against
primary sources before being published as customer-facing claims. Recommendation #1 is what turns next
week's report back into measurement.
