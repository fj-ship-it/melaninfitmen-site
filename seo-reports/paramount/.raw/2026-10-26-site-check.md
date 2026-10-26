# Raw reachability + search data — 2026-10-26

Run from the **Melanin Fit** environment, ~11:11-11:35 UTC.

## 1. curl (Bash tool) — egress proxy

```
$ curl -sS -A "<Chrome 126 UA>" https://paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403     -> HTTP 000  time 0.207706s

$ curl -sS -A "<Chrome 126 UA>" https://www.paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403     -> HTTP 000
```

## 2. Controls, same session, same tool

| Host | Result |
|---|---|
| `https://example.com` | `curl: (56) CONNECT tunnel failed, response 403` -> 000 |
| `https://api.github.com` | **200** |

Signature unchanged from weeks 1-12. Developer-infrastructure hosts pass, general web hosts are
refused at CONNECT. Not a Paramount outage, not DNS, not the 406/UA quirk.

## 3. Proxy status endpoint — names the cause explicitly

`curl -sS "$HTTPS_PROXY/__agentproxy/status"` → `recentRelayFailures`:

```
{ "kind": "connect_rejected",
  "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host": "paramountnutra.com:443" }
```

Same entry for `example.com:443`. `selective: false`. This is a policy denial recorded
proxy-side — the request never leaves the container.

## 4. WebFetch (server-side path)

| URL | Result |
|---|---|
| `https://paramountnutra.com/` | `getaddrinfo ENOTFOUND paramountnutra.com` |
| `https://paramountnutra.com/sitemap.xml` | `getaddrinfo ENOTFOUND paramountnutra.com` |

Unchanged from weeks 10-12.

## 5. Search-derived page facts (extended mode only — standard mode cannot surface this domain)

| Page | Observation |
|---|---|
| `/faq/` | Title still **"How Can I Make My Own Dietary Supplement"**; stock-formulation answer still liquid-only, still contradicts homepage capsule+tablet. **Unchanged from 10-19.** |
| `/liquid-supplement-manufacturing/` | "16 years of manufacturing experience and cGMP-certified, FDA-registered **partner facilities**" |
| `/contact/` | Title "Request a Supplement Manufacturing Quote". Local (631) 259-6996, toll-free (888) 904-6977, fax (631) 229-9693, info@paramountnutra.com, M-F 9-5 EST, "respond within one business day". 30-year claim did **not** surface this week; 16-year figure did. Inconclusive. |
| `/private-label-supplement-manufacturer/` | Still no MOQ figure; "minimums typically lower than custom runs" |
| `/blog/` | Index previews confirm opening body copy of **both** August posts (see §6) |
| `/tablet-manufacturing/` | Still unconfirmed as a URL. Homepage nav lists "Tablet Manufacturing" under What We Offer. |
| `/stock-formulations/` | Still unconfirmed as a URL. |

Directory listings: "16 years", "6 facilities", "gummies, capsules, tablets, powders & liquids".

## 6. August posts — now confirmed live with body copy

Stronger evidence than 10-19 (which had index titles only). Index previews returned actual opening
sentences:

- `/gummy-vs-capsule/` — "Gummy vs. Capsule: Choosing a Delivery Format for Your Product. Every
  founder hits this decision early: should your product be a gummy or a capsule?"
- `/what-cgmp-actually-means/` — "What cGMP Actually Means (and How to Verify a Manufacturer's
  Claims)... every supplement manufacturer's website says 'cGMP'... founders skip past the term."

Blog index also surfaced "How to Start a Supplement Brand in 2026: A Manufacturer's Playbook" and
an MOQ post. **No post dated September or October surfaced in any probe.** Cache-age metadata read
546 days on a page carrying 2026 copy — unusable, so absence here is weak evidence, not proof.

## 7. Competitive / market data gathered

| Finding | Source class |
|---|---|
| GLP-1 use 11% of US adults 2026, up from 3% in 2024 (Gallup, cited) | trend report |
| GLP-1 companion private-label MOQs ~5,000-25,000 units/SKU | vendor |
| GP Labs: 55+ GLP-1 SKUs, 1,000-unit test order, custom from 3,000, 6-8 wk lead time | vendor self-report |
| Build Your Own Brand: GLP-1 MOQ 500 | vendor self-report |
| Intermountain Nutrition: dedicated "GLP-1 Support Gummies Manufacturer" page | competitor page |
| **Bactolac (Hauppauge NY)**: now markets turnkey GLP-1 companion manufacturing, "30+ years", NSF-registered | competitor page |
| Lead times: stock 2-4wk, private label 4-8wk, custom 12-16wk, gummies 8-12wk | multiple vendor guides |
| Switching manufacturers: 8-10wk typical; 2-4wk just to vet | multiple vendor guides |
| Long Island cluster: Bactolac (Hauppauge), Advanced Supplements (Edgewood, 60k sqft), ABH Pharma (Brentwood), NutraScience Labs (Farmingdale, Twinlab sub), SMP Nutra (Edgewood), Auri Nutra, Makers Nutrition (Commack) | directories |
| brandintus.com capabilities page titled "cGMP addition Manufacturing & Amazon Specialist" | competitor page |
| Amazon cGMP: mainstream sources consistent (all categories, approved TIC only, FDA registration insufficient); one source says "phasing out" while describing per-ASIN TIC routing | vendor/consultant blogs only |
| No Bactolac/Paramount business relationship found | checked, negative |

No Amazon first-party policy text retrieved. Most recent dated coverage: Aug-Sep 2026.
