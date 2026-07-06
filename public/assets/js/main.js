(function () {
  "use strict";

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // Lite YouTube embeds — load the iframe only on click.
  var liteButtons = document.querySelectorAll(".yt-lite[data-video-id]");
  Array.prototype.forEach.call(liteButtons, function (btn) {
    btn.addEventListener("click", function () {
      var videoId = btn.getAttribute("data-video-id");
      if (!videoId) return;
      var iframe = document.createElement("iframe");
      iframe.src =
        "https://www.youtube-nocookie.com/embed/" +
        encodeURIComponent(videoId) +
        "?autoplay=1&playsinline=1&rel=0";
      iframe.title = btn.getAttribute("aria-label") || "YouTube video";
      iframe.allow =
        "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      btn.replaceChildren(iframe);
    }, { once: true });
  });

  var form = document.getElementById("subscribe-form");
  if (!form) return;

  var statusEl = form.querySelector(".form-status");
  var emailInput = form.querySelector('input[name="email"]');
  var submitBtn = form.querySelector('button[type="submit"]');

  function setStatus(message, kind) {
    if (!statusEl) return;
    statusEl.textContent = message || "";
    statusEl.classList.remove("is-error", "is-success");
    if (kind) statusEl.classList.add("is-" + kind);
  }

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var email = (emailInput.value || "").trim();

    if (!isValidEmail(email)) {
      setStatus("Enter a valid email address.", "error");
      emailInput.focus();
      return;
    }

    submitBtn.disabled = true;
    var originalLabel = submitBtn.textContent;
    submitBtn.textContent = "Sending...";
    setStatus("");

    fetch(form.action, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify({ email: email })
    })
      .then(function (res) {
        return res.json().then(function (data) { return { ok: res.ok, data: data }; });
      })
      .then(function (result) {
        if (result.ok) {
          form.reset();
          setStatus("You're in. The Clean Stack Guide is headed to your inbox.", "success");
        } else {
          setStatus((result.data && result.data.error) || "Something went wrong. Try again in a moment.", "error");
        }
      })
      .catch(function () {
        setStatus("Network error. Try again in a moment.", "error");
      })
      .then(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = originalLabel;
      });
  });
})();
