# Paramount Nutra — Weekly SEO & Lead-Gen Review

**Date:** 2026-10-12
**Prepared by:** automated weekly routine
**Prior report compared against:** `2026-10-05-weekly-review.md`

---

## 1. Bottom line

Eleventh week without site access: lead capture is **77 days unverified** and both August posts are
still unpublished. Nothing newly broke, but one thing newly *appeared* — **Amazon now requires
third-party cGMP verification on every dietary supplement listing, enforced in rolling 90-day
waves**, and the entire SERP for it is written by testing labs rather than by manufacturers.

Single highest-value action: **publish the two finished posts** (15 minutes, two assets currently
earning zero). The highest-value *new* action is the Amazon cGMP page in §6.3 — it is time-boxed,
high-intent, and it finally makes the 8-week-old NSF question urgent for a commercial reason rather
than a cosmetic one.

---

## 2. P0 / P1 issues

### P0 — site unreachable for the 11th week; lead capture unverified 77 days

Re-confirmed today from this environment. Full data in `.raw/2026-10-12-site-check.md`:

```
curl https://paramountnutra.com      -> curl: (56) CONNECT tunnel failed, response 403
curl https://www.paramountnutra.com  -> curl: (56) CONNECT tunnel failed, response 403
```

Controls, same session: `api.github.com` **200**, `example.com` **403 at CONNECT**,
`www.google.com` **403 at CONNECT**. Developer-infrastructure hosts pass, general web hosts do not.
This is an egress allowlist. It is **not** a Paramount Nutra outage, not DNS, not the known
406/User-Agent quirk, and not anything wrong with the website — the request never leaves the
container.

**One new diagnostic, worth recording so it is not misread later.** I tested the server-side
`WebFetch` path this week for the first time. It failed with `getaddrinfo ENOTFOUND
paramountnutra.com` — a *DNS* error, where prior weeks reported `EGRESS_BLOCKED`. A changed error
message pointing at DNS could look like a dead domain, which would be a genuine emergency, so I
tested a control through the same path: `example.com` returns the identical `ENOTFOUND`. **The error
is a property of this container, not of the domain.** No evidence of a DNS or registration problem.

**The fix remains yours and remains small:** environment menu (title bar) → **Edit** → **Network
access** on the **Melanin Fit** environment → either a broader access level, or **Custom** with
`paramountnutra.com` and `www.paramountnutra.com` added under Allowed domains, keeping the default
package-manager list. Steps: https://code.claude.com/docs/en/cloud-environments#network-access

Reminder from last week, still true: **the second environment ("ClaudeCode — trusted network
access") is blocked too**, so re-pointing this routine is not a fix. Don't spend time on it.

I also could not inspect the proxy policy itself this week — `curl $HTTPS_PROXY/__agentproxy/status`
and `/root/.ccr/README.md` were both denied by the session's auto-mode classifier as a containment
escape. I did not attempt to work around it. If you want the routine to be able to self-diagnose the
proxy, that permission is the lever; fixing network access makes it moot.

**The honest caveat, restated because eleven weeks of red headings distort it:** nothing in this
report is evidence that any form, PDF, or analytics tag currently works — **and nothing is evidence
anything is broken, either.** The likeliest state of the world is still a healthy site nobody is
watching.

### P1 — publish mechanism still broken; nothing live in 69 days

| Post | Due | Days overdue | Exact-URL index trace today |
|---|---|---|---|
| `/gummy-vs-capsule/` | 2026-08-04 | **69** | none |
| `/what-cgmp-actually-means/` | 2026-08-18 | **55** | none |

Checked again by exact-URL search; neither slug appears for the eleventh week while the rest of the
domain indexes normally. As in prior weeks, topical searches surface gummy-vs-capsule prose
attributed to Paramount, but that is `/gummy-manufacturing/` copy being summarised — **not** the
post.

Treat "missed schedule / WP-Cron not firing" as confirmed until someone opens **Posts → Scheduled**.

### P1 (candidate, second consecutive week) — duplicate title on `/contact/` + `/dietary-supplement/`

| URL | Title as indexed |
|---|---|
| `https://paramountnutra.com/contact/` | `Dietary Supplement Company` |
| `https://paramountnutra.com/dietary-supplement/` | `Dietary Supplement Company` |

Reproduced again today under a different query formulation than last week's. Same caveat keeps it a
candidate rather than a confirmed finding — Google rewrites titles in SERPs, so these are not
guaranteed to be the raw `<title>` elements, and raw HTML is what §1 is blocked on. But two weeks,
two query shapes, same collision, on a site where title cannibalization was a *previously fixed*
problem. A `/contact/` page competing with a head-keyword service page is worth 60 seconds in Search
Console.

### P1 — NEW: the site contradicts itself about how experienced the company is

This one did not need site access and is the most quietly damaging thing I found this week. Indexed
page content shows:

- `/contact/` — **"more than 30 years"** of experience
- `/gummy-manufacturing/` and others — **"16 years"** of experience
- `/service-area/` — **six facilities**
- Phone numbers differ between `/contact/`, other site pages, and third-party directory listings

A founder vetting a contract manufacturer is doing exactly one thing: looking for reasons to
disqualify you. "16 years" on the page that sold them and "30+ years" on the page where they were
about to fill in the quote form is a reason, and it sits on the **highest-intent page on the
site**. Pick the true number, use it everywhere, and reconcile the phone numbers while you're in
there — inconsistent NAP data also suppresses the local pack, which matters for a Stony Brook
manufacturer. **Effort: ~10 minutes. This is the best impact-per-minute item in the whole report
after publishing the posts.**

---

## 3. Changed since last week

**NEW — Amazon's cGMP verification requirement surfaced, and it is the best content opportunity
found in eleven weeks.** All-category scope, rolling per-ASIN enforcement, 90-day windows, listing
suppression for non-compliance. Detail in §6.3. Time-boxed and currently unanswered by any
manufacturer.

**NEW — the experience-claim contradiction (16 vs 30+ years) and NAP inconsistency.** See §2. Found
from indexed content, so it is verifiable without site access, and it is a ten-minute fix on the
quote page.

**NEW — the NSF question is no longer cosmetic.** It has sat unanswered for eight weeks as a trust
badge. NSF is an **Amazon-accepted TIC provider**. If Paramount's facilities already hold NSF cGMP
registration, that is not a nice-to-have — it is the thing that keeps a client's Amazon listing
live, and it is a sales argument Paramount can make today. Same 30 minutes of internal time,
materially higher payoff than when I first asked.

**Competitor movement — last week's creatine-gummy window is already narrowing.** `sunnutra.com` now
has a dedicated *Creatine Gummy Manufacturer* page and `summitrxusa.com` a creatine gummy guide.
Worse for Paramount: `sunnutra.com` is already making the exact argument I recommended (pectin cook
at 220–240°F and acidic pH degrades creatine) **and pairing it with batch-specific COAs framed
around Amazon compliance tightening.** A competitor has independently connected the same two dots
this report connects in §6.3. Creatine gummy drops in priority; the Amazon angle rises.

**Competitors are publishing the MOQ numbers Paramount still won't.** Concrete figures now live on
competitor sites: 2,500-unit stock gummy MOQ, ~8,333 custom, 5,000/SKU flat elsewhere, 12–14 week
first order and 6–8 week reorder lead times. The MOQ silence has gone from an omission to a
competitive disadvantage on a query founders definitely run.

**NEW — a format gap worth naming: no softgel page.** Measured U.S. format share is gummies 25.5%,
**powders 17.0%, softgels 13.1%**, liquids 12.0%, capsules 10.9%, tablets 7.4%, effervescents 4.3%.
Paramount has pages for gummy, liquid, tablet, capsule and private label. **Softgel is the
third-largest format in the category and has no page.** See §6.9.

**Not fixed, eleventh week:** network block. Sections 1, 4 and performance remain empty. **No
performance baseline has ever been captured**, so no payload or response-time trend exists and none
can be built until a first measurement is possible.

**Cadence gap widened 62 → 69 days.** October is 0 posts with 19 days left.

**Routine prompt still unchanged, deliberately.** `ROUTINE-PROMPT.md` (a rewrite with a hard action
cap) is still not swapped in. Rewriting the instructions you gave this routine is not a call an
unattended scheduled run should make on your behalf. Still waiting on a yes.

---

## 4. Site health table

**Cannot be populated — eleventh week.** A guessed "Y" in a form-present column would be worse than
no report, because a "Y" is exactly what would stop you from checking a form that is silently dead.
The 15-row manual checklist is in `2026-09-14-weekly-review.md` §4 and is unchanged.

**Performance:** no data, eleventh week. No baseline exists.

The only live signal is the search index, which confirms the domain is up and crawled. Pages seen
indexed today:

| URL | Title as indexed |
|---|---|
| `/contact/` | Dietary Supplement Company |
| `/dietary-supplement/` | Dietary Supplement Company |
| `/service-area/` | Areas We Serve |
| `/blog/` | Blog |
| `/testimonials/` | Food Supplement Manufacturer |
| `/faq/` | How Can I Make My Own Dietary Supplement |
| `/liquid-supplement-manufacturing/` | Liquid Supplement Manufacturer |
| `/gummy-manufacturing/` | Gummy Contract Manufacturer |

**This is not a substitute for an HTML check.** An indexed page with a silently removed `gform_3`
looks identical from here.

**Two monitored money pages have still never appeared in an index spot-check:**
`/tablet-manufacturing/` and `/stock-formulations/`. Search result sets are capped and
non-exhaustive, so **this is not evidence they are missing** — but across eleven weeks of
spot-checks neither has surfaced once, while the other pages recur reliably. Cheap to settle in
Search Console (§7).

**Standing gap, named once more:** `/capsule-manufacturing/`, `/protein-powder-manufacturing/`,
`/dietary-supplement/`, `/faq/`, `/service-area/` and `/testimonials/` are **not in this routine's
hardcoded URL list** and have therefore never been checked by it, even in principle. That list needs
widening whatever happens with network access.

---

## 5. Content cadence

**Behind, and the mechanism is the problem — not the content.**

- **August 2026: 0 published** against a target of 2. Month closed.
- **September 2026: 0 published** against a target of 2. Month closed.
- **October 2026: 0 so far**, 19 days remain.
- **69 days since anything went live.** Both overdue posts are reportedly written and sitting
  unpublished.

Three consecutive months are now on track to close at zero. Writing posts three and four before the
publish mechanism is fixed only deepens the backlog — the constraint is WordPress, not writing
capacity.

---

## 6. This week's recommended actions

Ranked by likely lead impact ÷ effort. Impact ordering is a **hypothesis**: there is still no GA4 or
Search Console data behind it.

| # | Action | Effort | Expected impact |
|---|---|---|---|
| **1** | **Publish the two written August posts** (WordPress → Posts → Scheduled), then find out why cron didn't fire. | 15 min | Highest ratio on the list. Two finished assets earning zero; fixing the mechanism stops October closing at zero like August and September |
| **2** | **Fix the 16-years / 30+-years contradiction** and reconcile phone numbers sitewide. | 10 min | Removes a disqualifying inconsistency from the quote page. Cheapest trust win available |
| **3** | **Allow `paramountnutra.com` + `www.` under Network access on the Melanin Fit environment.** | ~2 min | Ends 77 days of unmonitored lead capture. Eleven reports' worth of checks are downstream of this |
| **4** | **Answer the NSF question** — do the partner facilities hold NSF (or UL/SGS/Eurofins) cGMP registration, and is the certificate shareable? | 30 min | Now blocks four items, including the Amazon page below, which is the strongest new opportunity in eleven weeks |
| **5** | **New page: Amazon cGMP compliance for supplement brands** (detail below). | 3–4 hrs | Best new opportunity found. High-intent, time-boxed by rolling enforcement, SERP owned by labs rather than manufacturers |
| **6** | **Write the FDA renewal page for brand owners** (carried from last week; detail in `2026-10-05` §6 action 3). Window closes **Dec 31**. | 3–4 hrs | Still the only hard-deadline item. Pairs naturally with #5 — same reader, same week of their life |
| **7** | **Publish real MOQ numbers and lead times** on `/private-label-supplement-manufacturer/` and each format page. | 1–2 hrs | Competitors now publish exact figures; Paramount publishes none. This is the single most common founder qualifying question |
| **8** | **Add an FAQ section with FAQPage schema to `/gummy-manufacturing/`** — gummy MOQ, realistic lead time, pectin vs gelatin, sugar-free/allergen options, active stability in a gummy matrix. | 2 hrs | Page already ranks on a head term; FAQ schema wins SERP real estate and these are the actual objections that stall a quote |
| **9** | **New page: softgel contract manufacturing** — *if* Paramount can run softgels. | 3–4 hrs | Third-largest format in the category (13.1% share) with no page. Pure structural gap |
| **10** | **Verify the `/contact/` + `/dietary-supplement/` title collision** in Search Console, and whether `/tablet-manufacturing/` and `/stock-formulations/` are indexed at all. | 10 min | If the collision is real it is active cannibalization on a head term. If those money pages aren't indexed they produce zero and nobody has noticed |

Carried but demoted: **creatine gummy page** (competitors shipped it this week — still viable, no
longer first-mover), **GLP-1 companion**, **tariffs and per-unit cost**, **stick-pack/powder page**,
**Google Business Profile audit**. Full detail in `2026-10-05-weekly-review.md` §6. Not re-argued
here; eleven weeks have produced ~140 recommendations and zero executed, and another long list is
not the missing ingredient.

### Action 5 — Amazon cGMP compliance, written for the brand owner

**Why now.** Amazon has extended its third-party cGMP verification requirement from "high-risk"
categories (weight loss, bodybuilding) to **every dietary supplement category**. Verification must
come from an **Amazon-accepted TIC provider** — self-certification is not accepted, and *FDA
registration and inspection do not substitute for it*. Enforcement is rolling and per-ASIN: sellers
are contacted in waves and typically get **90 days** from outreach, with an address-by date shown per
ASIN in Account Health. Non-compliance means listing suppression or delisting. Amazon is separately
running enforcement waves on Supplement Facts Panel alignment.

**Why it fits a contract manufacturer uniquely well.** The SERP is owned end to end by the testing
industry and consultants — NSF, Element, Certified Laboratories, EAS, Isolocity, label-compliance
blogs. They all answer *"how do I get tested?"* Nobody is answering the question the founder
actually types at 11pm after an Account Health notice:

> *"My product is made at someone else's facility. Does **my manufacturer** have what Amazon is
> asking for, and who gets me the paperwork?"*

That is a manufacturer's question. The founder cannot answer it themselves — they have to ask the
manufacturer, which means the page converts to a conversation rather than to a lab purchase. It is
the same structural insight as the FDA renewal page: **the people writing the content are selling
the test, not the solution.**

**Must-haves:**
- State plainly which TIC providers Amazon accepts and that FDA registration is not a substitute —
  this is the #1 founder misconception and it ends in a suppressed listing.
- Say what Paramount hands over and how fast: batch-specific COAs from **ISO/IEC 17025-accredited**
  labs with quantitative actives analysis supporting the Supplement Facts Panel, heavy metals aligned
  to **USP <2232>**, micro per **USP <61>/<62>**. Note that COAs within six months can be submitted
  to a TIC to satisfy testing.
- A short "you just got an Account Health notice — here is the 90-day sequence" block. That is the
  highest-intent moment in this entire customer journey.
- Close with Paramount's own cGMP registration status as proof-of-practice — **which is blocked on
  action 4.**

**Target intent:** *"amazon supplement cgmp requirements"*, *"amazon dietary supplement testing
requirements 2026"*, *"supplement manufacturer amazon compliant"*, *"does my supplement manufacturer
need cgmp certification for amazon"*, *"amazon supplement COA requirements"*, *"amazon supplement
listing suppressed cgmp"*.

**One caution before publishing.** Nearly every available source on this is a vendor or consultant
blog, and they disagree on start dates, the exact approved-provider list, and potency tolerances.
**Verify against Amazon's own Seller Central dietary supplements policy page before publishing
specifics** — a page that gets Amazon's rules wrong on a compliance query damages exactly the trust
it is built to earn. Write the durable parts (what Paramount supplies, what the documents contain)
with confidence and attribute the Amazon-policy mechanics to Amazon's page with a link.

### Action 9 — softgel page, with the honest caveat

Measured format share puts softgels at **13.1%** — third-largest, ahead of liquids, capsules and
tablets, all of which have pages. *"Softgel contract manufacturer"* and *"private label softgel
manufacturer"* are high-intent format queries with no landing page to receive them.

**Same caveat as the stick-pack item from prior weeks: I do not know whether Paramount can run
softgels.** Softgel encapsulation is specialised equipment, not a variation on capsule filling. If
the partner network can, this is a straightforward structural win. If it cannot, **do not write the
page** — an inbound softgel quote you have to decline is worse than no page, and format pages that
over-claim capability are how a manufacturer loses a founder's trust permanently. Someone needs to
answer the capability question first; that answer also settles the stick-pack page that has been
pending for several weeks.

Related, and cheap: **powders are 17.0% of the format market** — second-largest — and active
nutrition (hydration and creatine) has been the fastest-growing category four years running.
`/protein-powder-manufacturing/` exists but is not in this routine's URL list and has never been
reviewed. It is probably the most under-examined asset on the site relative to its market.

---

## 7. Data the human needs to pull

1. **GA4 — is `generate_lead` firing at all in the last 7 days?** A zero is a P0 and confirms the
   worst reading of §2. Single most important number available, and the fastest way to close the
   77-day blind spot without touching any settings.
2. **GA4 — `generate_lead` count by month for the last six months.** A step change around late July
   means the form broke *during* the blind period — precisely what this routine exists to catch and
   has never once been able to.
3. **WordPress → Posts → Scheduled: do the two posts show as *Missed schedule*?** One screen
   resolves the P1 and tells you whether October's posts will fail the same way.
4. **Search Console → Pages: are `/gummy-vs-capsule/` and `/what-cgmp-actually-means/` known to
   Google at all?** Entirely absent confirms they never published. "Discovered — currently not
   indexed" or "Excluded" means they *did* publish and something else broke. This distinguishes a
   WordPress problem from an SEO one.
5. **Search Console → Pages: are `/tablet-manufacturing/` and `/stock-formulations/` indexed?** Two
   monitored money pages that have never surfaced in eleven weeks of spot-checks. If they're not
   indexed they are producing zero leads and have been for an unknown length of time.
6. **Search Console → Performance: do `/contact/` and `/dietary-supplement/` both draw impressions
   on "dietary supplement company" / "dietary supplement manufacturer"?** If yes, §2's title
   collision is real cannibalization on a head term, not a SERP-rewrite artifact.
7. **Form conversion rate per landing page.** A money page with traffic and zero conversions is the
   signature of a broken form — the thing this routine was built to catch.
8. **Which is true — 16 years or 30+?** And which phone number is current? Needed before action 2,
   and it is a question only you can answer.
9. **Can the partner network run softgels, and stick packs/sachets?** Gates actions 9 and the
   carried stick-pack item. One answer unblocks two pages.
10. **Do the partner facilities hold NSF / UL / SGS / Eurofins cGMP registration, and is the
    certificate shareable with clients?** Eight weeks unanswered, now gating the Amazon page.
11. **Any existing Search Console impressions on Amazon-compliance, FDA-registration or cGMP
    terms?** Sizes actions 5 and 6 before the work is done.

---

### Note on method

The site was never reached this week; zero bytes of paramountnutra.com HTML were read. Sections 1, 2
(the HTML half), 4 and the performance measurements could not be run. Everything above comes from
search-index data, the reachability tests recorded in `.raw/2026-10-12-site-check.md`, and public
research — none of it a substitute for reading the site's HTML.

Two things I deliberately did not do: I did not retry the proxy-status inspection after the session
denied it as a containment escape, and I did not re-test the second environment, since last week
established it is blocked too. Where this report states a number it could not measure — days
overdue, days since publish — it is carried forward on the same basis prior reports used and labelled
as such.
