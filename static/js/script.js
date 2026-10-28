// ================= NAVBAR SCROLL EFFECT =================

window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".custom-navbar");

    if (!navbar) return;

    if (window.scrollY > 50) {

        navbar.style.background = "rgba(255,255,255,0.95)";
        navbar.style.boxShadow = "0 4px 25px rgba(0,0,0,0.08)";
        navbar.style.padding = "12px 0";

    } else {

        navbar.style.background = "rgba(255,255,255,0.15)";
        navbar.style.boxShadow = "none";
        navbar.style.padding = "18px 0";

    }

});



// ================= BUTTONS =================

const startBtn = document.querySelector(".start-btn");
const learnBtn = document.querySelector(".learn-btn");
const loginBtn = document.querySelector(".login-btn");
const registerBtn = document.querySelector(".register-btn");

function buttonClickEffect(button) {

    if (!button) return;

    button.addEventListener("click", () => {

        button.style.transform = "scale(0.95)";

        setTimeout(() => {

            button.style.transform = "scale(1)";

        }, 150);

    });

}

buttonClickEffect(startBtn);
buttonClickEffect(learnBtn);
buttonClickEffect(loginBtn);
buttonClickEffect(registerBtn);



// ================= PAGE REDIRECT =================

if (loginBtn) {

    loginBtn.addEventListener("click", () => {

        window.location.href = "/login";

    });

}

if (registerBtn) {

    registerBtn.addEventListener("click", () => {

        window.location.href = "/register";

    });

}



// ================= PARALLAX EFFECT =================

window.addEventListener("mousemove", (e) => {

    const leaf1 = document.querySelector(".leaf1");
    const leaf2 = document.querySelector(".leaf2");
    const bird1 = document.querySelector(".bird1");
    const bird2 = document.querySelector(".bird2");

    let x = e.clientX / 40;
    let y = e.clientY / 40;

    if (leaf1)
        leaf1.style.transform = `translate(${x}px,${y}px)`;

    if (leaf2)
        leaf2.style.transform = `translate(${-x}px,${-y}px)`;

    if (bird1)
        bird1.style.transform = `translate(${x / 2}px,${y / 2}px)`;

    if (bird2)
        bird2.style.transform = `translate(${-x / 2}px,${-y / 2}px)`;

});



// ================= HERO ANIMATION =================

window.addEventListener("load", () => {

    const heroText = document.querySelector(".hero-left");
    const heroImage = document.querySelector(".farmer-box");

    if (heroText) {

        heroText.style.opacity = "0";
        heroText.style.transform = "translateY(40px)";

        setTimeout(() => {

            heroText.style.transition = "1s ease";
            heroText.style.opacity = "1";
            heroText.style.transform = "translateY(0)";

        }, 300);

    }

    if (heroImage) {

        heroImage.style.opacity = "0";
        heroImage.style.transform = "translateX(60px)";

        setTimeout(() => {

            heroImage.style.transition = "1.2s ease";
            heroImage.style.opacity = "1";
            heroImage.style.transform = "translateX(0)";

        }, 500);

    }

});



// ================= LOGO ANIMATION =================

const logo = document.querySelector(".logo");

if (logo) {

    setInterval(() => {

        logo.style.transform = "scale(1.05)";

        setTimeout(() => {

            logo.style.transform = "scale(1)";

        }, 500);

    }, 3000);

}



// ================= SMOOTH SCROLL =================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});