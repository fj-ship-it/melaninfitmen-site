(function () {
  "use strict";

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

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
          setStatus("You're in. Watch your inbox for the King's Drop.", "success");
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
