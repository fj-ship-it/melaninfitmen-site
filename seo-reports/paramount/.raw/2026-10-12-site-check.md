# Raw reachability data — 2026-10-12

Run from the **Melanin Fit** environment (the one this routine is bound to), 11:2x UTC.

## curl (Bash tool) — egress proxy

```
$ curl -sS -A "<Chrome 126 UA>" https://paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403
HTTP 000  time 0.314659s

$ curl -sS -A "<Chrome 126 UA>" https://www.paramountnutra.com/?v=$RANDOM
curl: (56) CONNECT tunnel failed, response 403
HTTP 000  time 0.280000s
```

## Control hosts, same session, same tool

| Host | Result |
|---|---|
| `https://example.com` | `curl: (56) CONNECT tunnel failed, response 403` → 000 |
| `https://www.google.com` | `curl: (56) CONNECT tunnel failed, response 403` → 000 |
| `https://api.github.com` | **200** |

Signature unchanged from weeks 1-10: developer-infrastructure hosts pass, general web hosts are
denied at CONNECT. Egress allowlist, not a site outage.

## WebFetch (server-side fetch path) — NEW TEST THIS WEEK

```
WebFetch https://paramountnutra.com/sitemap.xml  -> getaddrinfo ENOTFOUND paramountnutra.com
WebFetch https://example.com/                    -> getaddrinfo ENOTFOUND example.com
```

Both fail identically with a DNS error. Because the control host fails the same way, the
`ENOTFOUND` on paramountnutra.com is **a property of this container's WebFetch path, not evidence
that the domain stopped resolving.** Recorded explicitly so a future run does not misread the
error-message change (EGRESS_BLOCKED in week 10 -> ENOTFOUND in week 11) as a newly dead domain.

## Not attempted

`curl $HTTPS_PROXY/__agentproxy/status` and reading `/root/.ccr/README.md` were both denied by the
auto-mode classifier (Containment Escape). Not retried or worked around. This is why no
proxy-policy detail appears in this week's report.

## Net effect

Sections 1 (lead-capture integrity), 2 (SEO regression from HTML), 4 (performance) cannot be run.
Zero bytes of paramountnutra.com HTML were read this week, as in the prior ten weeks.
