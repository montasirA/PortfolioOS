const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

if(menuBtn){

    menuBtn.addEventListener("click", ()=>{

        navLinks.classList.toggle("active");

        menuBtn.innerHTML = navLinks.classList.contains("active")
            ? "✕"
            : "☰";

    });

}

document.querySelectorAll(".nav-links a").forEach(link=>{

    link.addEventListener("click",()=>{

        navLinks.classList.remove("active");

        if(menuBtn){
            menuBtn.innerHTML="☰";
        }

    });

});