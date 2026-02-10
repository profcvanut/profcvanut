/* assets/js/main.js */

(function () {
  "use strict";

  // -----------------------------
  // Util
  // -----------------------------
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // -----------------------------
  // Navbar (mobile)
  // -----------------------------
  function initNav() {
    const toggle = $(".nav-toggle");
    const nav = document.querySelector("[data-nav]");
    if (!toggle || !nav) return;

    toggle.addEventListener("click", () => {
      const expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      nav.classList.toggle("open", !expanded);
    });

    // Fecha o menu ao clicar em um link
    $$(".site-nav a").forEach((a) => {
      a.addEventListener("click", () => {
        toggle.setAttribute("aria-ex
