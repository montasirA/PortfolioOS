// =========================
// MOBILE MENU
// =========================

const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

if (menuBtn && navLinks) {

    menuBtn.addEventListener("click", () => {

        navLinks.classList.toggle("active");

        menuBtn.innerHTML = navLinks.classList.contains("active")
            ? "✕"
            : "☰";

    });

}



// =========================
// CLOSE MENU AFTER CLICK
// =========================

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

        menuBtn.innerHTML = "☰";

    });

});



// =========================
// CLICK OUTSIDE
// =========================

document.addEventListener("click", function (e) {

    if (

        navLinks.classList.contains("active")

        &&

        !navLinks.contains(e.target)

        &&

        !menuBtn.contains(e.target)

    ) {

        navLinks.classList.remove("active");

        menuBtn.innerHTML = "☰";

    }

});



// =========================
// ESC KEY
// =========================

document.addEventListener("keydown", function(e){

    if(e.key==="Escape"){

        navLinks.classList.remove("active");

        menuBtn.innerHTML="☰";

    }

});



// =========================
// NAVBAR SCROLL EFFECT
// =========================

const navbar = document.getElementById("navbar");

window.addEventListener("scroll", ()=>{

    if(window.scrollY > 60){

        navbar.classList.add("scrolled");

    }

    else{

        navbar.classList.remove("scrolled");

    }

});