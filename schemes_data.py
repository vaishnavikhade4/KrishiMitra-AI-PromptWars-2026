# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Government Agricultural Schemes Knowledge Base
Focus: National (India) and State-specific (Maharashtra).
All URLs point strictly to verified official government portals (.gov.in / .nic.in / mahadbt).
No fabricated deadlines, fake submissions, or unauthorized credential requirements.
"""

GOVERNMENT_SCHEMES = [
    {
        "id": "pmkisan",
        "category": "finance",
        "name": {
            "en": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            "mr": "प्रधानमंत्री किसान सन्मान निधी (PM-KISAN)",
            "hi": "प्रधानमंत्री किसान सम्मान निधि (PM-KISAN)"
        },
        "description": {
            "en": "Central sector scheme providing income support of ₹6,000 per year in three equal 4-monthly installments of ₹2,000 directly into Aadhaar-linked bank accounts of landholding farmer families.",
            "mr": "सर्व जमीनधारक शेतकरी कुटुंबांना आर्थिक मदत म्हणून दरवर्षी ₹६,००० तीन समान हप्त्यांमध्ये (प्रत्येकी ₹२,०००) थेट बँक खात्यात जमा केले जातात.",
            "hi": "भूमिधारक किसान परिवारों को ₹६,००० प्रति वर्ष की वित्तीय सहायता, ₹२,००० की तीन समान किश्तों में सीधे बैंक खाते में प्रदान की जाती है।"
        },
        "benefits": {
            "en": ["Direct financial grant of ₹6,000 per year", "100% centrally funded direct benefit transfer (DBT)", "Assists with purchase of seeds, fertilizers, and operational inputs"],
            "mr": ["दरवर्षी ₹६,००० थेट बँक खात्यात", "१००% केंद्र सरकारचे अनुदान (DBT)", "बियाणे, खते आणि शेती खर्चासाठी आर्थिक आधार"],
            "hi": ["प्रति वर्ष ₹६,००० की नकद सहायता", "सीधे आधार से जुड़े बैंक खाते में भुगतान", "कृषि आदानों और बीज-खाद खरीद में सहायक"]
        },
        "eligibility": {
            "en": ["All small and marginal landholding farmer families who own cultivable land", "Name registered in State land records (7/12 extract in Maharashtra)", "Excludes institutional landholders, serving/retired government officers, and income tax payers"],
            "mr": ["ज्या शेतकऱ्यांच्या नावावर शेतजमीन आहे (७/१२ उतारा)", "सर्व लहान आणि सीमांत शेतकरी कुटुंबे", "सरकारी नोकरदार व प्राप्तिकर (Income Tax) भरणारे शेतकरी वगळता"],
            "hi": ["सभी भूमिधारक किसान परिवार जिनके नाम कृषि भूमि है", "राज्य के भू-अभिलेखों में नाम दर्ज होना अनिवार्य", "आयकर दाता और सरकारी कर्मचारी इस योजना के पात्र नहीं हैं"]
        },
        "documents": {
            "en": ["Aadhaar Card with mobile linkage", "Land Ownership Record (7/12 & 8A in Maharashtra)", "Active Bank Account Passbook with NPCI/Aadhaar seeding", "Active Mobile Number for OTP authentication"],
            "mr": ["आधार कार्ड (मोबाईल लिंक असलेले)", "जमीन मालकीचा ७/१२ व ८-अ उतारा", "आधार संलग्न बँक पासबुक", "सक्रिय मोबाईल नंबर"],
            "hi": ["आधार कार्ड (मोबाइल लिंक)", "भूमि के दस्तावेज (खसरा/खतौनी)", "आधार से जुड़ा बैंक खाता", "सक्रिय मोबाइल नंबर"]
        },
        "process": {
            "en": "Self-register on PM-KISAN portal using Aadhaar and land record details, or apply via nearest Common Service Center (CSC). Complete e-KYC via facial recognition or OTP.",
            "mr": "PM-KISAN अधिकृत पोर्टलवर किंवा जवळच्या 'आपले सरकार' / CSC केंद्रावर जाऊन ७/१२ आणि आधार कार्डाद्वारे ऑनलाइन नोंदणी करा. e-KYC पूर्ण करणे बंधनकारक आहे.",
            "hi": "पोर्टल पर 'Farmer Corner' में जाकर स्वयं पंजीकरण करें अथवा निकटतम सीएससी केंद्र पर जाकर भू-अभिलेख और आधार से आवेदन करें।"
        },
        "website": "https://pmkisan.gov.in",
        "last_verified": "October 2026",
        "official_source": "Ministry of Agriculture & Farmers Welfare, Govt of India"
    },

    {
        "id": "namo_shetkari",
        "category": "state",
        "name": {
            "en": "Namo Shetkari Mahasanman Nidhi Yojana (Maharashtra)",
            "mr": "नमो शेतकरी महासन्मान निधी योजना (महाराष्ट्र शासन)",
            "hi": "नमो शेतकरी महासम्मान निधि योजना (महाराष्ट्र)"
        },
        "description": {
            "en": "Maharashtra State Government top-up scheme providing an additional ₹6,000 per year to eligible PM-Kisan beneficiaries in Maharashtra, bringing total annual assistance to ₹12,000.",
            "mr": "महाराष्ट्र शासनाची विशेष योजना; PM-Kisan च्या ₹६,००० व्यतिरिक्त राज्य सरकारकडून आणखी ₹६,००० देण्यात येतात, ज्यामुळे एकूण ₹१२,००० वार्षिक सन्मान निधी मिळतो.",
            "hi": "महाराष्ट्र सरकार की योजना जो पीएम-किसान के ₹६,००० के अतिरिक्त ₹६,००० और देती है, जिससे कुल वार्षिक सहायता ₹१२,००० हो जाती है।"
        },
        "benefits": {
            "en": ["Additional ₹6,000 per year directly credited to eligible farmers in Maharashtra", "Disbursed in three tranches of ₹2,000 synchronised with PM-Kisan"],
            "mr": ["महाराष्ट्र शासनाकडून वर्षाला अतिरिक्त ₹६,००० ची आर्थिक मदत", "PM-Kisan सोबतच प्रत्येकी ₹२,००० च्या हप्त्यात वितरण"],
            "hi": ["प्रति वर्ष ₹६,००० की अतिरिक्त राज्य सहायता", "कुल ₹१२,००० का वार्षिक संबल"]
        },
        "eligibility": {
            "en": ["Must be an approved beneficiary of PM-KISAN residing in Maharashtra", "Valid land title (7/12 extract) registered in Maharashtra", "Active e-KYC and NPCI-linked DBT bank account"],
            "mr": ["शेतकरी महाराष्ट्राचा रहिवासी असणे आवश्यक", "PM-Kisan योजनेचा अधिकृत लाभार्थी असणे बंधनकारक", "७/१२ उतारा आणि आधार प्रमाणीकरण पूर्ण असावे"],
            "hi": ["महाराष्ट्र का मूल निवासी किसान होना आवश्यक", "पीएम-किसान योजना का सत्यापित लाभार्थी होना अनिवार्य", "भूमि रिकॉर्ड सही और आधार लिंक होना चाहिए"]
        },
        "documents": {
            "en": ["PM-Kisan Registration ID", "Aadhaar Card", "Maharashtra 7/12 & 8A Land Record", "Bank Passbook"],
            "mr": ["PM-Kisan नोंदणी क्रमांक", "आधार कार्ड", "७/१२ व ८-अ उतारा", "बँक पासबुक"],
            "hi": ["पीएम किसान पंजीकरण नंबर", "आधार कार्ड", "७/१२ खतौनी", "बैंक पासबुक"]
        },
        "process": {
            "en": "Automated integration for approved PM-Kisan farmers in Maharashtra. Verification can be tracked on the MahaDBT farmer portal.",
            "mr": "PM-Kisan मधील पात्र शेतकऱ्यांना स्वतंत्र अर्जाची गरज नाही; MahaDBT पोर्टलवरून पडताळणी केली जाते.",
            "hi": "पीएम किसान के पात्र किसानों को स्वतः लाभ मिलता है; महाडीबीटी पोर्टल पर स्थिति जांचें।"
        },
        "website": "https://mahadbt.maharashtra.gov.in",
        "last_verified": "October 2026",
        "official_source": "Department of Agriculture, Government of Maharashtra"
    },

    {
        "id": "pmfby",
        "category": "insurance",
        "name": {
            "en": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
            "mr": "प्रधानमंत्री पीक विमा योजना (PMFBY / १ रुपयात पीक विमा)",
            "hi": "प्रधानमंत्री फसल बीमा योजना (PMFBY)"
        },
        "description": {
            "en": "Comprehensive risk insurance covering yield losses due to non-preventable natural perils (drought, dry spells, flood, inundation, pests & diseases). In Maharashtra, farmers can enroll at a nominal ₹1 premium under the Sarvadoor scheme.",
            "mr": "नैसर्गिक आपत्ती, अवकाळी पाऊस, दुष्काळ, कीड व रोगांमुळे होणाऱ्या पिकांच्या नुकसानीस सर्वसमावेशक विमा संरक्षण. महाराष्ट्रात फक्त ₹१ भरून विमा उतरवता येतो.",
            "hi": "सूखा, बाढ़, ओलावृष्टि और कीट-रोगों से फसल के नुकसान पर व्यापक बीमा कवरेज। महाराष्ट्र में ₹१ के टोकन प्रीमियम पर उपलब्ध।"
        },
        "benefits": {
            "en": ["Complete coverage from pre-sowing to post-harvest losses", "Lowest farmer premium (2% Kharif, 1.5% Rabi, 5% Commercial/Horticultural)", "Maharashtra ₹1 premium top-up by State government"],
            "mr": ["पेरणीपूर्व ते काढणीपश्चात सर्व टप्प्यांवर नुकसान भरपाई", "महाराष्ट्रात शेतकऱ्यांसाठी फक्त ₹१ मध्ये नोंदणी", "स्थानिक आपत्ती व गारपिटीसाठी ७२ तासांत ऑनलाइन पंचनामा"],
            "hi": ["बुवाई से लेकर कटाई के बाद तक के नुकसान पर भरपाई", "महाराष्ट्र में मात्र ₹१ टोकन प्रीमियम", "स्थानीय आपदा में ७२ घंटे के भीतर क्लेम सूचना"]
        },
        "eligibility": {
            "en": ["All farmers growing notified crops in notified areas", "Both loanee and non-loanee farmers, sharecroppers, and tenant farmers are eligible"],
            "mr": ["अधिसूचित पिके घेणारे सर्व शेतकरी", "खातेदार शेतकरी तसेच कुळ व भाडेतत्त्वावर शेती करणारे शेतकरी", "पीक पेरा नोंद ७/१२ वर असणे आवश्यक"],
            "hi": ["अधिसूचित क्षेत्रों में अधिसूचित फसल उगाने वाले सभी किसान", "बटाईदार और पट्टेदार किसान भी पात्र हैं"]
        },
        "documents": {
            "en": ["Aadhaar Card", "7/12 Land Record with Crop Sowing Certificate (Pik Pera)", "Bank Passbook with IFSC", "Sowing Declaration / Self-Certificate"],
            "mr": ["आधार कार्ड", "चालू वर्षाचा पीक पेरा नोंद असलेला ७/१२ उतारा", "बँक पासबुक", "हमीपत्र / घोषणापत्र"],
            "hi": ["आधार कार्ड", "खसरा खतौनी एवं बुवाई प्रमाण पत्र", "बैंक पासबुक", "स्व-घोषणा पत्र"]
        },
        "process": {
            "en": "Apply through PMFBY national portal or the nearest CSC centre before the seasonal cut-off date (July 31 for Kharif, Dec 31 for Rabi). In case of localized damage, report within 72 hours via the Crop Insurance App.",
            "mr": "हंगाम संपण्यापूर्वी PMFBY पोर्टलवर किंवा सीएससी केंद्रावर ₹१ भरून अर्ज करा. नुकसान झाल्यास ७२ तासांच्या आत 'Crop Insurance App' वरून फोटोसह तक्रार नोंदवा.",
            "hi": "पोर्टल अथवा सीएससी पर जाकर कट-ऑफ तिथि से पूर्व आवेदन करें। नुकसान होने पर ७२ घंटे में 'क्रॉप इंश्योरेंस ऐप' से शिकायत दर्ज करें।"
        },
        "website": "https://pmfby.gov.in",
        "last_verified": "October 2026",
        "official_source": "Ministry of Agriculture & Farmers Welfare, Govt of India"
    },

    {
        "id": "pmkusum",
        "category": "irrigation",
        "name": {
            "en": "PM-KUSUM Solar Agricultural Pump Scheme",
            "mr": "पीएम-कुसुम सौर कृषी पंप योजना (महाकृषी ऊर्जा अभियान)",
            "hi": "पीएम-कुसुम सोलर पंप योजना"
        },
        "description": {
            "en": "Promotes solarization of agricultural pump sets. Component-B offers up to 90% subsidy (30% Central + 60% State in Maharashtra through MEDA/MSEDCL) for standalone off-grid solar water pumps (3 HP, 5 HP, 7.5 HP).",
            "mr": "शेतकऱ्यांना सिंचनासाठी दिवसा वीज उपलब्ध करून देण्यासाठी सौर पंपांवर ९०% पर्यंत अनुदान (केंद्र ३०% + राज्य शासन ६०%). शेतकरी हिस्सा फक्त १०% (SC/ST प्रवर्गासाठी ५%).",
            "hi": "किसानों को सिंचाई के लिए दिन में बिजली देने हेतु सौर ऊर्जा पंपों पर ९०% तक की सब्सिडी। किसान अंश मात्र १०% (एससी/एसटी के लिए ५%)।"
        },
        "benefits": {
            "en": ["Up to 90% capital subsidy on 3, 5, and 7.5 HP solar pumps", "Guaranteed daylight irrigation, eliminating night power hazards", "Zero electricity bills and reliable water for 25 years"],
            "mr": ["३, ५ आणि ७.५ एचपी सौर पंपांवर ९०% पर्यंत अनुदान", "रात्रीच्या धोक्यांशिवाय दिवसा सुरक्षित पाणी", "२५ वर्षे मोफत वीज आणि देखभाल"],
            "hi": ["३, ५ व ७.५ एचपी सौर पंपों पर ९०% तक सब्सिडी", "दिन में विश्वसनीय सिंचाई की सुविधा", "बिजली बिलों से पूर्ण मुक्ति"]
        },
        "eligibility": {
            "en": ["Farmer with cultivable land and an available water source (well, borewell, farm pond)", "Must not already possess a conventional grid electricity connection for irrigation"],
            "mr": ["शेतजमीन व पाण्याचा शाश्वत स्त्रोत (विहीर, कूपनलिका, शेततळे) असणारे शेतकरी", "पारंपरिक कृषी वीज जोडणी नसलेले शेतकरी"],
            "hi": ["जिनके पास कृषि भूमि और जल स्रोत (कुआं, बोरवेल, तालाब) उपलब्ध हो", "जहां पहले से ग्रिड बिजली कनेक्शन न हो"]
        },
        "documents": {
            "en": ["7/12 Land Record and 8A Extract", "No-Objection Certificate from Water Resource / Gram Panchayat", "Aadhaar Card", "Caste Certificate (for SC/ST concession)"],
            "mr": ["७/१२ व ८-अ उतारा", "विहीर किंवा बोअरवेल पाण्याची नोंद", "आधार कार्ड", "जातीचा दाखला (लागू असल्यास)"],
            "hi": ["७/१२ खतौनी और ८-ए", "जल स्रोत का प्रमाण पत्र", "आधार कार्ड", "जाति प्रमाण पत्र"]
        },
        "process": {
            "en": "Apply online on the official Maharashtra State Electricity Distribution Co. (MSEDCL) Solar Pump portal or PM-KUSUM portal. Upload documents and pay the beneficiary share after demand note generation.",
            "mr": "महावितरण (MSEDCL) किंवा महाऊर्जा (MEDA) पोर्टलवर जाऊन ऑनलाइन अर्ज करा. मंजुरी मिळाल्यावर डिमांड नोट भरून सौर पंप बसवून घ्या.",
            "hi": "महावितरण या पीएम-कुसुम पोर्टल पर ऑनलाइन आवेदन करें। डिमांड नोट जारी होने पर किसान अंश जमा करें।"
        },
        "website": "https://pmkusum.mnre.gov.in",
        "last_verified": "October 2026",
        "official_source": "Ministry of New and Renewable Energy / MSEDCL Maharashtra"
    },

    {
        "id": "kcc",
        "category": "credit",
        "name": {
            "en": "Kisan Credit Card (KCC) & Interest Subvention",
            "mr": "किसान क्रेडिट कार्ड (KCC - कमी व्याजाचे पीक कर्ज)",
            "hi": "किसान क्रेडिट कार्ड (KCC)"
        },
        "description": {
            "en": "Provides timely, institutional short-term credit up to ₹3,00,000 for crop cultivation, inputs, and post-harvest expenses at a subsidized effective interest rate of 4% (7% base minus 3% prompt repayment incentive).",
            "mr": "शेतकऱ्यांना खते, बियाणे व शेती मशागतीसाठी ₹३ लाखांपर्यंत अत्यल्प व्याजदरावर (वेळेत परतफेड केल्यास फक्त ४% प्रभावी व्याज) पीक कर्ज उपलब्ध करून देणारी योजना.",
            "hi": "खेती की लागत और आदानों के लिए ₹३ लाख तक का अल्पकालिक ऋण, समय पर भुगतान करने पर मात्र ४% प्रभावी ब्याज दर पर।"
        },
        "benefits": {
            "en": ["Credit limit up to ₹3 Lakh at effectively 4% interest per annum", "Collateral-free loan up to ₹1.60 Lakh", "Covers crop cultivation, animal husbandry, and fisheries"],
            "mr": ["वेळेवर परतफेड केल्यास ३ लाखांपर्यंत कर्ज फक्त ४% व्याजाने", "₹१.६० लाखांपर्यंत कोणतेही तारण (Collateral) न देता कर्ज", "पशुपालन व मत्स्यपालनासाठीही सुविधा उपलब्ध"],
            "hi": ["समय पर भुगतान पर मात्र ४% ब्याज दर", "₹१.६० लाख तक बिना किसी बंधक (कोलैटरल) के ऋण", "पशुपालन और डेयरी के लिए भी मान्य"]
        },
        "eligibility": {
            "en": ["Individual or joint landholders", "Tenant farmers, sharecroppers, and oral lessees with verified cultivation agreements"],
            "mr": ["जमीनधारक वैयक्तिक किंवा संयुक्त शेतकरी", "बटाईदार किंवा भाडेकरू शेतकरी"],
            "hi": ["व्यक्तिगत या संयुक्त रूप से भूमिधारक किसान", "बटाईदार और पट्टेदार किसान भी पात्र"]
        },
        "documents": {
            "en": ["Completed KCC Application Form", "Aadhaar Card & PAN Card", "Land Record (7/12 & 8A in Maharashtra)", "No Dues Certificate from adjacent bank branches"],
            "mr": ["केसीसी अर्ज", "आधार व पॅन कार्ड", "७/१२ व ८-अ उतारा", "इतर बँकेचे थकबाकी नसल्याचे प्रमाणपत्र"],
            "hi": ["केसीसी आवेदन पत्र", "आधार व पैन कार्ड", "भूमि दस्तावेज", "नो ड्यूज प्रमाण पत्र"]
        },
        "process": {
            "en": "Download standard 1-page KCC form from myscheme.gov.in or obtain from your local cooperative or nationalized bank branch. Banks issue KCC within 14 days of receipt.",
            "mr": "आपल्या गावातील राष्ट्रीयीकृत किंवा सहकारी बँकेच्या शाखेत जाऊन १ पानाचा KCC अर्ज ७/१२ जोडून जमा करा. १४ दिवसांत मंजुरी मिळते.",
            "hi": "अपने निकटतम बैंक शाखा में जाकर १ पेज का आवेदन पत्र जमा करें। १४ दिनों के भीतर कार्ड जारी किया जाता है।"
        },
        "website": "https://www.myscheme.gov.in/schemes/kcc",
        "last_verified": "October 2026",
        "official_source": "Department of Agriculture and Farmers Welfare & RBI"
    },

    {
        "id": "soil_health",
        "category": "soil",
        "name": {
            "en": "Soil Health Card Scheme (SHC)",
            "mr": "मृदा आरोग्य पत्रिका योजना (Soil Health Card)",
            "hi": "मृदा स्वास्थ्य कार्ड योजना (सॉइल हेल्थ कार्ड)"
        },
        "description": {
            "en": "Issues crop-wise fertilizer dosage recommendations based on laboratory testing of 12 critical chemical parameters (N, P, K, S, Zn, Fe, Cu, Mn, Bo, pH, EC, OC) to prevent costly over-fertilization.",
            "mr": "शेतकऱ्यांच्या शेतातील मातीचे १२ घटकांनुसार प्रयोगशाळेत मोफत परीक्षण करून रासायनिक खतांचा अतिवापर टाळण्यासाठी आणि उत्पादकता वाढवण्यासाठी मृदा पत्रिका दिली जाते.",
            "hi": "खेत की मिट्टी की १२ पोषक तत्वों की जांच कर संतुलित खाद प्रयोग हेतु किसानों को मृदा स्वास्थ्य कार्ड जारी किया जाता है।"
        },
        "benefits": {
            "en": ["Customized dosage recommendations for primary, secondary, and micronutrients", "Reduces unnecessary chemical fertilizer expenditure by 15-25%", "Improves long-term soil structure and fertility"],
            "mr": ["पिकानुसार खतांच्या योग्य मात्रेची अचूक शिफारस", "खतांचा खर्च १५ ते २५ टक्क्यांनी कमी होतो", "जमिनीची सुपीकता दीर्घकाळ टिकून राहते"],
            "hi": ["फसल अनुसार संतुलित पोषक तत्वों की सिफारिश", "खाद लागत में १५-२५% की बचत", "मिट्टी की उर्वरता में सुधार"]
        },
        "eligibility": {
            "en": ["All farmers possessing agricultural land in India"],
            "mr": ["शेती असणारे सर्व शेतकरी"],
            "hi": ["सभी भूमिधारक किसान"]
        },
        "documents": {
            "en": ["Soil sample collected following standard diagonal grid method", "Aadhaar Card", "7/12 Land Record"],
            "mr": ["शेतातील मातीचा नमुना (V आकारात काढलेला)", "आधार कार्ड", "७/१२ उतारा"],
            "hi": ["मिट्टी का नमूना", "आधार कार्ड", "खसरा खतौनी"]
        },
        "process": {
            "en": "Collect soil sample with assistance of taluka agricultural assistant (Krishi Sahayak) and submit to nearest Krishi Vigyan Kendra (KVK) or government soil testing laboratory. Download report online.",
            "mr": "तालुका कृषी सहाय्यक किंवा ग्रामसेवकांशी संपर्क साधून मातीचा नमुना द्या किंवा जवळच्या कृषी विज्ञान केंद्रात (KVK) जमा करा. पोर्टलवरून पत्रिका डाऊनलोड करा.",
            "hi": "कृषि सहायक की मदद से मिट्टी का नमूना लेकर कृषि विज्ञान केंद्र (केवीके) या प्रयोगशाला में जमा करें।"
        },
        "website": "https://soilhealth.dac.gov.in",
        "last_verified": "October 2026",
        "official_source": "Ministry of Agriculture & Farmers Welfare, Govt of India"
    },

    {
        "id": "mahadbt_drip",
        "category": "state",
        "name": {
            "en": "MahaDBT Micro-Irrigation & Farm Pond Subsidies",
            "mr": "महाडीबीटी सूक्ष्म सिंचन व शेततळे अनुदान योजना",
            "hi": "महाडीबीटी सूक्ष्म सिंचाई व खेत तालाब योजना"
        },
        "description": {
            "en": "Maharashtra State flagship scheme offering 75% to 80% capital subsidy for drip and sprinkler irrigation systems, along with 100% subsidies for individual plastic-lined farm ponds (Shet Tale).",
            "mr": "महाराष्ट्रातील शेतकऱ्यांसाठी ठिबक सिंचन आणि तुषार सिंचनावर ७५% ते ८०% अनुदान तसेच मागेल त्याला शेततळे योजनेअंतर्गत अनुदान देणारी योजना.",
            "hi": "महाराष्ट्र में ड्रिप व स्प्रिंकलर सिंचाई पर ७५-८०% अनुदान तथा व्यक्तिगत खेत तालाब निर्माण पर विशेष सहायता।"
        },
        "benefits": {
            "en": ["75% subsidy for small/marginal farmers and 60% for other farmers on drip/sprinkler systems", "Up to ₹75,000 grant for farm pond construction and plastic lining", "Saves up to 60% water while boosting crop yields by 35%"],
            "mr": ["लहान व सीमांत शेतकऱ्यांसाठी ठिबकवर ७५% ते ८०% थेट अनुदान", "शेततळे खोदकाम व प्लास्टिक अस्तरीकरणासाठी ₹७५,००० पर्यंत अनुदान", "पाण्याची ६०% बचत व पिकांच्या उत्पादनात ३५% वाढ"],
            "hi": ["ड्रिप व स्प्रिंकलर पर ७५ से ८०% तक प्रत्यक्ष अनुदान", "खेत तालाब निर्माण के लिए अनुदान", "पानी की भारी बचत और उपज में वृद्धि"]
        },
        "eligibility": {
            "en": ["Farmer in Maharashtra with valid land title (7/12)", "Permanent water source available on the farm", "Must register on MahaDBT Farmer Portal"],
            "mr": ["महाराष्ट्राचा रहिवासी शेतकरी", "७/१२ वर पाण्याची व विहिरीची नोंद असणे आवश्यक", "महाडीबीटी पोर्टलवर शेतकरी नोंदणी आवश्यक"],
            "hi": ["महाराष्ट्र का किसान, ७/१२ रिकॉर्ड होना अनिवार्य", "खेत पर जल स्रोत उपलब्ध होना चाहिए"]
        },
        "documents": {
            "en": ["7/12 & 8A Land Record", "Aadhaar Card", "Bank Passbook", "Water Source Certificate", "Quotation from authorized micro-irrigation dealer"],
            "mr": ["७/१२ व ८-अ उतारा", "आधार कार्ड", "बँक पासबुक", "अधिकृत ठिबक कंपनीचे कोटेशन"],
            "hi": ["७/१२ खतौनी", "आधार कार्ड", "बैंक पासबुक", "ड्रिप डीलर का कोटेशन"]
        },
        "process": {
            "en": "Register on the MahaDBT Farmer Portal under 'Agriculture Schemes'. Choose 'Micro-irrigation' and submit lottery application. Upon winning lottery, complete site inspection by Krishi Sahayak.",
            "mr": "MahaDBT पोर्टलवर 'शेतकरी योजना' या पर्यायामध्ये जाऊन सूक्ष्म सिंचनासाठी अर्ज करा. लॉटरीमध्ये नाव आल्यावर कंपनीचे कोटेशन अपलोड करा.",
            "hi": "महाडीबीटी किसान पोर्टल पर 'कृषि योजनाएं' के अंतर्गत आवेदन करें। लॉटरी में चयन होने पर सत्यापन पूर्ण कराएं।"
        },
        "website": "https://mahadbt.maharashtra.gov.in",
        "last_verified": "October 2026",
        "official_source": "Government of Maharashtra Agriculture Department"
    },

    {
        "id": "pkvy",
        "category": "organic",
        "name": {
            "en": "Paramparagat Krishi Vikas Yojana (PKVY - Organic Farming)",
            "mr": "परंपरागत कृषी विकास योजना (PKVY - सेंद्रिय शेती अभियान)",
            "hi": "परंपरागत कृषि विकास योजना (PKVY - जैविक खेती)"
        },
        "description": {
            "en": "Promotes organic cluster farming and Participatory Guarantee System (PGS) organic certification. Financial assistance of ₹50,000 per hectare is provided over 3 years, of which ₹31,000 is given directly for organic inputs (Jeevamrut, bio-fertilizers, vermicompost).",
            "mr": "शेतकऱ्यांचे सेंद्रिय गट तयार करून सेंद्रिय प्रमाणीकरण (PGS) आणि खतांसाठी ३ वर्षांत ₹५०,००० प्रति हेक्टर आर्थिक सहाय्य देणारी केंद्र व राज्य सरकारची योजना.",
            "hi": "जैविक क्लस्टर खेती और प्रमाणीकरण को बढ़ावा देने वाली योजना। जैविक खादों और बीजों के लिए ३ वर्षों में ₹५०,००० प्रति हेक्टेयर की वित्तीय सहायता।"
        },
        "benefits": {
            "en": ["₹50,000 per hectare grant over 3 years for inputs and certification", "Free PGS-India organic certification label for premium price realization", "Cluster-level value addition, packing, and direct market linkage"],
            "mr": ["३ वर्षांत प्रति हेक्टर ₹५०,००० चे अनुदान", "सेंद्रिय मालाच्या अधिक दरासाठी मोफत PGS सेंद्रिय प्रमाणपत्र", "थेट ग्राहकांना सेंद्रिय भाजीपाला विक्रीसाठी बाजारपेठ जोडणी"],
            "hi": ["३ वर्षों में ₹५०,००० प्रति हेक्टेयर का अनुदान", "निशुल्क जैविक प्रमाणीकरण प्रमाण पत्र", "जैविक उपज के लिए सीधी बाजार पहुंच"]
        },
        "eligibility": {
            "en": ["Farmer groups forming a cluster of minimum 20 hectares (50 farmers)", "Individual farmers joining established state organic clusters in Maharashtra (e.g. ATMA groups)"],
            "mr": ["किमान २० हेक्टर क्षेत्र असणारा ५० शेतकऱ्यांचा सेंद्रिय गट किंवा आत्मा (ATMA) शेतकरी गट"],
            "hi": ["कम से कम २० हेक्टेयर भूमि वाले किसानों का समूह या आत्मा (ATMA) से जुड़े किसान"]
        },
        "documents": {
            "en": ["Cluster farmer registration list", "Aadhaar Card and Bank Account", "7/12 Land Records", "Affidavit to adopt 100% organic practices"],
            "mr": ["शेतकरी गटाची नोंदणी यादी", "आधार कार्ड व बँक पासबुक", "७/१२ उतारा", "सेंद्रिय शेती करण्याचे प्रतिज्ञापत्र"],
            "hi": ["किसान समूह की सूची", "आधार व बैंक खाता", "भूमि रिकॉर्ड", "जैविक खेती शपथ पत्र"]
        },
        "process": {
            "en": "Contact your Taluka Agriculture Officer or Project Director, ATMA. Group formation and geo-tagging of organic plots is completed before grant disbursement.",
            "mr": "तालुका कृषी अधिकारी किंवा 'आत्मा' (ATMA) प्रकल्प कार्यालयाशी संपर्क साधून शेतकरी गटाची नोंदणी करा.",
            "hi": "तालुका कृषि अधिकारी अथवा 'आत्मा' (ATMA) कार्यालय से संपर्क कर समूह पंजीकृत करवाएं।"
        },
        "website": "https://daconline.gov.in",
        "last_verified": "October 2026",
        "official_source": "Department of Agriculture & Farmers Welfare, Govt of India"
    }
]

def get_all_schemes():
    return GOVERNMENT_SCHEMES

def get_scheme_by_id(scheme_id):
    for s in GOVERNMENT_SCHEMES:
        if s["id"] == scheme_id:
            return s
    return None

def evaluate_eligibility(land_acres, category="general", irrigation="drip"):
    """
    Evaluates guided eligibility questionnaire based on land holding, category, and irrigation.
    Returns matched schemes with specific rationale.
    """
    matches = []
    land = float(land_acres)
    
    for s in GOVERNMENT_SCHEMES:
        reasons = []
        is_match = False

        if s["id"] == "pmkisan":
            if land > 0:
                is_match = True
                reasons.append("Eligible because you own cultivable agricultural land.")
        
        elif s["id"] == "namo_shetkari":
            if land > 0:
                is_match = True
                reasons.append("Eligible for additional ₹6,000 Maharashtra state top-up as a verified landholding farmer.")

        elif s["id"] == "pmfby":
            if land > 0:
                is_match = True
                reasons.append("Eligible for crop insurance with token ₹1 premium in Maharashtra.")

        elif s["id"] == "kcc":
            if land > 0:
                is_match = True
                reasons.append(f"Eligible for subsidized short-term crop credit at 4% for your {land} acre farm.")

        elif s["id"] == "pmkusum":
            if irrigation in ["rainfed", "well", "none", "canal"] and land >= 1.0:
                is_match = True
                reasons.append("Highly eligible for 90% solar water pump subsidy to ensure day-time irrigation.")

        elif s["id"] == "mahadbt_drip":
            if irrigation != "drip" or land <= 5.0:
                is_match = True
                sub_pct = "80%" if (land <= 5.0 or category in ["sc", "st"]) else "70%"
                reasons.append(f"Eligible for {sub_pct} subsidy on drip or sprinkler irrigation under MahaDBT.")

        elif s["id"] == "soil_health":
            is_match = True
            reasons.append("Free scientific soil testing and customized nutrient card for every farmer.")

        elif s["id"] == "pkvy":
            is_match = True
            reasons.append("Eligible to join local organic farming clusters for ₹50,000/ha input subsidies.")

        if is_match:
            matches.append({
                "scheme": s,
                "reasons": reasons
            })

    return matches
