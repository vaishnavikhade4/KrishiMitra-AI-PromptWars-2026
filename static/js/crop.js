document.getElementById("recommendBtn").addEventListener("click", async () => {

    const data = {

        nitrogen: document.getElementById("nitrogen").value,
        phosphorus: document.getElementById("phosphorus").value,
        potassium: document.getElementById("potassium").value,
        temperature: document.getElementById("temperature").value,
        humidity: document.getElementById("humidity").value,
        ph: document.getElementById("ph").value,
        rainfall: document.getElementById("rainfall").value

    };

    const response = await fetch("/recommend_crop", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    const result = await response.json();

    document.getElementById("cropName").innerHTML = result.crop;
    document.getElementById("season").innerHTML = result.season;
    document.getElementById("yield").innerHTML = result.yield;
    document.getElementById("fertilizer").innerHTML = result.fertilizer;

    document.getElementById("tips").innerHTML = "";

    result.tips.forEach(tip => {
        document.getElementById("tips").innerHTML += "<li>" + tip + "</li>";
    });

});