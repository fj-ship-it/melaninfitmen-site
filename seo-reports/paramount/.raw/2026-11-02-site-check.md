# Raw reachability data — 2026-11-02

Run from the **Melanin Fit** environment, ~11:12 UTC.

## 1. curl (Bash tool) — egress proxy

| Host | Result |
|---|---|
| `https://paramountnutra.com/?v=$RANDOM` | exit 56, `HTTP:000`, t=0.221s |
| `https://www.paramountnutra.com/?v=$RANDOM` | exit 56, `HTTP:000`, t=0.233s |
| `https://example.com/` (control) | `HTTP:000` |
| `https://api.github.com/` (control) | **HTTP:200** |

Signature unchanged from weeks 1–13: developer-infrastructure hosts pass, general web hosts are
refused at CONNECT. Not a Paramount outage, not DNS, not the 406/UA quirk.

## 2. Proxy status endpoint — names the cause

`curl -sS http://127.0.0.1:33521/__agentproxy/status` → `recentRelayFailures` contains:

```
{ "kind": "connect_rejected",
  "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host": "paramountnutra.com:443" }
{ ... "host": "www.paramountnutra.com:443" }
```

`selective: false`. Policy denial recorded proxy-side — the request never leaves the container.

## 3. WebFetch (server-side path)

`https://paramountnutra.com/?v=7781` → `getaddrinfo ENOTFOUND paramountnutra.com`.
Unchanged from weeks 10–13.

## 4. Search-index probes (the only instrument available)

| Probe | Result |
|---|---|
| `site:paramountnutra.com` (extended) | 8 pages: `/service-area/`, `/health-and-wellness-brands/`, `/capsule-manufacturing/`, `/liquid-supplement-manufacturing/`, `/private-label-supplement-manufacturer/`, `/contact/`, `/protein-powder-manufacturing/`, `/gummy-manufacturing/`. No blog posts, no `/faq/`, no `/tablet-manufacturing/`, no `/stock-formulations/` surfaced. |
| lead-time post ("how long does it take to manufacture a supplement") | **No Paramount URL.** SERP still owned by makersrow, vitaquest, elchemy, eightx — unchanged, still manufacturer-winnable. |
| GLP-1 companion page | **No Paramount URL.** |
| `/faq/` + "stock formulation" | **No Paramount URL** (page did not surface at all this week). |
| `"Paramount Nutra"` + October 2026 blog | **No Paramount URL.** Nothing dated Sept or Oct surfaced. |

Confirmed again from index text: six facilities, "cGMP-certified, FDA-registered **partner
facilities**", 16 years on service pages vs 30+ on contact, private label 4–8 week timelines,
Stony Brook NY, (888) 904-6977, info@paramountnutra.com.

Absence in a search probe is weak evidence (it was the wrong inference for eleven weeks on the
August posts). It is not proof nothing was published. It is the ceiling of what this environment
can measure.

## 5. Opportunity research

Not performed. Per the stop rule in `ROUTINE-PROMPT.md`, no new analysis was generated this week.
The live competitive data gathered 2026-10-26 (GLP-1 category, Bactolac, Long Island cluster,
switching-manufacturers SERP) is one week old and still current — see `.raw/2026-10-26-site-check.md`.
