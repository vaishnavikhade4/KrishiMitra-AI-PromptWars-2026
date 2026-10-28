# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Weather Service & Agricultural Decision Advisory
Connects to OpenWeatherMap API using WEATHER_API_KEY environment variable.
Generates evidence-based operational farm advisories (spraying, irrigation, disease risks).
"""

import os
import requests
from flask import current_app

class WeatherService:
    @staticmethod
    def get_weather_data(city_name="Pune"):
        api_key = os.getenv("WEATHER_API_KEY") or (current_app.config.get("WEATHER_API_KEY") if current_app else "")
        
        # Check if API key is provided
        if not api_key or api_key == "your_openweather_api_key_here":
            return {
                "configured": False,
                "error": "Weather API key not configured. Please add WEATHER_API_KEY to your .env file.",
                "demo_mode": True,
                "city": city_name,
                "temp": 28.5,
                "feels_like": 29.2,
                "temp_min": 22.0,
                "temp_max": 31.0,
                "humidity": 65,
                "wind_speed": 9.2,
                "condition": "Partly Cloudy",
                "condition_code": "Clouds",
                "icon": "03d",
                "rain_prob": 15,
                "pressure": 1012,
                "advisories": WeatherService._generate_agronomic_advisories(28.5, 65, 9.2, 15, "Partly Cloudy"),
                "forecast": WeatherService._generate_demo_forecast()
            }

        try:
            # 1. Fetch Current Weather
            curr_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            curr_resp = requests.get(curr_url, timeout=8)
            
            if curr_resp.status_code == 404:
                return {"configured": True, "error": f"Location '{city_name}' not found. Please try entering a district or major town."}
            elif curr_resp.status_code == 401:
                return {"configured": False, "error": "Invalid OpenWeather API Key. Please verify your credentials in .env."}
            elif curr_resp.status_code != 200:
                return {"configured": True, "error": f"Weather service temporarily unavailable (Code: {curr_resp.status_code})."}

            data = curr_resp.json()
            temp = round(data["main"]["temp"], 1)
            feels_like = round(data["main"]["feels_like"], 1)
            temp_min = round(data["main"]["temp_min"], 1)
            temp_max = round(data["main"]["temp_max"], 1)
            humidity = data["main"]["humidity"]
            wind_speed = round(data["wind"]["speed"] * 3.6, 1)  # convert m/s to km/h
            condition = data["weather"][0]["description"].title()
            condition_code = data["weather"][0]["main"]
            icon = data["weather"][0]["icon"]
            rain_mm = data.get("rain", {}).get("1h", 0) or data.get("rain", {}).get("3h", 0)
            rain_prob = 80 if rain_mm > 0 else (40 if "rain" in condition.lower() or "drizzle" in condition.lower() else 10)

            # 2. Fetch 5-Day Forecast
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
            forecast_resp = requests.get(forecast_url, timeout=8)
            forecast_items = []
            if forecast_resp.status_code == 200:
                f_data = forecast_resp.json()
                # Sample 1 forecast per day (around 12:00 PM)
                seen_dates = set()
                for item in f_data.get("list", []):
                    dt_txt = item["dt_txt"]
                    date_part = dt_txt.split(" ")[0]
                    time_part = dt_txt.split(" ")[1]
                    if "12:00:00" in time_part and date_part not in seen_dates:
                        seen_dates.add(date_part)
                        forecast_items.append({
                            "date": date_part,
                            "temp": round(item["main"]["temp"], 1),
                            "humidity": item["main"]["humidity"],
                            "condition": item["weather"][0]["description"].title(),
                            "icon": item["weather"][0]["icon"],
                            "pop": int(item.get("pop", 0) * 100)  # probability of precipitation
                        })
                    if len(forecast_items) >= 5:
                        break

            if not forecast_items:
                forecast_items = WeatherService._generate_demo_forecast()

            return {
                "configured": True,
                "error": None,
                "city": data.get("name", city_name),
                "country": data.get("sys", {}).get("country", "IN"),
                "temp": temp,
                "feels_like": feels_like,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "condition": condition,
                "condition_code": condition_code,
                "icon": icon,
                "rain_prob": rain_prob,
                "pressure": data["main"].get("pressure", 1013),
                "advisories": WeatherService._generate_agronomic_advisories(temp, humidity, wind_speed, rain_prob, condition),
                "forecast": forecast_items
            }

        except requests.exceptions.RequestException as e:
            return {
                "configured": True,
                "error": f"Network error connecting to weather provider: {str(e)}",
                "demo_mode": False
            }

    @staticmethod
    def _generate_agronomic_advisories(temp, humidity, wind_speed, rain_prob, condition):
        """Rule-based agronomic advisory based on meteorological thresholds."""
        advisories = {
            "spraying": {
                "status": "Safe",
                "badge": "success",
                "title": "Spraying Window Open",
                "message": "Wind speed and rainfall risk are low. Ideal window for protective or nutrient foliar spraying."
            },
            "irrigation": {
                "status": "Normal",
                "badge": "info",
                "title": "Regular Drip Irrigation",
                "message": "Soil moisture loss is moderate. Follow regular scheduled morning fertigation."
            },
            "disease_risk": {
                "status": "Low",
                "badge": "success",
                "title": "Low Disease Spread Risk",
                "message": "Current humidity and leaf wetness are unfavorable for rapid fungal spore germination."
            }
        }

        # Spraying evaluation
        if wind_speed > 14:
            advisories["spraying"] = {
                "status": "Unsafe (High Drift)",
                "badge": "danger",
                "title": "Avoid Chemical Spraying",
                "message": f"Wind speed is {wind_speed} km/h (above 14 km/h threshold). Spray drift will cause severe chemical wastage and off-target hazard."
            }
        elif rain_prob > 50 or "rain" in condition.lower():
            advisories["spraying"] = {
                "status": "Unsafe (Rain Expected)",
                "badge": "warning",
                "title": "Delay Chemical Sprays",
                "message": "Rain is likely within the next few hours. Foliar sprays will wash off before systemic absorption."
            }

        # Irrigation evaluation
        if rain_prob > 60 or "rain" in condition.lower():
            advisories["irrigation"] = {
                "status": "Delay Irrigation",
                "badge": "warning",
                "title": "Hold Scheduled Irrigation",
                "message": "Rainfall will provide sufficient root zone moisture. Prevent root asphyxiation and damping-off rot."
            }
        elif temp > 34:
            advisories["irrigation"] = {
                "status": "Increase Frequency",
                "badge": "danger",
                "title": "High Evapotranspiration Alert",
                "message": f"Ambient temperature is {temp}°C. Increase drip watering duration in early mornings to prevent flower blossom drop."
            }

        # Fungal & Pest Risk
        if humidity > 78 and 18 <= temp <= 28:
            advisories["disease_risk"] = {
                "status": "High Fungal Risk",
                "badge": "danger",
                "title": "Late Blight & Bacterial Warning",
                "message": f"High humidity ({humidity}%) and warm weather ({temp}°C) create optimal conditions for blight and leaf mold. Scout underside of leaves."
            }
        elif humidity < 45 and temp > 32:
            advisories["disease_risk"] = {
                "status": "Spider Mite Alert",
                "badge": "warning",
                "title": "Two-Spotted Spider Mite Outbreak Risk",
                "message": "Hot, dry conditions favor rapid mite multiplication. Check for yellow stippling and silk webbing on leaves."
            }

        return advisories

    @staticmethod
    def _generate_demo_forecast():
        from datetime import datetime, timedelta
        forecasts = []
        base = datetime.now()
        conditions = [
            {"cond": "Partly Cloudy", "temp": 29, "hum": 62, "pop": 10, "icon": "02d"},
            {"cond": "Light Rain Showers", "temp": 26, "hum": 78, "pop": 65, "icon": "10d"},
            {"cond": "Sunny & Clear", "temp": 31, "hum": 55, "pop": 5, "icon": "01d"},
            {"cond": "Passing Clouds", "temp": 30, "hum": 58, "pop": 15, "icon": "03d"},
            {"cond": "Clear Sky", "temp": 32, "hum": 50, "pop": 0, "icon": "01d"}
        ]
        for i in range(1, 6):
            day = base + timedelta(days=i)
            c = conditions[i-1]
            forecasts.append({
                "date": day.strftime("%Y-%m-%d"),
                "temp": c["temp"],
                "humidity": c["hum"],
                "condition": c["cond"],
                "icon": c["icon"],
                "pop": c["pop"]
            })
        return forecasts
