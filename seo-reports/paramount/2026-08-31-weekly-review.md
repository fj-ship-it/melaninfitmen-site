# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-08-31
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-08-24-weekly-review.md`

---

## 1. Bottom line

**Fifth consecutive week blind** — lead capture has now gone **35 days** unverified, and August closes
today with **zero published posts** against a 2/month target. The single highest-value action is still
the five-minute egress allowlist fix, which is now the longest-running unactioned item in this report's
history. The most valuable *new* finding is competitive, not technical: a NYC competitor publishes the
**"Top 10 Supplement Manufacturers in New York"** listicle, ranks itself first, and **Paramount is not
on it** — while two Long Island neighbours are.

---

## 2. P0 / P1 issues

### P0 — Monitoring blind for a fifth week. Lead capture UNVERIFIED for 35 days.

Re-confirmed today on both channels. Nothing has changed since last week:

```
kind:   connect_rejected
detail: gateway answered 403 to CONNECT (policy denial or upstream failure)
host:   paramountnutra.com:443
```

- `curl` fails at the CONNECT tunnel (exit 56, HTTP 000). `WebFetch` returns
  `{"error_type":"EGRESS_BLOCKED"}`. `www.paramountnutra.com` fails identically.
- Control tests today reconfirm last week's corrected diagnosis: `api.github.com` → 200,
  `registry.npmjs.org` → 200, `pypi.org` → 200; `example.com` and `www.google.com` → **blocked**.
  This is a **narrow allowlist covering developer infrastructure only**, excluding the general web.
  It is not a site outage, not the known 406/User-Agent quirk, and not a block aimed at
  paramountnutra.com specifically.
- `/root/.ccr/README.md` is explicit that 403/407 policy denials are reported, not retried or routed
  around. No workaround was attempted, including via connected third-party services — routing around
  a deliberate network policy is not mine to decide.

**Five weeks is long enough for a Gravity Forms or WordPress auto-update to have silently broken the
guide-download form on all fifteen monitored URLs with nobody noticing.** Nothing in this report is
evidence that any form, PDF, or analytics tag works.

**Fix:** add `paramountnutra.com` and `www.paramountnutra.com` to this environment's allowed hosts in
the Claude Code environment settings (https://code.claude.com/docs/en/claude-code-on-the-web covers
the network-policy options), then re-run the routine.

**Escalation note:** this item has been #1 for five consecutive weeks. If the allowlist cannot be
widened for policy reasons, the honest conclusion is that this routine cannot perform its primary
job — lead-capture integrity monitoring — and section 4 should be replaced with an external uptime/
form monitor (a scheduled check from any service that can reach the public web) rather than being
re-reported as "unverified" indefinitely.

### P1 — publish mechanism still broken. August ends with zero posts.

| Post | Due | Days overdue | Index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **27** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **13** | none |

Re-checked today with both a targeted slug/topic search and a `site:paramountnutra.com` query. The
`site:` query returns the homepage, `/testimonials/`, `/contact/`, `/capsule-manufacturing/`, `/blog/`
and the stock-greens PDF — so the domain is crawlable and indexing normally — but **neither scheduled
post appears**. Searches on both topics return only competitor articles.

Three weeks ago this was a suspicion; two weeks ago it was a prediction that came true; it is now a
month-long pattern. Treat "missed schedule / WP-Cron not firing" as confirmed until someone opens the
WordPress Posts screen and proves otherwise. **September's posts will miss the same way unless cron is
fixed**, which makes this cheaper to fix now than at any later point.

The cost is concrete and compounding: both posts are already written, one of them
(`/what-cgmp-actually-means/`) has now sat unpublished through five weeks in which its topic became
the most commercially valuable subject on this site's roadmap, and the site has published nothing for
a full month.

### P1 (suspected, carried forward, still unverified) — duplicate title regression

`/contact/` still carries **"Dietary Supplement Company | North America – Paramount Nutra"** in the
index, near-identical to `/dietary-supplement/`'s **"Dietary Supplement Company | North America"**.
Re-confirmed in today's `site:` results. Title cannibalization was a previously *fixed* problem on this
site, which is why this sits at P1. Confirm against live HTML before editing.

---

## 3. Changed since last week

**The block was not fixed. Fifth week.** Sections 4 and the performance check are empty again. Five
weeks of trend data are now permanently unrecoverable, and the measured baseline every future
week-over-week comparison depends on still does not exist.

**August finished with zero posts.** Last week this was "one week left"; that week has now elapsed. The
month is a confirmed zero against a target of two, with both posts written and sitting in the CMS.

**New and significant — a competitor owns Paramount's home-geography listicle.** Aurinutra (the NYC
competitor first flagged last week) publishes *"Top 10 Supplement Manufacturers in NEW YORK"* and ranks
**itself** as "best overall for New York-based startups." Paramount does not appear. The list that does
appear includes **Makers Nutrition (Commack, NY)** — a 177,000 sq ft FDA-registered facility explicitly
positioned on *"some of the lowest MOQs in the industry"* for startups — and **Bactolac Pharmaceutical
(Hauppauge, NY)**, both roughly fifteen minutes from Stony Brook. This upgrades last week's
"new competitor, and it is local" from a note to a ranked, named threat on geo-intent queries.

**New — TikTok Shop has become a second marketplace-compliance funnel, and nobody is serving it from
the manufacturer side.** The top 10 supplement brands on TikTok Shop are running roughly **$182M in
six months**. Onboarding requires a full label upload, **a COA from an approved lab**, and **proof of
manufacturing compliance** (FDA facility registration, plus ISO or HACCP). Trade coverage puts the
timeline at **6–12 weeks if the manufacturer genuinely meets cGMP and preserved its documentation, and
3–6 months if it did not** — because the brand has to go find a new manufacturer. That sentence is a
lead-generation asset. See 6a.

**New — the documentation requirements now have citable specifics.** Third-party testing guidance for
2026 names **ISO 17025-accredited** labs, **USP <2232>** (heavy metals), **USP <61>/<62>**
(microbiological), pesticide residue screening and stability data; ISO 17025 testing is called out as
required for Amazon FBA supplement sellers. Under 21 CFR 111 the manufacturer also owns **Master
Manufacturing Records**, supplier qualification, and identity/purity/strength/composition
verification. Prior reports argued the documentation angle in general terms; it can now be written with
specifics that signal genuine operator knowledge.

**New — sesame is the ninth major allergen** under the FASTER Act and must appear in the ingredient
list or a "Contains" statement. Small, concrete, and a legitimate label-review talking point.

**Federal/state regulatory picture sharpened (still no action required).** FDA's Office of Dietary
Supplement Programs now sits inside the new **Office of Food Chemical Safety, Dietary Supplements &
Innovation**; 2026 priority deliverables include **self-GRAS reform** and **NDIN safety/identity
guidance**. A federal bill would **preempt state supplement sales bans**. New York's existing law
restricts sale of weight-loss and muscle-building supplements to minors — relevant to Paramount's
customers in those categories, though it is a retail restriction rather than a manufacturing one.

**Carried and still undone:** `/capsule-manufacturing/` and `/protein-powder-manufacturing/` remain
**never once checked** for a lead form — fifth week flagged, still a two-page-load task.

---

## 4. Site health table

**Cannot be populated — fifth week.** A guessed "Y" in a form-present column is worse than no report.

The manual checklist below is what a human can work through in about fifteen minutes. Every row is
unverified as of today.

| # | URL / check | Look for | Status |
|---|---|---|---|
| 1 | `/gummy-manufacturing/` | `gform_3` | NOT VERIFIED (35 days) |
| 2 | `/private-label-supplement-manufacturer/` | `gform_3` | NOT VERIFIED (35 days) |
| 3 | `/liquid-supplement-manufacturing/` | `gform_3` | NOT VERIFIED (35 days) |
| 4 | `/tablet-manufacturing/` | `gform_3` | NOT VERIFIED (35 days) |
| 5 | `/stock-formulations/` | `gform_3` | NOT VERIFIED (35 days) |
| 6 | 10 monitored blog posts | `gform_3` | NOT VERIFIED (35 days) |
| 7 | `/contact/` | `gform_wrapper` (quote form) | NOT VERIFIED (35 days) |
| 8 | `Supplement-Launch-Guide-2026.pdf` | HTTP 200 | NOT VERIFIED (35 days) |
| 9 | Homepage | `generate_lead` ×1, `G-XK72PDD5T8` | NOT VERIFIED (35 days) |
| 10 | Homepage | `Made in cGMP-Certified`, `What Our Clients Say` | NOT VERIFIED (35 days) |
| 11 | **`/capsule-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 12 | **`/protein-powder-manufacturing/`** | `gform_3` — *never once checked* | NOT VERIFIED (ever) |
| 13 | Full sitemap crawl | status, redirects, titles, metas | NOT VERIFIED (35 days) |
| 14 | Homepage + one money page | response time, transfer size | NO BASELINE EXISTS |

Rows 11 and 12 first if time is short — live money pages ranking for commercial queries that this
routine has never inspected, because they are not in its hardcoded list. Add them to the monitored list
regardless of outcome.

**Performance (section 4 of the brief):** no data, fifth week. No payload or response-time deltas can
be computed, and none can be computed in future either until a first measurement exists.

---

## 5. Content cadence

**Verdict: behind, and the mechanism — not the content — is broken.**

**August 2026: zero published posts against a target of two.** The month is now closed. Both scheduled
posts are written; neither is live; neither has any index trace 27 and 13 days past their dates
respectively. Posts published in the last 60 days cannot be enumerated with dates — that requires
`post-sitemap.xml`, which is behind the egress block, so this section is inference from the public
index rather than measurement.

This remains the cheapest problem in the report to fix and the most wasteful to leave alone: the
content already exists and is earning nothing. Writing more posts before the publish mechanism is
fixed adds nothing.

---

## 6. Opportunity analysis

### 6a. NEW — TikTok Shop onboarding is a manufacturer-documentation problem, and the SERP is unclaimed

**What it is.** TikTok Shop supplement onboarding requires a complete product label upload, **a valid
COA from an approved lab**, and **proof of manufacturing compliance** — FDA facility registration plus
ISO or HACCP certification. Health/wellness sellers pass a category-specific verification, and certain
claims and ingredient categories are restricted or prohibited outright.

**Why it matters commercially.** The top 10 supplement brands on the platform are doing an estimated
**$182M in six months** (Micro Ingredients ~$31.2M YTD; Goli and MaryRuth's also in the top tier). This
is now a primary launch channel for exactly the founder profile Paramount sells to.

**Why it is a manufacturer's problem, not a consultant's.** The reported onboarding timeline is
**6–12 weeks when the manufacturer genuinely meets cGMP and kept its documentation, versus 3–6 months
when it did not** — because in that case the brand must find a new manufacturer first. That is the
single most persuasive argument a compliant contract manufacturer can make to a founder planning a
TikTok launch, and it is a *switching* argument as much as an acquisition one: it reaches brands
already burned by a cheap supplier.

**Why the SERP is winnable.** The results are held by 3PLs, regulatory consultancies and seller-service
agencies (fforder, Quality Smart Solutions, Blue Ocean Regulatory, NutraSeller, Sold Out Brands). They
answer from the audit and logistics side. **None of them can issue the COA or manufacture in the
registered facility.** Contract manufacturers are effectively absent.

**Concrete recommendation:** build one page — *"Supplement manufacturing for TikTok Shop and Amazon
sellers"* — covering the document set each marketplace demands, who produces each document, and the
timeline difference between a compliant and a non-compliant manufacturer. Add to every money page's
FAQ: *"Will I get the COA and facility documentation I need for TikTok Shop and Amazon?"*

**Keyword cluster:** *TikTok Shop supplement manufacturer*, *TikTok Shop supplement compliance
documents*, *COA for TikTok Shop supplements*, *supplement manufacturer FDA registration proof*,
*launch supplement brand TikTok Shop*.

### 6b. NEW — the marketplace-documentation position, unified

Prior reports treated Amazon claims alignment (6a last week) and the Amazon cGMP certificate (6b last
week) as separate opportunities. With TikTok Shop added, they are one position, and it is stronger as
one: **"we produce the documents the marketplaces make you produce."**

The document set is now specific enough to publish as a checklist page:

| Document | Who owns it | Required by |
|---|---|---|
| Supplement Facts panel matching all listing claims | Manufacturer | Amazon (claims alignment, since 2026-03-31) |
| COA — identity & potency | Manufacturer / ISO 17025 lab | Amazon, TikTok Shop |
| Heavy metals per **USP <2232>** | ISO 17025 lab | Amazon FBA, retail buyers |
| Microbiological per **USP <61>/<62>** | ISO 17025 lab | Amazon FBA, retail buyers |
| Pesticide residue screen, stability data | Manufacturer / lab | Category-dependent |
| FDA facility registration proof | Manufacturer | TikTok Shop |
| ISO or HACCP certification | Manufacturer | TikTok Shop |
| Third-party cGMP certificate (BSCG, Clean Label Project, GRMA, Informed Choice, NSF, USP) | Manufacturer | Amazon Fast-Track validation |
| Master Manufacturing Record, supplier qualification records | Manufacturer (21 CFR 111) | FDA inspection |
| Sesame allergen declaration (FASTER Act, 9th allergen) | Manufacturer / label | FDA labeling |

A page built on that table is genuinely useful, ranks for a dozen long-tail documentation queries, and
positions Paramount as the party that supplies the answers. It also pre-qualifies leads: founders who
read it arrive knowing what to ask for.

**The caution from the last two weeks stands and must not be dropped.** Paramount's public copy says
*"cGMP-certified, FDA-registered partner facilities."* **FDA registration satisfies TikTok Shop but
does NOT satisfy Amazon's certificate requirement** — Amazon explicitly excludes FDA inspections and
first-party or consulting audits. Conflating the two on this page would mislead the exact buyer being
courted and generate leads that die at diligence. State each marketplace's requirement separately.

### 6c. NEW — Paramount is missing from the New York listicle layer, and that layer is local now

Last week's report noted Paramount appears on no comparison roundups. This week that is specific and
worse: **Aurinutra publishes "Top 10 Supplement Manufacturers in NEW YORK" and ranks itself best
overall for New York startups.** Paramount is absent. Present instead:

- **Makers Nutrition** (Commack, NY) — 177,000 sq ft, FDA-registered, explicitly positioned on *"some
  of the lowest MOQs in the industry"* for startups and emerging brands.
- **Bactolac Pharmaceutical** (Hauppauge, NY) — 30+ years, full turnkey.
- **Gemini Pharmaceuticals** (Commack, NY), **Atlantic Essential Products**, **Halo Private Label**.

Commack and Hauppauge are ~15 minutes from Stony Brook. These are not abstract national competitors;
they compete for the same local referrals and the same "supplement manufacturer near me" intent, and
they are winning the query in public while Paramount is invisible on it.

Two distinct actions fall out, and they are among the cheapest in this report:

1. **Get listed** on the aggregator directories that rank for these queries — comanufacturers.com,
   Keychain, Inventory Ready ("Top 105 FDA-Registered Supplement Contract Manufacturers"), KokoQuest.
   These are submission forms, not link-building campaigns. Paramount's 30+ years and six-facility
   network are competitive credentials on every one of those lists.
2. **Own the geo query directly.** Paramount is a *New York* manufacturer and does not appear to have a
   page targeting *supplement manufacturer New York / Long Island / near me*. That is high-intent,
   low-volume, low-competition-from-real-manufacturers traffic, and it is defensible in a way national
   queries are not.

### 6d. Carried — the certificate question still gates the best opportunity

Unchanged and still unanswered:

> **Do any of Paramount's six partner facilities hold a current certificate from BSCG, Clean Label
> Project, GRMA, Informed Choice, NSF or USP?**

If yes, that converts into the strongest single sentence this site could publish for marketplace
sellers. If no, scope claims to facilities qualifying under the broader accepted schemes
(NSF/ANSI 455-2, NSF 173 §8, GRMA 455-2, UL, USP, SGS, Intertek, SQF, Eurofins). This gates the 6b page
and has now been open for three weeks. It is a 30-minute internal question.

### 6e. Carried forward — status unchanged

- **Low MOQ money page.** Still the highest-volume high-intent query in the category, still unbuilt,
  still gated on a business decision about what number to publish. Now with *two* NY competitors
  (Aurinutra, Makers Nutrition) explicitly marketing on low MOQ. Paramount publishes no number anywhere.
- **Creatine gummy/RTD stability post.** Strong technical differentiator; still gated on confirming
  capability plus stability data before publishing.
- **GLP-1 companion section** on `/protein-powder-manufacturing/` — protein for muscle preservation,
  fiber and electrolytes for side effects. Needs a section and internal links, not a new page. Keep
  claims nutritional, never drug-replacement.
- **Electrolyte / hydration / stick pack.** Unchanged; `/protein-powder-manufacturing/` is the template.
- **Softgels — still do not act.** Confirm in-house capability or a reliable toll partner first.
- **Tariff / domestic sourcing post.** Verify rates with a customs broker; avoid an unqualified
  "Made in USA" claim (FTC standard).
- **Regulatory watch, no action yet:** Dietary Supplement Listing Act of 2026, FDA self-GRAS reform and
  NDIN guidance, the federal state-preemption bill, NY's minors restriction. All increase brands'
  documentation burden, which favours a well-documented manufacturer — they feed 6b rather than
  justifying pages of their own.

### 6f. Existing pages worth strengthening — unchanged, all still open

- **Rows 11 and 12** (`/capsule-manufacturing/`, `/protein-powder-manufacturing/` form check) — still
  the cheapest high-value item in this report, fifth week running.
- **Titles.** Confirm the `/contact/` ↔ `/dietary-supplement/` duplicate against live HTML, then retitle
  `/contact/` for its actual job. `/testimonials/` ("Food Supplement Manufacturer | North America") and
  `/blog/` ("Blog | North America – Paramount Nutra") carry the same template bloat. Dropping
  `- Paramount Nutra` from titles already over 60 characters buys ~18 characters back.
- **The indexed PDF.** `Stock-Vegan-Greens-Paramount-PDF.pdf` still appears in `site:` results ahead of
  `/stock-formulations/`. Check for a CTA; add one or canonical/link it back.
- **FAQ blocks with FAQ schema on money pages.** Answer objections where the form is. Gummy first: MOQ,
  first-run lead time, pectin/vegan/sugar-free, stock-vs-custom cost. Add the marketplace-documentation
  question from 6a/6b to every one.
- **Internal linking.** Cost and MOQ posts should link hard into matching money pages.
- **Off-ICP:** `/boost-your-immune-system-with-nutrient-rich-foods/` is consumer-facing. No further
  investment.

### 6g. Competitor movement

- **Aurinutra (NYC)** — escalating. Now publishing the NY geo-listicle and ranking itself first on it.
- **Makers Nutrition (Commack, NY)** — newly surfaced, and the most direct local threat: large
  FDA-registered facility explicitly courting startups on low MOQ, the exact position Paramount has
  never staked.
- **The comparison-listicle layer** remains the real competitor. It is now both national (HDNUTRA,
  Matsun, CSK Biotech, SummitRx, Vitaplusinter, enzbio) and local (Aurinutra). Paramount appears on none.
- **Nobody has staked the marketplace-documentation manufacturer position** across Amazon *and* TikTok
  Shop. Labs, 3PLs and regulatory consultants are answering a question a manufacturer answers better.
  Windows like that close.

---

## 7. This week's recommended actions

Ranked by likely lead impact ÷ effort. **(carried)** marks items on prior lists that remain undone.

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | **Fix the egress allowlist** (carried ×4) — add `paramountnutra.com` and `www.paramountnutra.com` to this environment's allowed hosts. Five weeks blind. If policy forbids it, replace this routine's section 4 with an external form monitor instead of re-reporting "unverified" forever. | Critical — restores all lead-capture monitoring | 5 min |
| 2 | **Open WordPress Posts and fix WP-Cron** (carried ×3) — publish `/gummy-vs-capsule/` and `/what-cgmp-actually-means/`. August closed at zero. Fixing cron protects September. | Critical — recovers two written posts, stops the bleed | 10–20 min |
| 3 | **Check `/capsule-manufacturing/` and `/protein-powder-manufacturing/` for `gform_3`** (carried ×4). Two live money pages never once verified. Add to the monitored list either way. | High — possible live revenue leak, trivially checkable | 5 min |
| 4 | **Submit Paramount to the manufacturer directories** (6c) — comanufacturers.com, Keychain, Inventory Ready, KokoQuest. Competitors rank on these for Paramount's own geography. Rose sharply this week. | High — qualified leads plus backlinks, and defensive | 1–2 hrs |
| 5 | **Work the section 4 checklist manually** (carried) until monitoring is restored. | High — catches silent revenue loss now | 15 min |
| 6 | **Answer the certificate question (6d)** — do any partner facilities hold BSCG, Clean Label Project, GRMA, Informed Choice, NSF or USP certification? Gates #8. | Critical as an input — decides whether the best opportunity is real | 30 min internal |
| 7 | **Retarget `/what-cgmp-actually-means/` before publishing** — accepted schemes, why FDA registration is not one for Amazon, claims alignment, TikTok Shop's separate document set, the UL dropdown friction. Same effort, far better funnel position. | Very high — urgent commercial intent, already written | 1–2 hrs edit |
| 8 | **Build the marketplace-documentation page (6a/6b)** covering Amazon *and* TikTok Shop: the document table, who produces each, and the compliant-vs-non-compliant timeline. SERP held by labs and 3PLs, not manufacturers. Scope claims to what is documented. | Very high — highest-intent traffic available to this site | 4–6 hrs |
| 9 | **Build a New York / Long Island geo page** (6c). Paramount is a NY manufacturer invisible on NY queries while three Long Island competitors rank. | High — high-intent local traffic, low real competition | 2–3 hrs |
| 10 | **Retitle `/contact/`, `/testimonials/`, `/blog/`** after confirming the duplicate against live HTML. | High — resolves a regression of a previously fixed problem | 1 hr |
| 11 | **Decide the published MOQ number, then build the low-MOQ page.** Two NY competitors now market on this directly. | High — direct leads plus pre-qualification | 1 hr decision + 4 hrs page |
| 12 | **Add FAQ + FAQ schema to `/gummy-manufacturing/`**, then tablet, liquid, private label — including the marketplace-documentation question. | High — question intent where the form is | 2–3 hrs, then ~1 hr each |
| 13 | **Confirm creatine gummy/liquid capability, then write the stability post.** Hottest format in sports nutrition with a question only a manufacturer can answer. | High — differentiated, low competition | 30 min internal + 3–4 hrs |
| 14 | **Add a GLP-1 companion section to `/protein-powder-manufacturing/`** with internal links. | Medium-high — strongest-evidenced 2026 category | 2 hrs |
| 15 | **Check the indexed stock-formulations PDF for a CTA** (carried); add one or canonical it back. | Medium-high — recaptures attention already paid | 20 min |
| 16 | **Internal linking pass** (carried) — contextual CTAs from cost and MOQ posts into money pages. | Medium — converts traffic already on site | 1 hr |
| 17 | **Target drink-mix / stick-pack / electrolyte intent** — extend `/protein-powder-manufacturing/`. | Medium-high — fast-growing format, template exists | 3–4 hrs |
| 18 | **Write the domestic-sourcing / tariff post** (carried). Verify rates with a broker; avoid unqualified "Made in USA". | Medium — well-timed, diffuse intent | 3–4 hrs |
| 19 | **Audit the "food supplement manufacturer" cluster** (carried) — consolidate and 301 if GSC confirms overlap. | Medium — protects a previously fixed problem | 1 hr, pending GSC |
| 20 | **Consider Paramount-authored comparison content** to contest the listicle layer. | Medium — mid-funnel intent no service page reaches | 4–6 hrs |

Items 7, 8, 9, 11, 13, 14, 17 and 18 feed the 2-posts-per-month cadence rather than competing with it —
**once #2 makes publishing work again.**

**Re-ranked this week:** #4 (directory submissions) jumped from #12 to #4 — it was already the cheapest
lead channel here, and the discovery that a competitor ranks itself #1 on Paramount's own state while
Paramount is absent makes it urgent as well as cheap. #9 (NY geo page) is new. #8 absorbed the two
separate Amazon items into one broader marketplace-documentation page, which is a stronger asset than
either alone.

---

## 8. Data the human needs to pull

GA4 and Search Console remain inaccessible from here. Most valuable first.

**Lead capture — five weeks unverified:**
1. How many `generate_lead` events fired in the last 35 days versus the prior 35? With the routine
   blind for five weeks this is the *only* evidence the forms have worked at all. A sharp drop to zero
   on any page dates the breakage.
2. Which URLs produced those events? Traffic with zero leads across five weeks almost certainly means a
   missing or broken form.
3. Do `/capsule-manufacturing/` and `/protein-powder-manufacturing/` appear, and what traffic do they
   get? Decides whether action #3 is urgent or routine.
4. Did `/contact/` quote submissions over the last 35 days match what actually arrived in the sales
   inbox? A gap there is a notification failure, not a form failure — different fix.

**Search Console:**
5. Any impressions for **marketplace-compliance** queries — *Amazon cGMP*, *GMP certificate Amazon*,
   *NSF 173*, *supplement facts panel Amazon*, *Amazon claims alignment* — and now also **TikTok Shop**
   queries: *TikTok Shop supplement compliance*, *COA TikTok Shop*? Non-zero impressions with no
   dedicated page moves #7 and #8 to the top outright.
6. Any impressions for **geo queries** — *supplement manufacturer New York*, *Long Island*,
   *near me*, *Stony Brook*? Sizes #9 and tells you whether the local listicle is costing real traffic.
7. Do `/contact/` and `/dietary-supplement/` show impressions for the *same* queries? Confirms or kills
   the duplicate-title finding and decides #10.
8. Same across `/testimonials/` and the two "food supplement manufacturer" posts — which actually earns
   the impressions? Keep that one, consolidate the rest.
9. Any impressions for **low MOQ / minimum order quantity**, or for **creatine**, electrolyte,
   hydration, stick pack, or GLP-1 related manufacturing queries? Sizes #11, #13, #14 and #17.
10. **Are `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` in the index at all?** URL Inspection
    settles in seconds what public search can only infer.
11. Any new Coverage / Page Indexing errors since last month, particularly pages dropping out?

**Cadence and infrastructure — do this one first:**
12. WordPress Posts screen: are both posts "Missed schedule"? **Is WP-Cron firing at all?** A month of
    consecutive failures says it is not. If `DISABLE_WP_CRON` is set or the host's cron is not hitting
    `wp-cron.php`, a real server cron job is the fix — otherwise September's posts will miss too.

**Internal, not a data pull — gates the best opportunities:**
13. Do any partner facilities hold **BSCG, Clean Label Project, GRMA, Informed Choice, NSF or USP**
    certification (Amazon Fast-Track list), or any other accredited third-party scheme, and can a
    customer be handed that certificate for their ASIN? Gates 6b and action #8.
14. **Which facilities hold ISO or HACCP certification, and can Paramount hand a customer FDA facility
    registration proof on request?** This is the TikTok Shop requirement specifically and is a
    different question from #13. Gates 6a.
15. Can Paramount manufacture creatine in gummy or RTD format **with stability data**? Gates #13.

---

## Methodology note

Sections 6 and 7 derive from Google's public index and third-party trade sources via web search — the
only research channel reachable from this environment. Indexed titles can be stale and say nothing
about HTTP status, redirects, meta descriptions, page content, or form presence. **No claim in this
report constitutes verification that any form, PDF, or analytics tag is working.** Absence from search
results is strong but not conclusive evidence a post is unpublished — item 10 in section 8 settles it
definitively. Regulatory, marketplace-policy and tariff details are summarised from trade press and
secondary sources and must be confirmed against primary sources before being published as
customer-facing claims; the TikTok Shop and Amazon document requirements in 6b especially, since they
change without notice. Action #1 is what turns next week's report back into a measurement rather than
an inference.
