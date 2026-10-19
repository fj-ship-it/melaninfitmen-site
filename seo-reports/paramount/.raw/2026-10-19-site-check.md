# Raw reachability + search-method data — 2026-10-19

Run from the **Melanin Fit** environment, ~11:16-11:30 UTC.

## 1. curl (Bash tool) — egress proxy

```
$ curl -sS -A "<Chrome 126 UA>" https://paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403     -> HTTP 000  time 0.280049s

$ curl -sS -A "<Chrome 126 UA>" https://www.paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403     -> HTTP 000  time 0.310615s
```

## 2. Control hosts, same session, same tool

| Host | Result |
|---|---|
| `https://example.com` | `curl: (56) CONNECT tunnel failed, response 403` -> 000 |
| `https://api.github.com` | **200** |

`getent hosts paramountnutra.com` -> no result. `HTTPS_PROXY=http://127.0.0.1:40287`.

Signature unchanged from weeks 1-11: developer-infrastructure hosts pass, general web hosts are
refused at CONNECT by the proxy. Not a Paramount outage, not DNS, not the 406/UA quirk.

## 3. WebFetch (server-side path)

| URL | Result |
|---|---|
| `https://paramountnutra.com/gummy-manufacturing/` | `getaddrinfo ENOTFOUND paramountnutra.com` |
| `https://example.com/` (control) | `getaddrinfo ENOTFOUND example.com` |

Control fails identically -> property of this container, not of the domain. Same as 2026-10-12.

## 4. WebSearch mode comparison — THE METHOD BUG

This is the important data this week. Prior reports' "exact-URL index trace: none" conclusions were
produced with `standard` mode. That mode cannot surface this domain at all.

| Query | Mode | Any paramountnutra.com result? |
|---|---|---|
| `site:paramountnutra.com gummy manufacturing` | standard | **No** (site: operator not honored) |
| `"paramountnutra.com/gummy-vs-capsule"` | standard | **No** |
| `"paramountnutra.com/what-cgmp-actually-means"` | standard | **No** |
| `Paramount Nutra Stony Brook supplement contract manufacturer` | standard | **No — not one result from the domain** |
| `paramountnutra` | **extended** | **Yes — 8 of 9 results from the domain** |

The 4th row is the control that invalidates the method: a direct brand + location query returning
nothing from the domain means absence-of-result carried no information in any prior week.

## 5. Pages confirmed to exist (via extended-mode results)

`/` `/blog/` `/contact/` `/faq/` `/gallery/` `/testimonials/` `/service-area/`
`/dietary-supplement/` `/health-and-wellness-brands/` `/capsule-manufacturing/`
`/gummy-manufacturing/` `/liquid-supplement-manufacturing/`
`/private-label-supplement-manufacturer/` `/protein-powder-manufacturing/`
plus `/wp-content/uploads/2024/06/Stock-Vegan-Greens-Paramount-PDF.pdf`

Did **not** surface in any probe: `/tablet-manufacturing/`, `/stock-formulations/`
(both listed as money pages in the routine prompt). Homepage reportedly links a tablet
manufacturing service, so the slug may differ from the one the routine checks.

## 6. Observed page facts (search-derived, not raw HTML)

| Page | Experience claim |
|---|---|
| `/contact/` | "more than 30 years" |
| `/dietary-supplement/` | "30+ years" |
| `/liquid-supplement-manufacturing/` | "16 years" |
| `/private-label-supplement-manufacturer/` | "16 years" |
| third-party directories | "16 years", "6 facilities" |

Titles observed: `/contact/` = "Request a Supplement Manufacturing Quote";
`/dietary-supplement/` = "Dietary Supplement Company". **No collision** — retires the
two-week-old duplicate-title candidate.

NAP: 2168 Nesconset Hwy, Stony Brook, NY 11790; toll-free (888) 904-6977; info@paramountnutra.com.

Blog index (`/blog/`) snippet listed three posts: protein supplement demand; what cGMP means and
how to check a manufacturer's claims; gummy vs capsule format comparison. Search metadata put the
cached blog page ~539 days old, which conflicts with its own "2026 guide" banner — cache age is
unreliable here, so treat the listing as evidence of existence, not of publish date.
