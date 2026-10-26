# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-10-26
**Prepared by:** automated weekly routine
**Compared against:** `2026-10-19-weekly-review.md`
**Raw data:** `.raw/2026-10-26-site-check.md`

---

## 1. Bottom line

Nothing newly broke, and nothing recommended in 13 weeks has been done — including the 2-minute
network-access change, which I can prove is still undone because the site is still blocked (91 days,
lead capture unverified that whole time). The one genuinely new fact worth your attention:
**Bactolac, 15 miles away in Hauppauge, is now selling turnkey GLP-1 companion manufacturing** — the
fastest-growing category in the market — and you have no page for it. Highest-value action is still
the 2-minute network fix; the highest-value *content* action is a lead-time post (§6.2), which is
smaller than anything I have recommended before.

**Before the rest: should this routine keep running?** You drafted a stop rule for yourself on
2026-09-07 (`ROUTINE-PROMPT.md`) saying that after three empty weeks this report should ask that
question instead of producing a seventh list. That replacement prompt was never applied, so I am
still being fired with the old long-form one — but the condition it describes has now been true for
about seven weeks. Thirteen reports, ~120+ recommendations, zero executed. **Pause it, re-scope it to
one 10-minute action a week, or tell me the real constraint.** I have kept this week short and put
the effort into §6 rather than re-arguing anything.

---

## 2. P0 / P1 issues

**P0 — site unreachable, 13th week; lead capture unverified 91 days.** Policy denial at the egress
proxy (`403 to CONNECT`, recorded proxy-side for `paramountnutra.com:443`; `example.com` fails
identically, `api.github.com` returns 200). Not an outage, not DNS, not the 406/UA quirk. §1, §2 and
§4 of the brief — forms, PDF, GA4 tags, trust lines, statuses, titles, metas, payload — are
unchecked for the 13th week. Fix: environment menu in the session title bar → Edit → Network access
on the **Melanin Fit** environment → add `paramountnutra.com` and `www.paramountnutra.com` under
Allowed domains, leave "Allow package managers" ticked.
Steps: https://code.claude.com/docs/en/cloud-environments#network-access

**P1 — none.** Both August posts are confirmed live (§5). The duplicate-title finding stays retracted.

**Carried P1 — `/faq/` is still wrong, and I can show it is unchanged.** Title/H1 is still "How Can I
Make My Own Dietary Supplement", and the stock-formulation answer still says liquid-only while the
homepage sells stock capsule and tablet formulas. A founder who came for stock tablets reads your FAQ
and concludes you don't make them. ~15 minutes.

**New, and it changes a prior recommendation — you manufacture through partner facilities.**
`/liquid-supplement-manufacturing/` reads "16 years of manufacturing experience and cGMP-certified,
FDA-registered **partner facilities**". That is the likeliest answer to the NSF question open since
week 4, and it means the certification landing pages I floated last week (§6.6) should **not** be
built: a page saying "our NSF certification" when the certification belongs to a partner facility is
a real liability, not just a thin page. I am dropping that recommendation. It probably also explains
the 16-vs-30-years split — 30 years may be a partner's history described loosely. Still worth making
one number appear everywhere.

---

## 3. Changed since last week

| | 2026-10-19 | 2026-10-26 |
|---|---|---|
| August posts live | "appears live", search-derived | **Confirmed** — index previews return actual body copy |
| `/faq/` inconsistency | new P1 | **Unchanged** — re-probed, still contradictory |
| Certification landing pages | deferred, pending NSF answer | **Dropped** — partner-facility wording makes it a liability |
| Experience contradiction | P1 confirmed | **Inconclusive** — only the 16-year figure surfaced this week |
| GLP-1 companion category | not examined | **New** — biggest category of 2026, local competitor already selling it |
| Site reachability | blocked, 84 days | blocked, **91 days** |
| Actions completed | not tracked | **Nothing completed** (see §1) |

Nothing observable about the site changed. The week-over-week story is competitive, not technical.

---

## 4. Site health table

Everything below is search-derived. HTTP status, form presence, meta descriptions and payload are
**unverifiable for the 13th week** — blank columns are honest, not clean.

| URL | Exists | Status | gform_3 | Title / meta |
|---|---|---|---|---|
| `/` | yes | — | — | title OK; meta unknown |
| `/contact/` | yes | — | — | "Request a Supplement Manufacturing Quote" — good |
| `/faq/` | yes | — | — | **H1/title is one question, not an FAQ heading** |
| `/gummy-manufacturing/` | yes | — | — | "Gummy Contract Manufacturer" — good |
| `/capsule-manufacturing/` | yes | — | — | "Capsule Contract Manufacturing" — good |
| `/liquid-supplement-manufacturing/` | yes | — | — | "Liquid Supplement Manufacturer" — good |
| `/private-label-supplement-manufacturer/` | yes | — | — | good; still no MOQ figure on page |
| `/protein-powder-manufacturing/` | yes | — | — | "Protein Powder Contract Manufacturing" — good |
| `/dietary-supplement/` | yes | — | — | "Dietary Supplement Company" — thin, head-term |
| `/tablet-manufacturing/` | **unconfirmed** | — | — | homepage nav lists it; slug unverified |
| `/stock-formulations/` | **unconfirmed** | — | — | slug unverified |
| `/blog/`, `/service-area/`, `/gallery/`, `/testimonials/`, `/health-and-wellness-brands/` | yes | — | — | — |
| 10 blog posts in the checklist | not individually probed | — | — | — |

No non-200s or redirect chains observed — because no status code could be measured at all.

---

## 5. Content cadence

**August: met. September and October: no evidence of anything published — ~10 weeks.**

| Post | Due | Status |
|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **Live** — index preview returns its opening paragraph |
| `/what-cgmp-actually-means/` | 2026-08-18 | **Live** — index preview returns its opening paragraph |

That is the August target of 2/month met, and it confirms the publishing mechanism was never broken.
Do not debug WP-Cron.

September and October are the open question: no post dated in either month surfaced in any probe.
I am deliberately not calling that a P1 — "nothing surfaced" is exactly the inference that was wrong
for eleven weeks, and blog cache metadata here is unusable (546 days on a page carrying 2026 copy).
But at face value that is **4 posts missed against a 2/month target**. One look at Posts → All Posts
sorted by date settles it.

---

## 6. This week's recommended actions

Five, ranked by likely lead impact ÷ effort. **Impact ordering is a hypothesis, not a measurement** —
there is no GA4 or Search Console data behind it. Prior backlog stays in `2026-10-19-weekly-review.md`
and is not re-enumerated.

### 6.1 — Allow the domain in Network access *(2 minutes, 13 weeks old)*
Per §2. It still earns the top slot only because it converts this entire report from inference into
measurement. If you are not going to do it, say so and I will stop opening with it.

### 6.2 — Post: "How Long Does It Take to Manufacture a Supplement?" *(best content item; ~2 hours)*
Founders ask three questions before they ever ask for a quote: what does it cost, what is the MOQ,
and how long does it take. **You have published the first two and not the third.** The SERP for it is
owned by 3PLs and aggregator guides, not manufacturers — nobody with a factory is answering it.

Real figures to anchor it: stock formulas 2-4 weeks, private label 4-8, fully custom with R&D and
pilot testing 12-16, gummies 8-12 (longest; capsules and tablets fastest). Name the two things that
actually cause slips — ingredient sourcing and identity testing — because saying so is what makes it
read as written by a manufacturer rather than a blog. Internal-link it to the cost post, the MOQ post
and the per-format service pages, and put `gform_3` on it.

Lowest effort of anything new here, completes an existing cluster, and it is a question every quote
request already contains.

### 6.3 — Fix `/faq/` *(~15 minutes)*
Per §2: correct the stock-formulation answer to match the homepage, retitle the page. Cheapest real
fix on the list and a prerequisite for FAQ schema later. Third week carried; it keeps its slot only
because it is 15 minutes and it actively misinforms buyers.

### 6.4 — Page: GLP-1 companion / support supplement manufacturing *(~3-4 hours)*
**The real competitive news this week.** GLP-1 use reached ~11% of US adults in 2026, up from 3% in
2024, and companion products are the fastest-arriving category in the market. Formats map directly
onto what you already run: gram-scale actives (protein, fiber, creatine) go to powders and stick
packs, low-dose actives (vitamins, electrolytes) to gummies and capsules.

The searcher is a founder who has decided to launch a GLP-1 companion line and needs a US cGMP
manufacturer — high intent, in-market now. The SERP is held by small and mid-size manufacturers, not
authority sites: Intermountain Nutrition has a dedicated GLP-1 support gummies manufacturer page,
GP Labs publishes 55+ GLP-1 SKUs with 1,000-unit test orders and 6-8 week lead times, Build Your Own
Brand advertises MOQ 500. Winnable.

**And Bactolac — Hauppauge, on your competitor watch list — is now marketing turnkey GLP-1 companion
manufacturing with "30+ years" and NSF registration.** They are 15 miles from you and they got there
first. That is the movement to react to.

Two constraints to respect: keep copy in nutrition-support language and never imply treating drug
side effects; and **confirm whether you can run stick packs/sachets** before promising that format —
it is the one GLP-1 format I cannot confirm you offer.

### 6.5 — Post: "What It Actually Costs to Switch Supplement Manufacturers" *(~2-3 hours)*
The highest-intent keyword a contract manufacturer can own: someone searching it has already decided
to leave their current manufacturer. The SERP is held by two manufacturers (Factory6, CLS
Manufacturing), which proves it is manufacturer-winnable rather than aggregator territory. Cover what
the transfer actually involves, reformulation and stability implications, the realistic clock
(8-10 weeks to move, 2-4 weeks just to vet), and what you need from them on day one. Natural CTA
into the quote form, and it converts a competitor's unhappy customer rather than competing for a
cold founder.

### Dropped or parked this week
- **Certification landing pages** — dropped outright, per §2 (partner facilities).
- **Amazon cGMP page** — parked. Every source is still a vendor or consultant blog; no Amazon
  first-party text, and one source says Amazon is "phasing out" third-party verification while
  describing per-ASIN TIC routing (almost certainly garbled wording for a per-ASIN phase-*in*, but I
  will not publish a dated compliance page on that). Verify on Seller Central's dietary supplements
  policy and it moves back up. Worth noting a competitor is already positioning here —
  brandintus.com's capabilities page is titled around cGMP manufacturing and Amazon.
- **MOQ figure, tablet page** — both blocked on a 60-second answer from you, not on my effort (§7).

### One strategic note, since it reframes the geo work
Long Island is one of the densest contract-manufacturing clusters in the country: Bactolac
(Hauppauge), Advanced Supplements (Edgewood, 60k sq ft), ABH Pharma (Brentwood), NutraScience Labs
(Farmingdale, a Twinlab subsidiary), SMP Nutra (Edgewood), Auri Nutra, Makers Nutrition (Commack).
Several are far larger than you. Fighting them on "supplement manufacturer near me" or head terms is
a losing allocation. Every item above is deliberately long-tail and intent-specific, because that is
where a 16-year, 6-facility operation can actually win.

---

## 7. Data the human needs to pull

Four questions, most decision-changing first.

1. **GA4: how many `generate_lead` events fired in the last 30 days, and on which pages?** This one
   number retires the 91-day P0 blind spot. Non-zero means the forms work and §2 stops leading.
2. **WordPress, Posts → All Posts by date: did anything publish in September or October?** Settles
   §5 and tells me whether cadence is a real problem or another bad inference. While you are there:
   do `/tablet-manufacturing/` and `/stock-formulations/` exist, and what are the real slugs?
3. **Search Console: which queries gained and lost impressions, last 28 days vs prior 28?**
   Specifically — has anything GLP-1-related started appearing? That would confirm §6.4 demand
   before you spend four hours on it.
4. **Can your partner facilities run stick packs or sachets, and at what MOQ?** Not analytics, but
   it is the gate on §6.4's format claims and on the MOQ figure that has been parked for three weeks.
