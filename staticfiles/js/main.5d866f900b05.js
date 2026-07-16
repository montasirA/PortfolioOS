document.addEventListener("DOMContentLoaded", function () {

    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");
    const navbar = document.getElementById("navbar");

    if (!menuBtn || !navLinks) return;

    // Toggle Mobile Menu
    menuBtn.addEventListener("click", function (e) {

        e.stopPropagation();

        navLinks.classList.toggle("active");

        menuBtn.innerHTML = navLinks.classList.contains("active")
            ? "✕"
            : "☰";

    });

    // Close after clicking link
    document.querySelectorAll("#navLinks a").forEach(link => {

        link.addEventListener("click", function () {

            navLinks.classList.remove("active");
            menuBtn.innerHTML = "☰";

        });

    });

    // Close outside
    document.addEventListener("click", function (e) {

        if (
            navLinks.classList.contains("active") &&
            !navLinks.contains(e.target) &&
            !menuBtn.contains(e.target)
        ) {

            navLinks.classList.remove("active");
            menuBtn.innerHTML = "☰";

        }

    });

    // ESC Close
    document.addEventListener("keydown", function (e) {

        if (e.key === "Escape") {

            navLinks.classList.remove("active");
            menuBtn.innerHTML = "☰";

        }

    });

    // Navbar Scroll
    if (navbar) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 60) {

                navbar.classList.add("scrolled");

            } else {

                navbar.classList.remove("scrolled");

            }

        });

    }

});