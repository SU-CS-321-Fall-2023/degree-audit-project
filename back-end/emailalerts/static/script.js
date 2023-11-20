// static/script.js

document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.body;

    // Check for user preference
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

    // Set initial theme based on user preference
    if (prefersDarkScheme.matches) {
        body.classList.add("dark-mode");
    } else {
        body.classList.remove("dark-mode");
    }

    // Toggle theme on button click
    themeToggle.addEventListener("click", function () {
        body.classList.toggle("dark-mode");
    });
});
