document.getElementById("searchBtn").addEventListener("click", function () {

    const crop = document.getElementById("crop").value;
    const state = document.getElementById("state").value;
    const district = document.getElementById("district").value;

    fetch("/get_market_price", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            crop: crop,
            state: state,
            district: district
        })

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("marketResult").innerHTML = `

            <div class="card shadow-lg border-0 rounded-4 mt-4">

                <div class="card-body">

                    <h3 class="text-success fw-bold">
                        ${data.crop}
                    </h3>

                    <hr>

                    <div class="row">

                        <div class="col-md-4">
                            <h6>Market</h6>
                            <h4>${data.market}</h4>
                        </div>

                        <div class="col-md-4">
                            <h6>Minimum Price</h6>
                            <h4>₹${data.min_price}</h4>
                        </div>

                        <div class="col-md-4">
                            <h6>Maximum Price</h6>
                            <h4>₹${data.max_price}</h4>
                        </div>

                    </div>

                    <hr>

                    <h5 class="text-primary">
                        Modal Price : ₹${data.modal_price}
                    </h5>

                </div>

            </div>

        `;

    });

});