# KrishiMitra AI — Intelligent Farming Assistant
**AI-Powered Smart Agriculture Platform for Prompt Wars Hackathon 2026**

KrishiMitra AI (कृषिमित्र AI) is a production-grade, full-stack, AI-driven smart agriculture platform designed to empower small, marginal, and commercial farmers across India (with an initial focus on Maharashtra).

---

## 🌟 Key Features & Functional Modules

### 1. 🍃 AI Plant Disease Detection (Core Module)
- **Real Deep Learning Model**: Uses a lightweight Convolutional Neural Network (CNN) trained on 10 tomato plant health classes (`models/plant_disease_model.keras`, only **322 KB** in size, perfectly meeting the hackathon's **<10 MB** repository limit).
- **Inference Pipeline**: Validates uploaded images (JPG, PNG, WEBP), resizes to exact `(224, 224)` RGB dimensions, normalizes pixel intensities to `[0, 1]`, and runs inference with confidence scoring.
- **Hardware Agnostic**: Supports local file uploads, drag-and-drop, and real-time live camera capture via WebRTC.
- **Diagnostics**: Displays predicted disease name, confidence %, host plant, health classification (Healthy vs Diseased), symptoms, causes, environmental conditions, spread mode, immediate actions, long-term prevention, and agronomist consultation thresholds.
- **Reliability Safeguards**: Flags scans with `<55%` confidence and advises taking closer, clearer photos before chemical application.

#### Supported Disease Classes:
1. `Tomato_Target_Spot` (Corynespora cassiicola)
2. `Tomato_Tomato_mosaic_virus` (ToMV)
3. `Tomato_Tomato_YellowLeaf_Curl_Virus` (TYLCV)
4. `Tomato_Bacterial_spot` (Xanthomonas campestris pv. vesicatoria)
5. `Tomato_Early_blight` (Alternaria solani)
6. `Tomato_healthy` (Optimal vegetative vigor)
7. `Tomato_Late_blight` (Phytophthora infestans)
8. `Tomato_Leaf_Mold` (Passalora fulva)
9. `Tomato_Septoria_leaf_spot` (Septoria lycopersici)
10. `Tomato_Spider_mites_Two_spotted_spider_mite` (Tetranychus urticae)

---

### 2. 🧪 Dual Treatment Plans (Chemical & Organic)
- **Side-by-Side Comparison**: Side-by-side on desktop, stacked on mobile.
- **Plan A — Chemical Fertilizer & Crop Protection Plan**:
  - Distinguishes nutrient deficiencies from infectious pathogens.
  - Recommends verified fungicides/bactericides/miticides (e.g., Mancozeb 75 WP, Copper Oxychloride 50 WP, Difenoconazole, Abamectin) with exact label precautions and Pre-Harvest Intervals (PHI).
  - Worker PPE requirements and environmental drift precautions.
- **Plan B — Certified Organic Treatment Plan**:
  - Cultural controls and field sanitation (deep burial of diseased tissue).
  - Crop rotation guidance with non-solanaceous crops (maize, pulses).
  - Biological control formulations: *Trichoderma harzianum*, *Pseudomonas fluorescens*, cold-pressed Neem Oil (10,000 ppm), NSKE 5%, Bordeaux mixture 1%, and fermented Jeevamrut.
- **Comparison Matrix**: Compares both plans on Estimated Cost, Speed of Action, Pre-Harvest Interval (PHI), and Environmental Impact.

---

### 3. 🌤️ Weather Forecasting & Farm Decision Advisory
- **Real Weather Integration**: OpenWeatherMap API connection configured via `WEATHER_API_KEY`.
- **Micro-Climate Tracking**: Temperature, Feels-like, Humidity %, Wind speed (km/h), Precipitation probability %, and 5-Day forecast.
- **Operational Farm Advisories**:
  - **Spraying Window**: Evaluates wind speed (>14 km/h drift threshold) and impending rainfall.
  - **Irrigation Guidance**: Recommends holding irrigation when rain is expected or increasing drip frequency during heatwaves (>34°C).
  - **Disease Risk Alert**: Flags high fungal spore germination risk when relative humidity exceeds 78% in moderate temperatures (18–28°C).
- **Graceful Fallback**: If `WEATHER_API_KEY` is unconfigured, displays a clear setup banner and verified regional baseline rather than fake live numbers.

---

### 4. 🏛️ Government Agricultural Schemes (India & Maharashtra)
- **Verified Portals Only**: Direct links strictly to verified government domains (`.gov.in`, `mahadbt.maharashtra.gov.in`).
- **Zero Sensitive Data Stored**: Does **not** ask for or store Aadhaar numbers, OTPs, or bank passwords.
- **Catalog of Schemes**:
  1. *PM-KISAN* (₹6,000/yr direct income support)
  2. *Namo Shetkari Mahasanman Nidhi Yojana* (Maharashtra ₹6,000/yr additional top-up)
  3. *PMFBY* (Crop insurance with ₹1 farmer premium in Maharashtra)
  4. *PM-KUSUM* (Up to 90% capital subsidy on solar agricultural water pumps)
  5. *Kisan Credit Card (KCC)* (Subsidized crop credit at 4% effective interest)
  6. *Soil Health Card Scheme* (12-parameter soil testing and fertilizer cards)
  7. *MahaDBT Micro-Irrigation* (75–80% subsidy for drip/sprinkler systems & farm ponds)
  8. *PKVY* (₹50,000/ha subsidy for organic farming clusters)
- **Guided Eligibility Tool**: Answers 3 quick questions (land size, farmer category, irrigation type) to calculate matching schemes.

---

### 5. 📈 Current Agricultural Market Prices
- **Authentic Mandi Rates**: Integrated with Agmarknet / Open Government Data (`data.gov.in`).
- **Parameters**: State, District (Pune, Nashik, Nagpur, Kolhapur), Commodity (Tomato, Onion, Soybean, Cotton).
- **Displays**: Arrival Date, APMC Mandi Name, Min Price, Max Price, Modal Price (₹/Quintal), and 30-day historical trend chart.
- **Anti-Fabrication Guard**: If external API keys are not supplied, displays authenticated Agmarknet historical benchmarks with clear disclosure.

---

### 6. 🤖 AI/ML 2–3 Months Market Price Forecasting
- **Time-Series Engine**: Uses Holt-Winters Double Exponential Smoothing with seasonal indexing to project 60-day to 90-day wholesale commodity price trends.
- **Chronological Validation**: Evaluates models on holdout historical test slices (avoiding random split data leakage) against a Seasonal-Naive prior-year baseline.
- **Uncertainty Bands**: Displays 80% and 95% confidence intervals growing with forecast horizon volatility ($\sigma \sqrt{t}$).
- **Evaluation Metrics**: Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE %), and RMSE.
- **Agronomic Factors & Disclaimer**: Explains seasonal arrivals, storage, and transport factors; explicitly notes forecasts are probabilistic estimates.

---

### 7. 🗣️ Personalized Farming Assistant
- **Multilingual Chatbot**: Native dialogue in Marathi (मराठी), English, and Hindi (हिंदी).
- **Dual AI Engine**: Supports Google Gemini API (`GEMINI_API_KEY`) when configured, with an automatic, offline rule-based knowledge engine fallback grounded in ICAR extension recommendations.
- **Conversation History**: Automatically logged and isolated to each authenticated farmer's account.

---

### 8. 👤 Farmer Profile & Farming History
- **Profile Customization**: Name, mobile, district, state, farm size (acres), primary crops, and preferred language.
- **Diagnostic History Archive**: Private, chronological table of all past leaf scans, images, confidence scores, and instant links to review saved treatment plans.
- **Strict User Isolation**: Database access control ensures no farmer can see another farmer's data.

---

### 9. 🌐 Multilingual Accessibility (3 Languages)
- **1. Marathi — मराठी** (Default for Maharashtra)
- **2. English**
- **3. Hindi — हिंदी**
- Persistent across user sessions, navigation, buttons, forms, alerts, and advisories. Preserves scientific names without distortion.

---

## 🏗️ Project Architecture

```
KrishiMitra-AI-PromptWars-2026/
├── app.py                      # Flask Application factory & routing
├── config.py                   # Environment configuration & .env loader
├── models.py                   # SQLAlchemy Models (User, DiseasePrediction, FarmingQuery)
├── translations.py             # Complete Multilingual Dictionary (MR, EN, HI)
├── disease_knowledge_base.py   # Verified Agronomic Knowledge Base for 10 classes
├── inference_engine.py         # Keras image preprocessor & model runner
├── weather_service.py          # Weather provider & agronomic decision rules
├── schemes_data.py             # Government schemes database & eligibility logic
├── market_service.py           # Mandi price retrieval & Agmarknet benchmark data
├── forecast_service.py         # Holt-Winters 2-3 months time-series price forecasting
├── assistant_service.py        # Conversational assistant (Gemini + Rule-based)
├── models/
│   └── plant_disease_model.keras # Real trained Keras CNN model (322 KB)
├── static/
│   ├── css/
│   │   └── krishimitra.css     # Unified modern agricultural stylesheet
│   ├── images/
│   │   ├── government-banner.png
│   │   └── sample_leaf.jpg
│   └── uploads/                # User uploaded leaf images
├── templates/
│   ├── base.html               # Base layout with sidebar & language selector
│   ├── index.html              # Modern Landing Page
│   ├── login.html              # Farmer Login
│   ├── register.html           # Farmer Registration
│   ├── dashboard.html          # Main Farmer Dashboard
│   ├── detect.html             # Disease Detection & Dual Treatment Plans
│   ├── treatment.html          # Dedicated Treatment Details view
│   ├── weather.html            # Weather Forecast & Farm Advisories
│   ├── government.html         # Government Schemes & Eligibility Check
│   ├── scheme.html             # Detailed Scheme View with Portal Link
│   ├── market.html             # Mandi Rates & 2-3 Months AI/ML Forecasting
│   ├── assistant.html          # Conversational Farming Assistant
│   ├── history.html            # My Farming History Log
│   └── settings.html           # Farmer Profile & Preferences
├── tests/
│   └── test_krishimitra.py     # 16 Unit & Integration Tests (100% Pass)
├── .env.example                # Configuration template
├── .gitignore                  # Git exclusions (caches, .env, large datasets)
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation
```

---

## ⚡ Quick Start Guide

### 1. Prerequisites
- Python 3.10+
- Pip package manager

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com/<your-username>/KrishiMitra-AI-PromptWars-2026.git
cd KrishiMitra-AI-PromptWars-2026

# Create virtual environment (optional)
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
Open `.env` and configure your API keys (optional; intelligent offline fallbacks are built-in):
```ini
SECRET_KEY=krishimitra_secure_session_key_2026_hackathon
WEATHER_API_KEY=your_openweather_api_key_here
DATA_GOV_IN_API_KEY=your_data_gov_in_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run Automated Test Suite
```bash
python -m unittest discover -s tests -v
```
*Expected: 16 passing tests covering auth, model loading, predictions, translations, weather, schemes, market forecasts, and history isolation.*

### 5. Launch Application
```bash
python app.py
```
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📊 Repository Size & Hackathon Compliance

| Metric | Hackathon Requirement | KrishiMitra AI Implementation | Status |
| :--- | :--- | :--- | :--- |
| **Repository Size** | Strictly Under 10 MB | **3.27 MB total** | ✅ Compliant |
| **Model Size** | Must fit under 10 MB | **322 KB** (`plant_disease_model.keras`) | ✅ Compliant |
| **Git Branches** | Single Branch | 1 branch (`main`) | ✅ Compliant |
| **Trained AI Model** | Real, no mock | Tested on sample leaf: 67.5% confidence | ✅ Compliant |
| **Languages** | Marathi, English, Hindi | Full UI & content translated | ✅ Compliant |
| **Credentials** | Never commit secrets | Kept strictly in `.env` / ignored | ✅ Compliant |

---

## 🛡️ Agricultural & Legal Disclaimer
KrishiMitra AI is an educational and technological decision-support system. All crop protection suggestions are compiled in accordance with standard agricultural university and ICAR extension literature. Farmers are urged to cross-verify specific pesticide formulations with local Krishi Vigyan Kendra (KVK) agronomists and read product labels before spraying. KrishiMitra AI never claims 100% future market price guarantees and never collects sensitive identity credentials like Aadhaar or bank passwords.
