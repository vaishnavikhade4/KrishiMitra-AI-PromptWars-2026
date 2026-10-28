
// IMAGE PREVIEW

const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const predictBtn = document.getElementById("predictBtn");

let selectedFile = null;

imageInput.addEventListener("change", function () {

    selectedFile = this.files[0];

    if (selectedFile) {

        const reader = new FileReader();

        reader.onload = function (e) {

            previewImage.src = e.target.result;

        };

        reader.readAsDataURL(selectedFile);

    }

});


// PREDICT BUTTON

predictBtn.addEventListener("click", async function () {

    if (!selectedFile) {

        alert("Please upload an image first.");

        return;

    }

    const formData = new FormData();

    formData.append("file", selectedFile);

    const response = await fetch("/predict", {

        method: "POST",

        body: formData

    });

    const data = await response.json();

    if (data.error) {

        alert(data.error);

        return;

    }

    document.getElementById("diseaseName").innerHTML = data.disease;

    document.getElementById("confidence").innerHTML =
        data.confidence + "%";

    document.getElementById("symptoms").innerHTML =
        data.symptoms.map(s => `<li>✓ ${s}</li>`).join("");

    document.getElementById("treatment").innerHTML =
        data.treatment.map(s => `<li>✓ ${s}</li>`).join("");

    document.getElementById("prevention").innerHTML =
        data.prevention.map(s => `<li>✓ ${s}</li>`).join("");

});
