// ===============================
// KrishiMitra AI Dashboard JS
// ===============================

// Sidebar Active Menu

const menuItems = document.querySelectorAll(".sidebar ul li");

menuItems.forEach(item => {

    item.addEventListener("click", () => {

        menuItems.forEach(i => i.classList.remove("active"));

        item.classList.add("active");

    });

});


// ===============================
// Card Hover Animation
// ===============================

const cards = document.querySelectorAll(".card-box");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-10px) scale(1.03)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px) scale(1)";

    });

});


// ===============================
// Counter Animation
// ===============================

const counters = document.querySelectorAll(".stat h2");

counters.forEach(counter => {

    const target = parseInt(counter.innerText);

    let count = 0;

    const speed = 20;

    const update = () => {

        if(count < target){

            count++;

            counter.innerText = count;

            setTimeout(update, speed);

        }

    };

    counter.innerText = 0;

    update();

});


// ===============================
// Welcome Message
// ===============================

console.log("🌱 Welcome to KrishiMitra AI Dashboard");