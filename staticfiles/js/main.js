document.addEventListener("DOMContentLoaded", function () {

    /* =========================
       NAVBAR
    ========================= */

    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");
    const navbar = document.getElementById("navbar");

    if (menuBtn && navLinks) {

        menuBtn.addEventListener("click", function (e) {

            e.stopPropagation();

            navLinks.classList.toggle("active");

            menuBtn.innerHTML = navLinks.classList.contains("active")
                ? "✕"
                : "☰";

            menuBtn.setAttribute(
                "aria-expanded",
                navLinks.classList.contains("active")
            );

        });

        document.querySelectorAll("#navLinks a").forEach(link => {

            link.addEventListener("click", function () {

                navLinks.classList.remove("active");

                menuBtn.innerHTML = "☰";

                menuBtn.setAttribute("aria-expanded", "false");

            });

        });

        document.addEventListener("click", function (e) {

            if (
                navLinks.classList.contains("active") &&
                !navLinks.contains(e.target) &&
                !menuBtn.contains(e.target)
            ) {

                navLinks.classList.remove("active");

                menuBtn.innerHTML = "☰";

                menuBtn.setAttribute("aria-expanded", "false");

            }

        });

        document.addEventListener("keydown", function (e) {

            if (e.key === "Escape") {

                navLinks.classList.remove("active");

                menuBtn.innerHTML = "☰";

                menuBtn.setAttribute("aria-expanded", "false");

            }

        });

    }

    /* =========================
       NAVBAR SCROLL
    ========================= */

    if (navbar) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 60) {

                navbar.classList.add("scrolled");

            } else {

                navbar.classList.remove("scrolled");

            }

        });

    }

    /* =========================
       HERO TYPING EFFECT
    ========================= */

    const typingElement = document.getElementById("typed-text");

    if (typingElement) {

        const words = [

            "Python Developer",

            "Django Backend Engineer",

            "Full Stack Developer",

            "AI Enthusiast",

            "Problem Solver",

            "Building Ideas Into Reality"

        ];

        let wordIndex = 0;
        let charIndex = 0;
        let deleting = false;

        function typeEffect() {

            const currentWord = words[wordIndex];

            if (!deleting) {

                typingElement.textContent = currentWord.substring(0, charIndex);

                charIndex++;

                if (charIndex > currentWord.length) {

                    deleting = true;

                    setTimeout(typeEffect, 1700);

                    return;

                }

            } else {

                typingElement.textContent = currentWord.substring(0, charIndex);

                charIndex--;

                if (charIndex < 0) {

                    deleting = false;

                    wordIndex++;

                    if (wordIndex >= words.length) {

                        wordIndex = 0;

                    }

                    charIndex = 0;

                }

            }

            setTimeout(typeEffect, deleting ? 45 : 90);

        }

        typeEffect();

    }

    /* =========================
       GALLERY LIGHTBOX
    ========================= */

    const galleryImages = document.querySelectorAll(".gallery-image");

    galleryImages.forEach(image => {

        image.addEventListener("click", function () {

            const overlay = document.createElement("div");

            overlay.className = "lightbox";

            overlay.innerHTML = `
                <img src="${this.src}" alt="">
            `;

            document.body.appendChild(overlay);

            document.body.style.overflow = "hidden";

            overlay.addEventListener("click", function () {

                overlay.remove();

                document.body.style.overflow = "";

            });

        });

    });

});