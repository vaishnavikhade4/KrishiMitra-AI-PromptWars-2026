alert("weather.js loaded");
document.getElementById("weatherBtn").addEventListener("click", async () => {

    const city = document.getElementById("city").value;

    if(city==""){

        alert("Please enter city name");

        return;

    }

    const response = await fetch("/get_weather",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            city:city
        })

    });

    const data = await response.json();

    if(data.error){

        alert(data.error);

        return;

    }

    document.getElementById("cityName").innerHTML=data.city;

    document.getElementById("temperature").innerHTML=data.temperature+" °C";

    document.getElementById("humidity").innerHTML=data.humidity+" %";

    document.getElementById("wind").innerHTML=data.wind+" km/h";

    document.getElementById("condition").innerHTML=data.condition;

    document.getElementById("rain").innerHTML=data.rain+" %";

    document.getElementById("warning").innerHTML=data.warning;

    document.getElementById("recommendation").innerHTML="";

    data.recommendation.forEach(item=>{

        document.getElementById("recommendation").innerHTML+=
        "<li>"+item+"</li>";

    });

});