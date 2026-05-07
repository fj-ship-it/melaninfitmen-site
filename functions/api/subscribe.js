/**
 * POST /api/subscribe — Cloudflare Pages Function
 *
 * Phase 1 stub: validates the email and returns success.
 * Wire to your ESP by setting the env var ESP_PROVIDER + relevant keys
 * in the Cloudflare Pages dashboard (Settings → Environment Variables),
 * then uncomment the matching block below.
 *
 *   ESP_PROVIDER = "convertkit" | "beehiiv" | "mailerlite" | ""
 *
 * ConvertKit:
 *   CONVERTKIT_API_KEY, CONVERTKIT_FORM_ID
 * Beehiiv:
 *   BEEHIIV_API_KEY, BEEHIIV_PUBLICATION_ID
 * MailerLite:
 *   MAILERLITE_API_KEY, MAILERLITE_GROUP_ID
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}

export async function onRequestPost({ request, env }) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: "Invalid request body." }, 400);
  }

  const email = (payload && payload.email ? String(payload.email) : "").trim().toLowerCase();
  if (!EMAIL_RE.test(email)) {
    return json({ error: "Enter a valid email address." }, 400);
  }

  const provider = (env.ESP_PROVIDER || "").toLowerCase();

  try {
    if (provider === "convertkit") {
      const res = await fetch(
        `https://api.convertkit.com/v3/forms/${env.CONVERTKIT_FORM_ID}/subscribe`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ api_key: env.CONVERTKIT_API_KEY, email }),
        }
      );
      if (!res.ok) throw new Error(`ConvertKit ${res.status}`);
    } else if (provider === "beehiiv") {
      const res = await fetch(
        `https://api.beehiiv.com/v2/publications/${env.BEEHIIV_PUBLICATION_ID}/subscriptions`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${env.BEEHIIV_API_KEY}`,
          },
          body: JSON.stringify({ email, reactivate_existing: true, send_welcome_email: true }),
        }
      );
      if (!res.ok) throw new Error(`Beehiiv ${res.status}`);
    } else if (provider === "mailerlite") {
      const res = await fetch("https://connect.mailerlite.com/api/subscribers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${env.MAILERLITE_API_KEY}`,
        },
        body: JSON.stringify({
          email,
          groups: env.MAILERLITE_GROUP_ID ? [env.MAILERLITE_GROUP_ID] : undefined,
        }),
      });
      if (!res.ok) throw new Error(`MailerLite ${res.status}`);
    } else {
      // No provider wired yet — accept the address and log to the request
      // tail in the Cloudflare dashboard. Swap in a provider above when ready.
      console.log("[subscribe stub] received:", email);
    }
  } catch (err) {
    console.error("[subscribe] provider error:", err && err.message);
    return json({ error: "Could not subscribe right now. Try again shortly." }, 502);
  }

  return json({ ok: true });
}

export async function onRequest() {
  return json({ error: "Method not allowed." }, 405);
}
