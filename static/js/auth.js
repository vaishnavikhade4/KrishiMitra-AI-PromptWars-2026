const togglePassword = document.querySelector(".togglePassword");
const password = document.querySelector("#password");

if (togglePassword && password) {
    togglePassword.addEventListener("click", () => {

        if (password.type === "password") {
            password.type = "text";
            togglePassword.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            password.type = "password";
            togglePassword.classList.replace("fa-eye-slash", "fa-eye");
        }

    });
}