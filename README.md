# Melanin Fit Men — Phase 1 Landing

The Phase 1 landing page for [@melaninfitmen](https://instagram.com/melaninfitmen)
at **melaninfitmen.com**. Vanilla HTML + CSS + a sliver of JS, deployed to
Cloudflare Pages with a Pages Function for the email signup.

## Structure

```
Melanin-Fit/
├── index.html
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── img/
│       ├── watermarks/        # 5 brand PNGs
│       ├── favicon-32.png
│       ├── favicon-180.png
│       └── og-image.png
├── functions/
│   └── api/subscribe.js       # POST /api/subscribe (Pages Function)
├── robots.txt
└── sitemap.xml
```

## Develop locally

No build step. Either:

- Open `index.html` directly in a browser (form will 404 — that's fine), **or**
- Run a static server from the project root:

  ```bash
  npx serve .
  ```

To test the `/api/subscribe` Pages Function locally, install Wrangler and run:

```bash
npm i -g wrangler
wrangler pages dev .
```

## Deploy to Cloudflare Pages

1. Push to GitHub:
   ```bash
   gh repo create melaninfitmen-site --public --source=. --remote=origin --push
   ```
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
3. Pick the repo. Build command: *(leave empty)*. Build output directory: `/`.
4. Click **Save and Deploy**. You'll get a URL like
   `melaninfitmen-site.pages.dev` in ~30 seconds.

### Wire the email form

The form posts to `/api/subscribe`, which is a Cloudflare Pages Function in
`functions/api/subscribe.js`. By default it accepts the email and logs it.
To plug in a real ESP, set these in **Settings → Environment variables**:

| Provider | Required env vars |
|---|---|
| ConvertKit | `ESP_PROVIDER=convertkit`, `CONVERTKIT_API_KEY`, `CONVERTKIT_FORM_ID` |
| Beehiiv | `ESP_PROVIDER=beehiiv`, `BEEHIIV_API_KEY`, `BEEHIIV_PUBLICATION_ID` |
| MailerLite | `ESP_PROVIDER=mailerlite`, `MAILERLITE_API_KEY`, `MAILERLITE_GROUP_ID` |

No HTML changes needed when you swap providers.

### Cloudflare Web Analytics

Create the property in the Cloudflare dashboard, copy the token, and uncomment
the analytics snippet near the bottom of the `<head>` in `index.html`.

## DNS migration: Bluehost → Cloudflare

Domain stays registered at Bluehost. Only the DNS resolver changes.

1. Cloudflare dashboard → **Add a Site** → enter `melaninfitmen.com` → **Free**
   plan. Cloudflare scans existing DNS.
2. Cloudflare gives you two nameservers (e.g. `arya.ns.cloudflare.com`,
   `bran.ns.cloudflare.com`).
3. Bluehost → Domains → `melaninfitmen.com` → Nameservers → **Use custom
   nameservers** → paste the two Cloudflare nameservers → Save.
4. Wait 5 min – a few hours for propagation. Cloudflare emails when active.
5. Pages project → **Custom domains** → add `melaninfitmen.com` and
   `www.melaninfitmen.com`. SSL provisions automatically.

If you have Bluehost email (`frank@melaninfitmen.com`), confirm the imported
MX records match what was at Bluehost before propagation completes.

## Phase 1 success checklist

- [ ] `melaninfitmen.com` resolves over HTTPS
- [ ] `www.melaninfitmen.com` redirects to apex
- [ ] Lighthouse mobile: Perf ≥ 90, A11y ≥ 95, SEO ≥ 95
- [ ] Renders cleanly at 375 / 768 / 1200 px
- [ ] Email form submits and a real signup arrives in your ESP
- [ ] Footer watermark + favicon visible
- [ ] OG preview works in iMessage / Slack
- [ ] Cloudflare Web Analytics shows pageviews
- [ ] Instagram bio updated: Linktree → `melaninfitmen.com`
