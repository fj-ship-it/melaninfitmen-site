# Melanin Fit Men — Phase 1 Landing

The Phase 1 landing page for [@melaninfitmen](https://instagram.com/melaninfitmen)
at **melaninfitmen.com**. Vanilla HTML + CSS + a sliver of JS, deployed to
**Cloudflare Workers + Static Assets** with a tiny Worker that handles the
email signup endpoint.

## Structure

```
Melanin-Fit/
├── public/                     # everything served as static
│   ├── index.html
│   ├── robots.txt
│   ├── sitemap.xml
│   └── assets/
│       ├── css/styles.css
│       ├── js/main.js
│       └── img/
│           ├── watermarks/     # 5 brand PNGs
│           ├── favicon-32.png
│           ├── favicon-180.png
│           └── og-image.png
├── src/
│   └── worker.js               # Worker entry — handles /api/subscribe, falls through to assets
├── wrangler.jsonc              # Cloudflare config
├── README.md
└── .gitignore
```

## Develop locally

No build step. Either:

- Open `public/index.html` directly in a browser (the subscribe form will
  fail — there's no server), **or**
- Run a static server from the `public/` directory:

  ```bash
  npx serve public
  ```

To test the `/api/subscribe` endpoint locally, install Wrangler and run:

```bash
npm i -g wrangler
wrangler dev
```

That spins up the Worker + serves `public/` locally at `http://localhost:8787`.

## Deploy to Cloudflare

The repo is connected to a Cloudflare Workers project. Pushing to `main` on
GitHub triggers an auto-redeploy.

To deploy manually from the command line:

```bash
npx wrangler deploy
```

### Wire the email form

The form posts to `/api/subscribe`, handled by `src/worker.js`. By default it
accepts the email and logs it. To plug in a real ESP, set these env vars in
the Cloudflare dashboard (**Workers & Pages → melaninfitmen-site → Settings
→ Variables**):

| Provider | Required env vars |
|---|---|
| ConvertKit | `ESP_PROVIDER=convertkit`, `CONVERTKIT_API_KEY`, `CONVERTKIT_FORM_ID` |
| Beehiiv | `ESP_PROVIDER=beehiiv`, `BEEHIIV_API_KEY`, `BEEHIIV_PUBLICATION_ID` |
| MailerLite | `ESP_PROVIDER=mailerlite`, `MAILERLITE_API_KEY`, `MAILERLITE_GROUP_ID` |

Mark the API keys as **Secret** when adding them. No HTML changes needed
when you swap providers.

### Cloudflare Web Analytics

Create the property in the Cloudflare dashboard, copy the token, and uncomment
the analytics snippet near the bottom of the `<head>` in `public/index.html`.

## DNS migration: Bluehost → Cloudflare

Domain stays registered at Bluehost. Only the DNS resolver changes.

1. Cloudflare dashboard → **Add a Site** → enter `melaninfitmen.com` → **Free**
   plan. Cloudflare scans existing DNS.
2. Cloudflare gives you two nameservers (e.g. `arya.ns.cloudflare.com`,
   `bran.ns.cloudflare.com`).
3. Bluehost → Domains → `melaninfitmen.com` → Nameservers → **Use custom
   nameservers** → paste the two Cloudflare nameservers → Save.
4. Wait 5 min – a few hours for propagation. Cloudflare emails when active.
5. Worker project → **Settings → Domains & Routes → Add custom domain** →
   add `melaninfitmen.com` and `www.melaninfitmen.com`. SSL provisions
   automatically.

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
