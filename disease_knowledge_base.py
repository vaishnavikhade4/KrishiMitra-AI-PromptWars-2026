# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Plant Disease Knowledge Base
Covers all 10 trained classes from PlantVillage Tomato dataset.
Evidence-based recommendations strictly adhering to Indian Council of Agricultural
Research (ICAR) and State Agricultural University extension guidelines.
"""

DISEASE_KNOWLEDGE_BASE = {
    "Tomato_Target_Spot": {
        "scientific_pathogen": "Corynespora cassiicola (Fungus)",
        "plant_name": {
            "en": "Tomato (Solanum lycopersicum)",
            "mr": "टोमॅटो (Tomato)",
            "hi": "टमाटर (Tomato)"
        },
        "disease_name": {
            "en": "Target Spot (Corynespora Leaf Spot)",
            "mr": "टार्गेट स्पॉट (चकतीसारखे डाग)",
            "hi": "टारगेट स्पॉट (लक्ष्य धब्बा रोग)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Pinpoint brown to dark-brown lesions with concentric rings resembling a target board",
                "Lesions coalesce causing extensive foliage blighting and premature defoliation",
                "Sunken, dark circular lesions on green and ripening tomato fruit"
            ],
            "mr": [
                "पानांवर गोलाकार तपकिरी डाग ज्यामध्ये टार्गेट बोर्डसारखी चकतीची वर्तुळे दिसतात",
                "डाग एकत्र येऊन पाने करपतात आणि अकाली गळून पडतात",
                "हिरव्या व पिकलेल्या फळांवर खोलगट काळे डाग पडतात"
            ],
            "hi": [
                "पत्तियों पर भूरे रंग के गोल धब्बे जिनमें टारगेट बोर्ड की तरह छल्ले बनते हैं",
                "धब्बे आपस में मिलकर पत्तियों को झुलसा देते हैं और पत्तियां झड़ने लगती हैं",
                "फलों पर गहरे और धंसे हुए गोल धब्बे दिखाई देते हैं"
            ]
        },
        "causes": {
            "en": "Fungal pathogen Corynespora cassiicola surviving in infected crop debris and alternate weed hosts.",
            "mr": "कोरीनेस्पोरा कॅसिकोला ही बुरशी, जी पिकांच्या जुन्या अवशेषांमध्ये व तणांवर जिवंत राहते.",
            "hi": "कोरीनेस्पोरा कैसिकोला नामक कवक जो पिछली फसल के अवशेषों और खरपतवार पर जीवित रहता है।"
        },
        "environmental_factors": {
            "en": "High relative humidity (>85%), warm temperatures (22°C - 30°C), and prolonged leaf wetness.",
            "mr": "उच्च आर्द्रता (८५% पेक्षा जास्त), २२° ते ३०° से. दरम्यान तापमान आणि पानांवर जास्त वेळ राहिलेला ओलावा.",
            "hi": "उच्च आर्द्रता (८५% से अधिक), २२° से ३०° सेल्सियस तापमान और पत्तियों पर लंबे समय तक नमी।"
        },
        "spread_mode": {
            "en": "Airborne fungal conidia and splashing water droplets from rain or overhead sprinkler irrigation.",
            "mr": "हवेतील बुरशीचे बीजाणू आणि पावसाच्या पाण्याचे शिंतोडे किंवा स्प्रिंकलर सिंचन.",
            "hi": "हवा में तैरते कवक बीजाणु और वर्षा या फव्वारा सिंचाई के जल छींटे।"
        },
        "immediate_actions": {
            "en": [
                "Prune lower infected leaves showing concentric lesions to improve airflow.",
                "Halt overhead sprinkler irrigation immediately; switch to root-zone drip watering.",
                "Sterilize pruning shears between plants using 70% isopropyl alcohol."
            ],
            "mr": [
                "खालील रोगट पाने काढून नष्ट करा जेणेकरून झाडांमध्ये हवा खेळती राहील.",
                "तुषार किंवा स्प्रिंकलर सिंचन त्वरित थांबवून ठिबक सिंचनाने मुळांपाशी पाणी द्या.",
                "कात्री व शेती अवजारे ७०% अल्कोहोल किंवा सॅनिटायझरने निर्जंतुक करा."
            ],
            "hi": [
                "रोगग्रस्त निचली पत्तियों की कटाई करें ताकि पौधों में वायु संचार बना रहे।",
                "फव्वारा सिंचाई तुरंत बंद करें और ड्रिप द्वारा जड़ों में पानी दें।",
                "उपकरणों को ७०% सैनिटाइजर या अल्कोहल से कीटाणुरहित करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Follow a strict 3-year crop rotation with non-solanaceous crops (e.g., maize, pulses).",
                "Maintain adequate row-to-row spacing (75-90 cm) for canopy aeration.",
                "Apply clean plastic or organic straw mulch to prevent soil-splash pathogens."
            ],
            "mr": [
                "टोमॅटो नंतर मका किंवा कडधान्यासारख्या पिकांची ३ वर्षांची फेरपालट करा.",
                "रोपांमध्ये योग्य अंतर (७५ ते ९० सेमी) ठेवा जेणेकरून सूर्यप्रकाश व्यवस्थित मिळेल.",
                "मातीचे शिंतोडे पानांवर उडू नयेत म्हणून प्लास्टिक किंवा गवताचे आच्छादन (मल्चिंग) वापरा."
            ],
            "hi": [
                "मक्का या दलहनी फसलों के साथ कम से कम ३ साल का फसल चक्र अपनाएं।",
                "पंक्तियों के बीच पर्याप्त दूरी (७५ से ९० सेमी) रखें।",
                "मिट्टी के छींटों को रोकने के लिए मल्चिंग शीट का प्रयोग करें।"
            ]
        },
        "expert_threshold": {
            "en": "Consult an agricultural extension specialist if lesions spread to upper branches or cover >15% of canopy.",
            "mr": "झाडाच्या वरील फांद्यांवर रोग पसरल्यास किंवा १५% पेक्षा जास्त पाने बाधित झाल्यास कृषी तज्ज्ञांचा सल्ला घ्या.",
            "hi": "यदि रोग ऊपरी शाखाओं में फैल जाए या १५% से अधिक पत्तियां प्रभावित हों तो कृषि विशेषज्ञ से संपर्क करें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Targeted protective and curative fungicide spray to disrupt fungal spore germination and cell division.",
                "mr": "बुरशीचे बीजाणू रोखण्यासाठी प्रतिबंधात्मक व उपचारात्मक रासायनिक बुरशीनाशकांची फवारणी.",
                "hi": "कवक बीजाणुओं को नष्ट करने के लिए उपयुक्त रासायनिक कवकनाशी का समय पर छिड़काव।"
            },
            "formulations": [
                {"name": "Chlorothalonil 75% WP", "dosage": "2.0 g per Liter water", "phi_days": "5 days"},
                {"name": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC", "dosage": "1.0 ml per Liter water", "phi_days": "7 days"},
                {"name": "Mancozeb 75% WP", "dosage": "2.5 g per Liter water", "phi_days": "7 days"}
            ],
            "application_timing": {
                "en": "Spray in early morning (7:00-9:30 AM) or late afternoon (4:30-6:30 PM) under calm wind conditions (<8 km/h).",
                "mr": "सकाळी (७:०० ते ९:३०) किंवा संध्याकाळी (४:३० ते ६:३०) कमी वाऱ्याच्या वेळी फवारणी करा.",
                "hi": "सुबह (७:०० से ९:३०) या शाम (४:३० से ६:३०) शांत मौसम में छिड़काव करें।"
            },
            "safety_precautions": {
                "en": "Wear protective eye goggles, rubber gloves, and an N95 respirator mask. Do not enter field for 24 hours after application.",
                "mr": "फवारणी करताना गॉगल, रबर हातमोजे आणि मास्क वापरा. फवारणीनंतर २४ तास शेतात जनावरे अथवा माणसांना जाऊ देऊ नका.",
                "hi": "छिड़काव के समय दस्ताने, चश्मा और मास्क अवश्य पहनें। २४ घंटे तक खेत में प्रवेश न करें।"
            },
            "irrigation_guidance": {
                "en": "Apply through drip irrigation; avoid wet leaves overnight. Maintain moderate soil moisture without water stagnation.",
                "mr": "ठिबक सिंचनाने पाणी द्या; संध्याकाळी उशिरा पाणी देणे टाळा जेणेकरून रात्रभर पाने ओली राहणार नाहीत.",
                "hi": "ड्रिप सिंचाई अपनाएं और शाम को पत्तियों को गीला होने से बचाएं।"
            }
        },
        "organic_plan": {
            "approach": {
                "en": "Biological antagonism using beneficial microbial consortia and botanical immune elicitors.",
                "mr": "जैविक बुरशीनाशक, जिवामृत आणि वनस्पती अर्काचा वापर करून रोगाचे नैसर्गिक नियंत्रण.",
                "hi": "लाभकारी सूक्ष्मजीव, जीवामृत और वनस्पति अर्क द्वारा प्राकृतिक रोग नियंत्रण।"
            },
            "bio_agents": [
                {"name": "Trichoderma harzianum (2x10^9 CFU/g)", "dosage": "5 g per Liter water as foliar spray"},
                {"name": "Pseudomonas fluorescens 1% WP", "dosage": "5 g per Liter water root drench and spray"},
                {"name": "Neem Oil 10000 ppm (Cold Pressed)", "dosage": "3 ml per Liter water with mild emulsifier"}
            ],
            "sanitation": {
                "en": "Collect all fallen spotted leaves in sealable bags and deep-bury at least 1 meter away from cultivated plots.",
                "mr": "गळालेली सर्व रोगट पाने गोळा करून शेताबाहेर खड्ड्यात गाडून टाका.",
                "hi": "गिरी हुई सभी रोगग्रस्त पत्तियों को एकत्र कर खेत से दूर गड्ढे में दबा दें।"
            },
            "soil_health": {
                "en": "Drench root zone with enriched Jeevamrut (200 L/acre) every 14 days to boost soil microbial diversity.",
                "mr": "दर १४ दिवसांनी २०० लिटर एकरी जिवामृत ठिबकमधून किंवा मुळांशी द्या.",
                "hi": "मिट्टी की उर्वरता बढ़ाने के लिए हर १४ दिन पर २०० लीटर प्रति एकड़ जीवामृत दें।"
            }
        },
        "comparison": {
            "cost": {"chemical": "₹600 - ₹900 / acre", "organic": "₹250 - ₹450 / acre"},
            "speed": {"chemical": "Rapid (24 - 48 hours)", "organic": "Gradual (4 - 7 days)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "0 Days (Safe on harvest day)"},
            "eco_impact": {"chemical": "Moderate (Follow label precautions)", "organic": "Zero toxic residue, bee-friendly"}
        }
    },

    "Tomato_Tomato_mosaic_virus": {
        "scientific_pathogen": "Tomato Mosaic Tobamovirus (ToMV)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Tomato Mosaic Virus (ToMV)",
            "mr": "टोमॅटो मोझॅक व्हायरस (विषाणूजन्य पर्णरोग)",
            "hi": "टमाटर मोज़ेक वायरस"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Mottling of leaves with alternating light-green and dark-green patches",
                "Leaf distortion, blistering, curling, and 'fern-like' or 'shoestring' narrowing",
                "Severe stunting of young plants and internal browning of tomato fruits"
            ],
            "mr": [
                "पानांवर फिकट हिरवे व गडद हिरवे चट्टे (मोझॅक नक्षी) दिसतात",
                "पाने चुरडणे, बारीक होणे व वाकडीतिकडी आकुंचन पावून दोरीसारखी बारीक दिसणे",
                "झाडांची वाढ खुंटणे आणि फळांच्या आतून तपकिरी चट्टे पडणे"
            ],
            "hi": [
                "पत्तियों पर हल्के और गहरे हरे रंग के चितकबरे धब्बे (मोज़ेक पैटर्न)",
                "पत्तियों का सिकुड़ना, मुड़ना और पतले धागे जैसा हो जाना",
                "पौधों का बौना रह जाना और फलों के अंदर भूरापन आना"
            ]
        },
        "causes": {
            "en": "Tomato mosaic virus (ToMV), a highly stable mechanical rod-shaped viral pathogen.",
            "mr": "टोमॅटो मोझॅक विषाणू, जो अतिशय चिवट असून हाताच्या संपर्काने व अवजारांनी पसरतो.",
            "hi": "टोमैटो मोज़ेक वायरस जो संपर्क, औजारों और संक्रमित बीजों द्वारा फैलता है।"
        },
        "environmental_factors": {
            "en": "Temperatures between 24°C - 32°C accelerate viral replication and systemic movement.",
            "mr": "२४° ते ३२° से. तापमान विषाणूच्या प्रसारासाठी अतिशय अनुकूल असते.",
            "hi": "२४° से ३२° सेल्सियस तापमान में यह वायरस तेजी से फैलता है।"
        },
        "spread_mode": {
            "en": "Readily transmitted through sap on workers' hands, tools, grafting knives, and contaminated seeds. Not usually insect-transmitted.",
            "mr": "कामगारांचे हात, खुरपणीची अवजारे, कात्री आणि बियाणांच्या माध्यमातून वेगाने पसरतो.",
            "hi": "हाथों, औजारों और संक्रमित बीजों के माध्यम से आसानी से फैलता है।"
        },
        "immediate_actions": {
            "en": [
                "Rogue out (uproot) severely infected plants immediately, bag them on site, and burn/destroy.",
                "Wash hands thoroughly with soap or 20% skimmed milk before touching healthy plants.",
                "Disinfect all tools with 10% trisodium phosphate (TSP) or household bleach."
            ],
            "mr": [
                "तीव्र बाधित झालेली झाडे मुळासकट उपटून पोत्यात भरा आणि शेताबाहेर नेऊन जाळून टाका.",
                "निरोगी झाडांना हात लावण्यापूर्वी हात साबणाने किंवा २०% दुधाने स्वच्छ धुवा.",
                "कात्री व अवजारे ट्रायसोडियम फॉस्फेट किंवा ब्लिचच्या पाण्याने निर्जंतुक करा."
            ],
            "hi": [
                "संक्रमित पौधों को तुरंत जड़ सहित उखाड़कर खेत से दूर जला दें।",
                "स्वस्थ पौधों को छूने से पहले साबुन या २०% दूध से हाथ धोएं।",
                "औजारों को ब्लीच या ट्राइसोडियम फॉस्फेट से साफ करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Plant certified ToMV-resistant F1 hybrid varieties (e.g., cultivars bearing 'Tm-2^2' gene).",
                "Soak seeds in 10% trisodium phosphate for 30 minutes before sowing.",
                "Strictly prohibit tobacco smoking or chewing inside the tomato greenhouse or field."
            ],
            "mr": [
                "विषाणू-प्रतिरोधक वाणांची लागवड करा (उदा. Tm-2^2 जनुक असलेले वाण).",
                "पेरणीपूर्वी बियाण्यांवर ट्रायसोडियम फॉस्फेटची प्रक्रिया करा.",
                "टोमॅटोच्या शेतात तंबाखू, विडी किंवा सिगारेट ओढण्यावर सक्त बंदी ठेवा."
            ],
            "hi": [
                "वायरस प्रतिरोधी संकरित किस्मों का चयन करें।",
                "बुवाई से पहले बीजों का शोधन करें।",
                "टमाटर के खेत में बीड़ी, सिगरेट या तंबाकू के सेवन पर पूर्ण प्रतिबंध लगाएं।"
            ]
        },
        "expert_threshold": {
            "en": "Viruses cannot be cured once inside the vascular system. If >10% of field shows systemic mosaic, consult KVK for containment.",
            "mr": "विषाणूवर रासायनिक इलाज नसतो; १०% पेक्षा जास्त शेत बाधित असल्यास पुढील नुकसान टाळण्यासाठी कृषी विद्यापीठाशी संपर्क साधा.",
            "hi": "वायरस का कोई रासायनिक इलाज नहीं है। १०% से अधिक फसल प्रभावित होने पर कृषि विज्ञान केंद्र से संपर्क करें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Note: Antibiotics or fungicides do not kill viruses. Spraying is strictly restricted to vector-control if secondary pests occur.",
                "mr": "टीप: विषाणूवर कोणतेही थेट रासायनिक औषध नसते. दुय्यम कीड (मावा/तुडतुडे) नियंत्रणासाठी कीटकनाशकाचा वापर केला जाऊ शकतो.",
                "hi": "ध्यान दें: वायरस पर कवकनाशी या एंटीबायोटिक काम नहीं करते। केवल कीट नियंत्रण हेतु छिड़काव किया जाता है।"
            },
            "formulations": [
                {"name": "No direct viricide exists", "dosage": "Sanitation + rogueing only", "phi_days": "N/A"},
                {"name": "Acetamiprid 20% SP (if secondary sap-suckers present)", "dosage": "0.3 g per Liter water", "phi_days": "5 days"}
            ],
            "application_timing": {"en": "Focus on tool sterilization and sanitation rather than chemical sprays.", "mr": "फवारणीपेक्षा अवजारांचे निर्जंतुकीकरण व स्वच्छता यावर भर द्या.", "hi": "रासायनिक छिड़काव के बजाय औजारों की स्वच्छता पर ध्यान दें।"},
            "safety_precautions": {"en": "Always wash hands between rows. Do not use chemical fertilizers excessively.", "mr": "ओळींमध्ये काम करताना हात सतत स्वच्छ धुवा.", "hi": "काम करते समय हाथ स्वच्छ रखें।"},
            "irrigation_guidance": {"en": "Avoid water stress to keep surviving plants vigorous.", "mr": "झाडांची प्रतिकारशक्ती टिकवण्यासाठी नियमित पाणी द्या.", "hi": "पौधों को तनाव से बचाने के लिए संतुलित सिंचाई करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Application of skimmed milk spray to denature virus proteins and induce systemic acquired resistance (SAR).",
                "mr": "विषाणूचे प्रथिने निष्प्रभ करण्यासाठी आणि प्रतिकारशक्ती वाढवण्यासाठी दुधाच्या अर्काची फवारणी.",
                "hi": "वायरस के प्रोटीन को निष्क्रिय करने हेतु बिना मलाई वाले दूध का छिड़काव और रोग प्रतिरोधक क्षमता बढ़ाना।"
            },
            "bio_agents": [
                {"name": "Skimmed Milk / Raw Milk Solution (10% v/v)", "dosage": "100 ml per Liter water weekly as foliar spray"},
                {"name": "Pseudomonas fluorescens", "dosage": "10 g per Liter for inducing systemic resistance"},
                {"name": "Dashaparni Ark (10-plant fermented extract)", "dosage": "20 ml per Liter water"}
            ],
            "sanitation": {"en": "Burn uprooted diseased plants; do not compost.", "mr": "उपटलेली रोगट झाडे जाळून टाका; खतात टाकू नका.", "hi": "संक्रमित पौधों को जलाएं, कंपोस्ट में न डालें।"},
            "soil_health": {"en": "Apply vermicompost enriched with mycorrhiza to boost plant resilience.", "mr": "गांडूळ खताचा मुबलक वापर करा.", "hi": "वर्मीकंपोस्ट का भरपूर उपयोग करें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹300 - ₹500 / acre (Vector control)", "organic": "₹200 - ₹350 / acre (Milk spray & rogueing)"},
            "speed": {"chemical": "Preventative only", "organic": "Preventative only"},
            "phi": {"chemical": "5 Days", "organic": "0 Days"},
            "eco_impact": {"chemical": "Low", "organic": "100% eco-friendly and safe"}
        }
    },

    "Tomato_Tomato_YellowLeaf_Curl_Virus": {
        "scientific_pathogen": "Tomato Yellow Leaf Curl Begomovirus (TYLCV)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Tomato Yellow Leaf Curl Virus (TYLCV)",
            "mr": "टोमॅटो पिवळा पर्णगुच्छ रोग (चुरडा-मुरडा)",
            "hi": "टमाटर पीला पत्ती मरोड़ रोग (पर्ण कुंचन)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Upward curling, cupping, and crinkling of leaf margins",
                "Prominent yellowing (chlorosis) of young growing leaves and stunted bushy growth",
                "Severe flower drop resulting in drastic fruit yield reduction (>80%)"
            ],
            "mr": [
                "पानांच्या कडा वरच्या दिशेने वळून वाटीसारख्या (कप) आकाराच्या होतात",
                "शेंड्याकडील नवीन पाने पिवळी पडून झाडाची वाढ खुंटते आणि झाड झुडपासारखे दिसते",
                "फुले गळून पडतात व फळधारणा अत्यंत कमी होते (८०% पर्यंत घट)"
            ],
            "hi": [
                "पत्तियों के किनारे ऊपर की ओर मुड़कर कटोरी जैसी आकृति बना लेते हैं",
                "नई पत्तियों का पीला पड़ना और पौधे की वृद्धि रुककर झाड़ीदार हो जाना",
                "फूलों का भारी गिरना और फल बनने में भारी कमी"
            ]
        },
        "causes": {
            "en": "Geminivirus transmitted exclusively by the Silverleaf Whitefly (Bemisia tabaci).",
            "mr": "पांढरी माशी (Bemisia tabaci) या कीटकामुळे पसरणारा बेगोमोव्हायरस विषाणू.",
            "hi": "सफेद मक्खी (बेमिसिया तबासी) द्वारा फैलने वाला बेगोमोवायरस।"
        },
        "environmental_factors": {
            "en": "Hot, dry conditions (28°C - 38°C) that favor rapid whitefly population outbreaks.",
            "mr": "उष्ण व कोरडे हवामान (२८° ते ३८° से.) जे पांढऱ्या माशीच्या जलद पुनरुत्पादनास पूरक ठरते.",
            "hi": "गर्म और शुष्क मौसम (२८° से ३८° सेल्सियस) जिसमें सफेद मक्खी तेजी से बढ़ती है।"
        },
        "spread_mode": {
            "en": "Vector-borne through adult whiteflies feeding on phloem sap for as little as 15-30 minutes.",
            "mr": "पांढऱ्या माशीच्या डंखातून, जी १५-३० मिनिटांत निरोगी झाडामध्ये विषाणू सोडते.",
            "hi": "वयस्क सफेद मक्खियों के रस चूसने से यह वायरस एक से दूसरे पौधे में फैलता है।"
        },
        "immediate_actions": {
            "en": [
                "Install yellow sticky traps (15-20 traps/acre) at canopy height to capture whitefly vectors.",
                "Rogue out and destroy early symptomatic plants before whiteflies multiply on them.",
                "Protect nursery beds with 40-50 mesh insect-proof nylon nets."
            ],
            "mr": [
                "पांढऱ्या माशीच्या नियंत्रणासाठी शेतात एकरी १५ ते २० पिवळे चिकट सापळे लावा.",
                "सुरुवातीला दिसणारी रोगट झाडे उपटून त्वरित नष्ट करा.",
                "रोपवाटिकेमध्ये रोपे ४०-५० मेशच्या कीटक प्रतिबंधक जाळीतच तयार करा."
            ],
            "hi": [
                "प्रति एकड़ १५-२० पीले चिपचिपे कार्ड (येलो स्टिकी ट्रैप) लगाएं।",
                "प्रारंभिक रोगग्रस्त पौधों को उखाड़कर नष्ट करें।",
                "नर्सरी को ५० मेश कीटनाशक जाली से ढककर तैयार करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Grow TYLCV-resistant hybrids with Ty-1, Ty-2, or Ty-3 genetic tolerance.",
                "Plant 2-3 border rows of tall non-host barrier crops such as maize or sorghum around the field.",
                "Avoid planting tomato adjacent to older cucurbit, cotton, or brinjal fields infested with whitefly."
            ],
            "mr": [
                "Ty-1 किंवा Ty-3 जनुक असलेले रोगप्रतिकारक संकरित बियाणे वापरा.",
                "शेताच्या चारी बाजूंनी मका किंवा ज्वारीच्या २-३ ओळींचे दाट कुंपण लावा.",
                "कापूस किंवा वांगी पिकाजवळ टोमॅटोची लागवड करणे टाळा."
            ],
            "hi": [
                "वायरस प्रतिरोधी किस्मों की ही बुवाई करें।",
                "खेत की मेड़ों पर मक्का या ज्वार की २-३ पंक्तियों की सघन बाड़ लगाएं।",
                "कपास या बैंगन के संक्रमित खेतों के पास टमाटर न लगाएं।"
            ]
        },
        "expert_threshold": {
            "en": "If whitefly trap counts exceed 10 adults per trap per day or leaf curling affects >10% plants in vegetative stage.",
            "mr": "पिवळ्या सापळ्यावर दररोज १० पेक्षा जास्त पांढऱ्या माशा दिसल्यास किंवा १०% रोपे बाधित झाल्यास तातडीने सल्ला घ्या.",
            "hi": "यदि चिपचिपे ट्रैप पर प्रति दिन १० से अधिक सफेद मक्खी दिखें तो तुरंत कृषि वैज्ञानिक से संपर्क करें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Aggressive, rotating systemic insecticide management targeting both adult whiteflies and nymphs.",
                "mr": "पांढऱ्या माशीच्या प्रौढ व पिल्लांच्या नियंत्रणासाठी आंतरप्रवाही कीटकनाशकांची आलटून-पालटून फवारणी.",
                "hi": "सफेद मक्खी के वयस्क और निम्फ के खात्मे हेतु प्रणालीगत कीटनाशकों का बारी-बारी से छिड़काव।"
            },
            "formulations": [
                {"name": "Diafenthiuron 50% WP", "dosage": "1.2 g per Liter water", "phi_days": "7 days"},
                {"name": "Spiromesifen 22.9% SC", "dosage": "1.0 ml per Liter water", "phi_days": "5 days"},
                {"name": "Thiamethoxam 25% WG", "dosage": "0.3 g per Liter water", "phi_days": "5 days"}
            ],
            "application_timing": {
                "en": "Spray late afternoon, covering undersides of leaves where whitefly nymphs reside.",
                "mr": "संध्याकाळी पानांच्या मागच्या बाजूस चांगल्या प्रकारे औषध बसेल अशा रीतीने फवारणी करा.",
                "hi": "शाम के समय पत्तियों के निचले हिस्से को अच्छी तरह भिगोते हुए छिड़काव करें।"
            },
            "safety_precautions": {
                "en": "Rotate chemical modes of action to prevent rapid neonicotinoid resistance. Wear protective face shield.",
                "mr": "कीटकांमध्ये प्रतिकारशक्ती तयार होऊ नये म्हणून एकाच औषधाची वारंवार फवारणी करू नका.",
                "hi": "प्रतिरोधक क्षमता से बचने के लिए एक ही कीटनाशक का बार-बार प्रयोग न करें।"
            },
            "irrigation_guidance": {"en": "Maintain consistent drip irrigation; avoid drought stress.", "mr": "ठिबक सिंचनाने नियमित पाणी द्या.", "hi": "नियमित रूप से ड्रिप द्वारा संतुलित जल दें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Mass trapping combined with entomopathogenic fungi and high-potency neem seed kernel extract.",
                "mr": "पिवळे सापळे, जैविक बुरशी आणि कडुनिंब अर्काचा एकात्मिक वापर.",
                "hi": "पीले चिपचिपे कार्ड, जैविक कवक और उच्च गुणवत्ता वाले नीम अर्क का उपयोग।"
            },
            "bio_agents": [
                {"name": "Verticillium lecanii (Beauveria bassiana)", "dosage": "5 g per Liter water (spray in high humidity evening)"},
                {"name": "Neem Seed Kernel Extract (NSKE 5%)", "dosage": "50 g soaked overnight in 1 Liter water"},
                {"name": "Yellow Sticky Traps", "dosage": "20 traps per acre placed 30 cm above crop canopy"}
            ],
            "sanitation": {"en": "Remove weeds like Parthenium and Datura which act as alternate whitefly reservoirs.", "mr": "गाजरगवत व धोत्रा यांसारखी तणे नष्ट करा.", "hi": "खेत के आसपास से गाजरघास और खरपतवार नष्ट करें।"},
            "soil_health": {"en": "Apply silica solubilizing bacteria to strengthen leaf epidermal tissue against piercers.", "mr": "सिलिकॉन विरघळणाऱ्या जिवाणूंचा वापर करा.", "hi": "पत्तियों को मजबूत बनाने हेतु सिलिकॉन का प्रयोग करें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹750 - ₹1200 / acre", "organic": "₹400 - ₹600 / acre"},
            "speed": {"chemical": "Fast knockdown of vectors (12 - 24 hrs)", "organic": "Biological suppression (3 - 5 days)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "0 Days"},
            "eco_impact": {"chemical": "Toxic to bees if applied during flowering", "organic": "Safe for natural predators like ladybird beetles"}
        }
    },

    "Tomato_Bacterial_spot": {
        "scientific_pathogen": "Xanthomonas vesicatoria / campestris pv. vesicatoria (Bacterium)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Bacterial Spot",
            "mr": "जिवाणूजन्य ठिपके (बॅक्टेरियल स्पॉट)",
            "hi": "जीवाणु धब्बा रोग (बैक्टीरियल स्पॉट)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Small (2-3 mm), dark, water-soaked circular to angular lesions on foliage with greasy appearance",
                "Lesions develop a distinctive narrow yellow halo; centers dry out, tear, and drop out (shot-hole)",
                "Small, raised, scab-like blister spots on green fruit surrounded by a water-soaked border"
            ],
            "mr": [
                "पानांवर लहान (२-३ मिमी), पाण्याचे शिंतोडे पडल्यासारखे तेलकट काळपट ठिपके दिसतात",
                "ठिपक्यांभोवती पिवळसर वलय दिसते; नंतर ठिपक्यांचा मधला भाग सुकतो आणि पानात भोके पडतात",
                "हिरव्या फळांवर खडबडीत, पुटकुळीसारखे काळे डाग पडतात"
            ],
            "hi": [
                "पत्तियों पर छोटे (२-३ मिमी) पानी से भीगे हुए तैलीय काले धब्बे",
                "धब्बों के चारों ओर पीले रंग का घेरा और बीच का हिस्सा सूखकर छेद बन जाना",
                "कच्चे फलों पर उभरे हुए खुरदरे छाले जैसे धब्बे"
            ]
        },
        "causes": {
            "en": "Bacterial pathogen Xanthomonas penetrating through stomata or mechanical wounds.",
            "mr": "झांथोमोनस जिवाणू, जो पानांच्या छिद्रांतून किंवा झाडाला झालेल्या जखमांमधून आत शिरतो.",
            "hi": "जैंथोमोनास जीवाणु जो पत्तियों के रंध्रों अथवा घावों से पौधे में प्रवेश करता है।"
        },
        "environmental_factors": {
            "en": "Warm temperatures (24°C - 30°C), heavy rainfall, high humidity (>80%), and wind-driven rainstorms.",
            "mr": "२४° ते ३०° से. उबदार तापमान, संततधार पाऊस, ढगाळ हवामान व सोसाट्याचा वारा.",
            "hi": "२४° से ३०° सेल्सियस तापमान, भारी वर्षा और ८०% से अधिक आर्द्रता।"
        },
        "spread_mode": {
            "en": "Splashing rain, overhead irrigation water, infected transplants, and contaminated farm implements.",
            "mr": "पावसाचे तुषार, वरून पाणी देणे, रोगट रोपे आणि काम करताना अवजारांद्वारे.",
            "hi": "बारिश के छींटों, फव्वारा सिंचाई और कृषि उपकरणों के माध्यम से।"
        },
        "immediate_actions": {
            "en": [
                "Avoid touching, pruning, or cultivating plants while foliage is wet from dew or rain.",
                "Immediately cease all overhead sprinkler irrigation.",
                "Spray copper bactericide promptly after storm or hail events to protect plant wounds."
            ],
            "mr": [
                "पाने दव किंवा पावसाने ओली असताना शेतात काम किंवा छाटणी करणे टाळा.",
                "स्प्रिंकलरने पाणी देणे त्वरित बंद करा.",
                "वादळ किंवा गारपिटीनंतर झाडांना झालेल्या जखमा भरण्यासाठी त्वरित कॉपरची फवारणी करा."
            ],
            "hi": [
                "पत्तियां गीली होने की स्थिति में खेत में कोई कार्य अथवा छंटाई न करें।",
                "फव्वारा सिंचाई तुरंत रोक दें।",
                "आंधी या ओलावृष्टि के बाद घावों पर कॉपर का छिड़काव तुरंत करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Hot water seed treatment at 50°C for 25 minutes to eliminate internal seed-borne bacteria.",
                "Rotate ground out of tomato, pepper, and eggplant for at least 2 consecutive growing seasons.",
                "Grow certified disease-free nursery seedlings."
            ],
            "mr": [
                "पेरणीपूर्वी बियाण्यांवर ५०° से. तापमानाच्या कोमट पाण्यात २५ मिनिटे बीजप्रक्रिया करा.",
                "टोमॅटो, वांगी आणि मिरची पिकांनंतर किमान २ हंगाम इतर पिके घ्या.",
                "फक्त प्रमाणित आणि निरोगी रोपवाटिकेतील रोपे वापरा."
            ],
            "hi": [
                "बीजों को बोने से पहले ५०° सेल्सियस गर्म पानी में २५ मिनट तक उपचारित करें।",
                "टमाटर, बैंगन और मिर्च के साथ कम से कम २ साल का फसल चक्र रखें।",
                "प्रमाणित रोगमुक्त नर्सरी से ही पौध खरीदें।"
            ]
        },
        "expert_threshold": {
            "en": "If bacterial spotting appears during early flowering or fruit-set stage, prompt bactericide intervention is essential.",
            "mr": "फुलधारणा किंवा फळधारणेच्या सुरुवातीला ठिपके दिसल्यास त्वरित कृषी तज्ज्ञांशी संपर्क साधा.",
            "hi": "फूल आने या फल बनने के समय धब्बे दिखने पर तुरंत विशेषज्ञ की सलाह लें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Fixed copper bactericide combined with antibiotic bactericide to manage copper-resistant strains.",
                "mr": "कॉपरयुक्त जिवाणूनाशक आणि प्रतिजैविक (अँटिबायोटिक) यांचे संयुक्त मिश्रण फवारणे.",
                "hi": "कॉपर आधारित जीवाणुनाशी और एंटीबायोटिक के सम्मिश्रण का छिड़काव।"
            },
            "formulations": [
                {"name": "Copper Oxychloride 50% WP + Streptocycline (90:10)", "dosage": "2.5 g COC + 0.1 g Streptocycline per Liter water", "phi_days": "7 days"},
                {"name": "Kasugamycin 3% SL", "dosage": "1.5 to 2.0 ml per Liter water", "phi_days": "5 days"},
                {"name": "Copper Hydroxide 77% WP", "dosage": "2.0 g per Liter water", "phi_days": "5 days"}
            ],
            "application_timing": {
                "en": "Apply at the first sign of symptoms; reapply every 7-10 days during rainy weather.",
                "mr": "रोगाची पहिली लक्षणे दिसताच फवारणी करा; पावसाळी वातावरणात दर ७-१० दिवसांनी पुनरावृत्ती करा.",
                "hi": "शुरुआती लक्षण दिखते ही छिड़काव करें; बारिश में ७-१० दिन के अंतराल पर दोहराएं।"
            },
            "safety_precautions": {
                "en": "Avoid spraying copper under direct hot sun to prevent foliar phytotoxicity (leaf scorch).",
                "mr": "कडक उन्हात कॉपरची फवारणी करू नका, अन्यथा पाने करपू शकतात.",
                "hi": "कड़क धूप में कॉपर का छिड़काव न करें जिससे पत्तियां झुलसने से बचें।"
            },
            "irrigation_guidance": {"en": "Drip irrigation only. Mulch heavily to stop soil splashing.", "mr": "फक्त ठिबक सिंचन वापरा. मातीचे आच्छादन (मल्चिंग) करा.", "hi": "केवल ड्रिप सिंचाई और मल्चिंग का उपयोग करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Bio-bactericidal inoculation using Pseudomonas and botanical extracts.",
                "mr": "स्यूडोमोनास फ्लुरोसेन्स आणि आंबट ताकाची फवारणी करून जिवाणूंचा नायनाट करणे.",
                "hi": "स्यूडोमोनास फ्लोरोसेंस और खट्टी छाछ के छिड़काव द्वारा जैविक रोकथाम।"
            },
            "bio_agents": [
                {"name": "Pseudomonas fluorescens 1% WP", "dosage": "5 g per Liter water as foliar spray every 10 days"},
                {"name": "Sour Buttermilk (5-7 days fermented) + Hing", "dosage": "50 ml buttermilk + 0.5 g asafoetida per Liter water"},
                {"name": "Bordeaux Mixture 1% (Copper sulfate + Slaked lime)", "dosage": "10 g CuSO4 + 10 g Lime in 1 Liter water"}
            ],
            "sanitation": {"en": "Bury all diseased plant debris deep into trenches away from fields.", "mr": "रोगट पाने व फळे खड्ड्यात गाडून नष्ट करा.", "hi": "रोगग्रस्त पत्तियों व फलों को गहरे गड्ढे में दबाएं।"},
            "soil_health": {"en": "Incorporate well-rotted cow dung compost enriched with Trichoderma.", "mr": "ट्रायकोडर्मायुक्त शेणखताचा जमिनीत वापर करा.", "hi": "ट्राइकोडर्मा युक्त सड़ी गोबर की खाद डालें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹550 - ₹850 / acre", "organic": "₹200 - ₹400 / acre"},
            "speed": {"chemical": "Moderate (48 - 72 hrs)", "organic": "Gradual preventative (4 - 6 days)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "0 - 1 Days"},
            "eco_impact": {"chemical": "Low copper accumulation risk if overused", "organic": "Environmentally neutral and organic certifiable"}
        }
    },

    "Tomato_Early_blight": {
        "scientific_pathogen": "Alternaria solani (Fungus)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Early Blight (Alternaria Leaf Spot)",
            "mr": "अल्टरनेरिया करपा (अर्ली ब्लाइट)",
            "hi": "अगेती झुलसा रोग (अर्ली ब्लाइट)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Dark brown to black necrotic spots with concentric ring pattern ('bullseye' or target rings)",
                "Yellow chlorotic tissue developing around lesions, progressing upwards from older lower leaves",
                "Stem cankers ('collar rot') at ground level and leathery sunken dark lesions at fruit stem ends"
            ],
            "mr": [
                "पानांवर तपकिरी-काळे गोलाकार डाग ज्यामध्ये एकाआड एक वलये (चकती/बुलसाई) दिसतात",
                "डागांभोवती पान पिवळे पडते आणि हा रोग खालच्या जुन्या पानांपासून सुरू होऊन वर पसरतो",
                "खोड जमिनीजवळ काळे पडणे (कॉलर रॉट) आणि फळांच्या देठाजवळ काळे चामड्यासारखे डाग पडणे"
            ],
            "hi": [
                "पत्तियों पर भूरे-काले गोल धब्बे जिनमें गोल छल्ले (बुल्सआई पैटर्न) बनते हैं",
                "धब्बों के आसपास का हिस्सा पीला पड़ना, रोग निचली पुरानी पत्तियों से शुरू होकर ऊपर बढ़ता है",
                "तने पर जमीन के पास कालापन और फलों के डंठल के पास धंसे हुए चमड़े जैसे काले धब्बे"
            ]
        },
        "causes": {
            "en": "Fungal pathogen Alternaria solani surviving in solanaceous plant residues and volunteer seedlings.",
            "mr": "अल्टरनेरिया सोलॅनी ही बुरशी, जी जमिनीत आणि पिकांच्या अवशेषांवर दीर्घकाळ टिकून राहते.",
            "hi": "अल्टरनेरिया सोलानी कवक जो मिट्टी और पिछली फसल के अवशेषों में रहता है।"
        },
        "environmental_factors": {
            "en": "Alternating wet and dry weather, temperatures between 24°C - 29°C, and heavy dew periods.",
            "mr": "दमट व कोरडे हवामान, २४° ते २९° से. तापमान आणि सकाळचे धुके किंवा दवबिंदू.",
            "hi": "बारी-बारी से गीला और सूखा मौसम, २४° से २९° सेल्सियस तापमान और अधिक ओस।"
        },
        "spread_mode": {
            "en": "Windborne conidia, splashing water, insects, and contaminated tools.",
            "mr": "वाऱ्यातून उडणारे बुरशीचे बीजाणू, पावसाचे पाणी आणि किडींद्वारे.",
            "hi": "हवा, बारिश के पानी के छींटों और संक्रमित औजारों से।"
        },
        "immediate_actions": {
            "en": [
                "Prune off the lowest 30 cm of leaves touching the soil once plants are established.",
                "Apply organic or silver-black plastic mulch to block soil-borne fungal spores.",
                "Ensure balanced nitrogen fertilization; avoid excessive nitrogen which produces soft, susceptible foliage."
            ],
            "mr": [
                "रोप मोठे झाल्यावर जमिनीला टेकलेली खालची ३० सेमी पर्यंतची पाने छाटून टाका.",
                "मातीतून बुरशी वर येऊ नये म्हणून प्लास्टिक किंवा गवताचे मल्चिंग करा.",
                "नत्राचा (युरिया) अतिवापर टाळा; नत्र जास्त झाल्यास झाडांची पाने मऊ होऊन रोगाला लवकर बळी पडतात."
            ],
            "hi": [
                "पौधा बड़ा होने पर जमीन से छूती हुई निचली ३० सेमी पत्तियों को काट दें।",
                "मिट्टी से बीजाणुओं को पत्तियों तक पहुंचने से रोकने के लिए मल्चिंग करें।",
                "यूरिया का अत्यधिक उपयोग न करें, इससे पत्तियां कोमल होकर जल्दी रोगग्रस्त होती हैं।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Stake plants securely to keep foliage off the damp ground.",
                "Practice a minimum 2-year crop rotation without potato, brinjal, or pepper.",
                "Plant certified disease-free seeds or seedlings."
            ],
            "mr": [
                "झाडांना बांबू किंवा तारेचा आधार देऊन ताठ बांधा जेणेकरून झाड जमिनीवर लोळणार नाही.",
                "बटाटा, वांगी किंवा मिरची या पिकांनंतर टोमॅटो घेणे टाळा.",
                "नेहमी निरोगी व दर्जेदार रोपांचीच निवड करा."
            ],
            "hi": [
                "पौधों को बांस या डंडे के सहारे बांधें ताकि वे जमीन पर न लटकें।",
                "आलू, बैंगन या मिर्च के बाद कम से कम २ साल तक टमाटर न लगाएं।",
                "रोगमुक्त प्रमाणित बीजों की ही बुवाई करें।"
            ]
        },
        "expert_threshold": {
            "en": "If early blight advances past the lower third of the canopy before flowering, chemical intervention is advised.",
            "mr": "फुलधारणेपूर्वी झाडाच्या मध्यभागापर्यंत करपा पोहोचल्यास कृषी सल्लागाराशी त्वरित चर्चा करा.",
            "hi": "फूल आने से पहले यदि झुलसा पौधे के बीच के हिस्से तक पहुंच जाए तो तुरंत कदम उठाएं।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Alternating contact protectants (e.g. Mancozeb) with systemic translaminar fungicides (e.g. Difenoconazole).",
                "mr": "स्पर्शजन्य बुरशीनाशक (उदा. मँकोझेब) आणि आंतरप्रवाही बुरशीनाशक (उदा. डायफेनोकोनॅझोल) आलटून-पालटून वापरणे.",
                "hi": "स्पर्श कवकनाशी (मैनकोजेब) और अंतःप्रवाही कवकनाशी (डाइफेनोकोनाजोल) का क्रमवार उपयोग।"
            },
            "formulations": [
                {"name": "Mancozeb 75% WP", "dosage": "2.5 g per Liter water", "phi_days": "7 days"},
                {"name": "Difenoconazole 25% EC", "dosage": "0.5 to 1.0 ml per Liter water", "phi_days": "7 days"},
                {"name": "Tebuconazole 50% + Trifloxystrobin 25% WG", "dosage": "0.7 g per Liter water", "phi_days": "5 days"}
            ],
            "application_timing": {
                "en": "Spray early morning on clear days. Ensure thorough coverage of both top and bottom of leaves.",
                "mr": "सकाळी स्वच्छ सूर्यप्रकाश असताना दोन्ही बाजूंनी पाने भिजतील अशी फवारणी करा.",
                "hi": "सुबह के समय पत्तियों के दोनों तरफ अच्छी तरह भीगने लायक छिड़काव करें।"
            },
            "safety_precautions": {
                "en": "Strictly follow 7-day PHI before harvesting. Wear mask and rubber gloves during tank mixing.",
                "mr": "कापणीपूर्वी किमान ७ दिवसांचा कालावधी ठेवा. औषध मिसळताना मास्क व हातमोजे वापरा.",
                "hi": "तुड़ाई से कम से कम ७ दिन पहले छिड़काव बंद करें। सुरक्षा उपकरण पहनें।"
            },
            "irrigation_guidance": {"en": "Water at root level using drip lines in the morning.", "mr": "सकाळी ठिबक सिंचनाने मुळांपाशी पाणी द्या.", "hi": "सुबह के समय ड्रिप से जड़ों में पानी दें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Preventative bio-fungicide inoculation with Trichoderma and cow urine fermented decoctions.",
                "mr": "ट्रायकोडर्मा व्हिरीडी आणि गोमूत्रयुक्त वनस्पती काढा (दशपर्णी अर्क) वापरून रोगाचा प्रतिबंध.",
                "hi": "ट्राइकोडर्मा विरिडी और गोमूत्र युक्त दशपर्णी अर्क द्वारा प्राकृतिक रोकथाम।"
            },
            "bio_agents": [
                {"name": "Trichoderma viride 1% WP", "dosage": "5 g per Liter water foliar spray and root drench"},
                {"name": "Cow Urine (Gomutra) 10% + Hing solution", "dosage": "100 ml gomutra + 1 g hing per Liter water"},
                {"name": "Copper Hydroxide or Bordeaux Mixture (0.5%)", "dosage": "5 g per Liter water"}
            ],
            "sanitation": {"en": "Strip off diseased leaves every 5 days and burn immediately.", "mr": "बाधित पाने ५ दिवसांच्या अंतराने खुडून जाळून टाका.", "hi": "रोगग्रस्त पत्तियों को हर ५ दिन में तोड़कर जला दें।"},
            "soil_health": {"en": "Apply neem cake @ 200 kg/acre to soil during land preparation.", "mr": "जमीन तयार करताना एकरी २०० किलो निंबोळी पेंड मिसळा.", "hi": "खेत की तैयारी के समय प्रति एकड़ २०० किलो नीम की खली डालें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹600 - ₹950 / acre", "organic": "₹250 - ₹450 / acre"},
            "speed": {"chemical": "Fast curative (24 - 48 hours)", "organic": "Moderate preventative (3 - 5 days)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "0 Days"},
            "eco_impact": {"chemical": "Observe water source safety buffer", "organic": "Safe for soil organisms, earthworms, and pollinators"}
        }
    },

    "Tomato_healthy": {
        "scientific_pathogen": "None (Plant is Healthy and Vigorous)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Healthy Tomato Foliage",
            "mr": "निरोगी टोमॅटोचे रोप",
            "hi": "स्वस्थ टमाटर का पौधा"
        },
        "is_healthy": True,
        "symptoms": {
            "en": [
                "Lush green, firm leaves without spots, curling, or chlorotic yellowing",
                "Sturdy upright stems with active vegetative vigor and healthy flower clusters",
                "Uniform fruit development free from lesions, rot, or blistering"
            ],
            "mr": [
                "टवटवीत हिरवीगार पाने, ज्यावर कोणताही डाग, सुरकुती किंवा पिवळेपणा नाही",
                "मजबूत खोड, जोमदार वाढ आणि निरोगी फुलोरा",
                "फळांचा एकसारखा आकार, डाग व सड नसलेली निरोगी फळे"
            ],
            "hi": [
                "चमकदार हरी और मजबूत पत्तियां जिन पर कोई धब्बा, सिकुड़न या पीलापन नहीं है",
                "मजबूत तना, अच्छी वानस्पतिक वृद्धि और स्वस्थ फूलों के गुच्छे",
                "बिना किसी दाग-धब्बे के एक समान स्वस्थ फल"
            ]
        },
        "causes": {
            "en": "Optimal agronomic care, balanced nutrition, and absence of pathogenic infection.",
            "mr": "उत्कृष्ट कृषी व्यवस्थापन, संतुलित खत व्यवस्थापन आणि रोगजंतूंचा अभाव.",
            "hi": "उत्कृष्ट कृषि प्रबंधन, संतुलित पोषण और रोगजनकों की अनुपस्थिति।"
        },
        "environmental_factors": {
            "en": "Favorable diurnal temperature (20°C-28°C), adequate sunlight, and proper drainage.",
            "mr": "योग्य तापमान (२०° ते २८° से.), भरपूर सूर्यप्रकाश आणि पाण्याचा उत्तम निचरा.",
            "hi": "अनुकूल तापमान (२०° से २८° सेल्सियस), पर्याप्त धूप और जल निकासी।"
        },
        "spread_mode": {"en": "N/A — Crop is currently healthy.", "mr": "लागू नाही — पीक सध्या निरोगी आहे.", "hi": "लागू नहीं — फसल वर्तमान में स्वस्थ है।"},
        "immediate_actions": {
            "en": [
                "Continue routine preventative scouting twice weekly.",
                "Maintain balanced N-P-K fertigation and trace micronutrient supplementation (Boron, Zinc, Calcium).",
                "Do not apply unneeded pesticides when the crop shows no signs of infection."
            ],
            "mr": [
                "आठवड्यातून किमान दोनदा पिकाची पाहणी चालू ठेवा.",
                "संतुलित खते आणि सूक्ष्मअन्नद्रव्ये (कॅल्शियम, बोरॉन, झिंक) ठिबकमधून देणे चालू ठेवा.",
                "कोणतीही लक्षणे नसताना अनावश्यक रासायनिक औषधांची फवारणी करू नका."
            ],
            "hi": [
                "सप्ताह में दो बार खेत का नियमित निरीक्षण जारी रखें।",
                "संतुलित खाद और सूक्ष्म पोषक तत्वों (कैल्शियम, बोरॉन, जिंक) की खुराक देते रहें।",
                "पौधे स्वस्थ होने पर किसी अनावश्यक कीटनाशक का छिड़काव न करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Keep yellow and blue sticky traps in place for proactive pest surveillance.",
                "Maintain mulch to suppress weeds and conserve root moisture.",
                "Maintain proper irrigation scheduling based on evapotranspiration."
            ],
            "mr": [
                "किडींचा मागोवा घेण्यासाठी पिवळे व निळे चिकट सापळे शेतात लावून ठेवा.",
                "जमिनीतील ओलावा टिकवण्यासाठी आणि तण रोखण्यासाठी आच्छादन (मल्चिंग) चालू ठेवा.",
                "हवामानानुसार पाण्याचे योग्य नियोजन करा."
            ],
            "hi": [
                "कीट निगरानी हेतु पीले व नीले चिपचिपे कार्ड खेत में लगाए रखें।",
                "खरपतवार नियंत्रण और नमी संरक्षण के लिए मल्चिंग बनाए रखें।",
                "मौसम के अनुसार संतुलित सिंचाई करें।"
            ]
        },
        "expert_threshold": {
            "en": "No immediate intervention required. Consult agronomist only if unusual wilting or nutrient deficiency symptoms develop.",
            "mr": "सध्या उपचाराची गरज नाही. पाने अचानक पिवळी पडल्यास किंवा सुकू लागल्यास कृषी तज्ज्ञांचा सल्ला घ्या.",
            "hi": "वर्तमान में किसी उपचार की आवश्यकता नहीं है। यदि अचानक कोई लक्षण दिखें तो ही विशेषज्ञ से मिलें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Prophylactic plant vigor and nutrient maintenance only. Strictly avoid prophylactic antibiotic or broad-spectrum insecticide sprays.",
                "mr": "फक्त पिकाची ताकद टिकवण्यासाठी सूक्ष्मअन्नद्रव्यांचा पुरवठा करा; अनावश्यक रासायनिक फवारणी टाळा.",
                "hi": "केवल सूक्ष्म पोषक तत्वों का संतुलित प्रयोग करें; बिना कारण रासायनिक कीटनाशक न छिड़कें।"
            },
            "formulations": [
                {"name": "Water Soluble NPK 19:19:19", "dosage": "3-5 g per Liter water / 2 kg per acre fertigation", "phi_days": "N/A"},
                {"name": "Chelated Micronutrient Grade II", "dosage": "1.5 g per Liter water foliar", "phi_days": "N/A"}
            ],
            "application_timing": {"en": "Early morning fertigation.", "mr": "सकाळी ठिबकमधून खत द्या.", "hi": "सुबह के समय ड्रिप से खाद दें।"},
            "safety_precautions": {"en": "Follow proper dilution ratios to avoid salt stress.", "mr": "खताचे प्रमाण योग्य ठेवा जेणेकरून मुळांना इजा होणार नाही.", "hi": "खाद की मात्रा संतुलित रखें।"},
            "irrigation_guidance": {"en": "Consistent drip irrigation.", "mr": "नियमित ठिबक सिंचन.", "hi": "नियमित ड्रिप सिंचाई।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Soil health enhancement through regular biostimulants, Jeevamrut, and vermicompost wash.",
                "mr": "जिवामृत, गांडूळ खताचा अर्क आणि ह्युमिक ॲसिड देऊन झाडांची नैसर्गिक प्रतिकारशक्ती वाढवणे.",
                "hi": "जीवामृत, वर्मीवाश और जैविक खादों द्वारा मिट्टी और पौधे की प्राकृतिक शक्ति बढ़ाना।"
            },
            "bio_agents": [
                {"name": "Jeevamrut / Panchagavya", "dosage": "200 L/acre drench or 30 ml/L spray"},
                {"name": "Pseudomonas fluorescens (Prophylactic)", "dosage": "5 g per Liter water every 20 days"},
                {"name": "Seaweed Biostimulant Extract", "dosage": "2 ml per Liter water"}
            ],
            "sanitation": {"en": "Routine field weeding.", "mr": "वेळोवेळी खुरपणी करून शेत स्वच्छ ठेवा.", "hi": "नियमित निराई-गुड़ाई कर खेत स्वच्छ रखें।"},
            "soil_health": {"en": "Add compost top-dressing around root zones.", "mr": "मुळांभोवती चांगले कुजलेले खत द्या.", "hi": "जड़ों के पास सड़ा हुआ कंपोस्ट डालें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹300 - ₹500 / acre (Nutrients only)", "organic": "₹150 - ₹300 / acre (Bio-stimulants)"},
            "speed": {"chemical": "Normal maintenance", "organic": "Normal maintenance"},
            "phi": {"chemical": "0 Days", "organic": "0 Days"},
            "eco_impact": {"chemical": "Safe when used as fertilizer", "organic": "100% sustainable and soil-regenerative"}
        }
    },

    "Tomato_Late_blight": {
        "scientific_pathogen": "Phytophthora infestans (Oomycete)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Late Blight (Phytophthora Blight)",
            "mr": "लेट ब्लाइट (उशीरा येणारा करपा / तांब्या)",
            "hi": "पछेती झुलसा रोग (लेट ब्लाइट)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Large, irregular water-soaked pale-green to brown lesions on leaves that expand rapidly",
                "Delicate white, cottony downy fungal mildew visible on the undersides of leaves during high humidity",
                "Dark brown, firm, greasy lesions on green fruit, turning leathery with potential whole-crop collapse in 7-10 days"
            ],
            "mr": [
                "पानांवर मोठे, पाण्याचे शिंतोडे पडल्यासारखे अनियमित हिरवट-तपकिरी डाग जे वेगाने पसरतात",
                "जास्त आर्द्रतेमध्ये पानांच्या खालच्या बाजूला पांढरी कापसासारखी नाजूक बुरशीची लव दिसते",
                "फळांवर कडक, काळे-तपकिरी खडबडीत चट्टे पडतात आणि संपूर्ण पीक अवघ्या आठवडाभरात करपून जाते"
            ],
            "hi": [
                "पत्तियों पर बड़े, अनियमित, पानी से भीगे हुए हरे-भूरे धब्बे जो बहुत तेजी से बढ़ते हैं",
                "अधिक नमी में पत्तियों की निचली सतह पर सफेद रंग की रुई जैसी फफूंद दिखाई देती है",
                "कच्चे फलों पर गहरे भूरे, कड़े और तैलीय धब्बे; पूरी फसल ७-१० दिनों में नष्ट हो सकती है"
            ]
        },
        "causes": {
            "en": "Aggressive oomycete Phytophthora infestans capable of devastating entire fields under cool, moist conditions.",
            "mr": "फायटोप्थोरा इन्फेस्टन्स ही अत्यंत विध्वंसक बुरशी (ऊमायसीट), जी संपूर्ण शेताचा नाश करू शकते.",
            "hi": "फाइटोफ्थोरा इन्फेस्टान्स नामक अत्यधिक आक्रामक कवक जो पूरी फसल को तबाह कर सकता है।"
        },
        "environmental_factors": {
            "en": "Cool to moderate temperatures (15°C - 22°C), fog, heavy dew, continuous drizzle, and relative humidity >90%.",
            "mr": "थंड व दमट हवामान (१५° ते २२° से. तापमान), धुके, संततधार पाऊस किंवा रिमझिम आणि ९०% पेक्षा जास्त आर्द्रता.",
            "hi": "ठंडा और नम मौसम (१५° से २२° सेल्सियस), कोहरा, भारी ओस और ९०% से अधिक आर्द्रता।"
        },
        "spread_mode": {
            "en": "Windborne sporangia travelling miles, splashing rain droplets, and infected seed tubers/cull piles.",
            "mr": "वाऱ्यातून कित्येक किलोमीटर वाहून जाणारे बुरशीचे बीजाणू आणि पावसाचे पाणी.",
            "hi": "हवा में मीलों दूर तक उड़ने वाले बीजाणु और वर्षा के पानी के छींटे।"
        },
        "immediate_actions": {
            "en": [
                "EMERGENCY ACTION: Late blight is a community epidemic disease. Scout fields daily.",
                "Immediately prune and bag severely blighted foliage; never drop infected tissue onto the ground.",
                "Stop all overhead irrigation immediately; inspect neighboring potato and tomato fields."
            ],
            "mr": [
                "तातडीची उपाययोजना: हा रोग अत्यंत वेगाने पसरतो; दररोज शेताची काळजीपूर्वक पाहणी करा.",
                "बाधित पाने व फांद्या ताबडतोब कापून पिशवीत भरा आणि शेताबाहेर नेऊन जाळून टाका.",
                "स्प्रिंकलर ताबडतोब बंद करा आणि आजूबाजूच्या बटाटा व टोमॅटो पिकांवर नजर ठेवा."
            ],
            "hi": [
                "आपातकालीन कार्रवाई: यह बीमारी बहुत तेजी से फैलती है; रोज खेत की जांच करें।",
                "संक्रमित पत्तियों को तुरंत काटकर प्लास्टिक बैग में भरकर जला दें।",
                "फव्वारा सिंचाई तुरंत रोक दें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Plant late-blight resistant hybrids (e.g., varieties with Ph-2 and Ph-3 genes).",
                "Destroy all wild solanaceous weeds and volunteer tomato/potato shoots near the plot.",
                "Avoid planting in low-lying frost pockets with poor air movement."
            ],
            "mr": [
                "लेट ब्लाइटला प्रतिकार करणारे संकरित बियाणे वापरा (Ph-2 किंवा Ph-3 जनुक असलेले).",
                "शेताभोवती उगवणारी जंगली झाडे व सोलानेसी कुळातील तण नष्ट करा.",
                "ज्या ठिकाणी हवा खेळती राहत नाही किंवा धुके साचून राहते अशा सखल भागात लागवड टाळा."
            ],
            "hi": [
                "प्रतिरोधी संकरित किस्मों का चयन करें।",
                "खेत के आसपास के जंगली पौधों और खरपतवार को नष्ट करें।",
                "जहां हवा का आवागमन कम हो या कोहरा जमता हो, वहां बुवाई न करें।"
            ]
        },
        "expert_threshold": {
            "en": "CRITICAL: Contact agricultural extension officer IMMEDIATELY upon first confirmed sighting in your taluka/district.",
            "mr": "अति महत्त्वाचे: शेतात लेट ब्लाइटची पहिली लक्षणे दिसताच त्वरित तालुका कृषी अधिकारी किंवा केव्हीकेशी संपर्क साधा.",
            "hi": "अति आवश्यक: क्षेत्र में लक्षण दिखते ही तुरंत कृषि विज्ञान केंद्र या कृषि अधिकारी को सूचित करें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Rapid intervention with specialized oomycete-specific systemic fungicides containing translaminar and curatively active molecules.",
                "mr": "लेट ब्लाइटसाठी विशेष आंतरप्रवाही आणि स्पर्शजन्य बुरशीनाशकांची त्वरित फवारणी.",
                "hi": "विशेष प्रणालीगत कवकनाशी का तत्काल उपयोग जो पौधे के भीतर जाकर फफूंद को नष्ट करे।"
            },
            "formulations": [
                {"name": "Dimethomorph 50% WP + Mancozeb 75% WP", "dosage": "1.0 g Dimethomorph + 2.0 g Mancozeb per Liter water", "phi_days": "7 days"},
                {"name": "Cymoxanil 8% + Mancozeb 64% WP", "dosage": "2.0 g per Liter water", "phi_days": "7 days"},
                {"name": "Fenamidone 10% + Mancozeb 50% WG", "dosage": "2.5 g per Liter water", "phi_days": "5 days"},
                {"name": "Metalaxyl 8% + Mancozeb 64% WP", "dosage": "2.5 g per Liter water", "phi_days": "7 days"}
            ],
            "application_timing": {
                "en": "Spray immediately upon weather alert of foggy/drizzly conditions. Repeat at 5-7 day intervals if wet weather persists.",
                "mr": "धुक्याचे किंवा ढगाळ वातावरण होताच त्वरित फवारणी करा; पाऊस चालू राहिल्यास ५-७ दिवसांनी पुन्हा फवारा.",
                "hi": "कोहरा या बारिश का मौसम बनते ही तुरंत छिड़काव करें; ५-७ दिन में दोहराएं।"
            },
            "safety_precautions": {
                "en": "Wear protective gear (respirator, gloves, waterproof apron). Strictly adhere to pre-harvest intervals.",
                "mr": "फवारणी करताना पूर्ण काळजी घ्या (मास्क, हातमोजे). फवारणीनंतर ७ दिवस फळे तोडू नका.",
                "hi": "मास्क और दस्ताने पहनें। तुड़ाई से पूर्व निर्धारित दिनों का अंतर अवश्य रखें।"
            },
            "irrigation_guidance": {"en": "Withhold irrigation during cold foggy spells.", "mr": "थंडी व धुक्याच्या दिवसांत पाणी देणे मर्यादित ठेवा.", "hi": "ठंड और कोहरे के दौरान सिंचाई सीमित करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Preventative heavy copper sprays (Bordeaux mixture) combined with bio-protective Bacillus subtilis.",
                "mr": "रोग येण्यापूर्वीच बोर्डो मिश्रण (१%) किंवा कॉपरयुक्त जैविक घटकांचा प्रतिबंधात्मक वापर.",
                "hi": "रोग आने से पहले ही बोर्डो मिश्रण (१%) अथवा कॉपर आधारित जैविक घोल का छिड़काव।"
            },
            "bio_agents": [
                {"name": "Bordeaux Mixture 1% (Copper sulfate + quicklime)", "dosage": "10 g CuSO4 + 10 g Lime in 1 Liter water"},
                {"name": "Bacillus subtilis (Bio-fungicide 1x10^9 CFU)", "dosage": "5 g per Liter water foliar spray"},
                {"name": "Trichoderma harzianum", "dosage": "5 g per Liter water soil and foliar"}
            ],
            "sanitation": {"en": "Immediately torch or bury infected foliage in deep trenches.", "mr": "बाधित पाने जाळून टाका किंवा खड्ड्यात गाडा.", "hi": "संक्रमित पत्तियों को तुरंत जलाएं या गड्ढे में दबाएं।"},
            "soil_health": {"en": "Avoid excess nitrogen fertilizer which causes succulent vulnerable growth.", "mr": "नत्राचा (युरिया) अतिवापर पूर्णपणे टाळा.", "hi": "अत्यधिक यूरिया का प्रयोग बिल्कुल न करें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹900 - ₹1500 / acre", "organic": "₹450 - ₹700 / acre"},
            "speed": {"chemical": "Immediate curative (within 24 hours)", "organic": "Strictly preventative (limited once disease explodes)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "1 Day"},
            "eco_impact": {"chemical": "Moderate risk; use judiciously", "organic": "Low toxicity; acceptable in certified organic farming"}
        }
    },

    "Tomato_Leaf_Mold": {
        "scientific_pathogen": "Passalora fulva / Cladosporium fulvum (Fungus)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Leaf Mold",
            "mr": "पानावरील बुरशी (लीफ मोल्ड)",
            "hi": "पत्ती फफूंद रोग (लीफ मोल्ड)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Pale greenish to light yellow chlorotic spots on upper leaf surface with indefinite margins",
                "Dense, velvety olive-green to grayish-brown fungal downy growth on the underside corresponding to the spots",
                "Infected leaves curl, wither, turn yellowish-brown, and drop prematurely, progressing upwards"
            ],
            "mr": [
                "पानाच्या वरच्या बाजूला फिकट पिवळसर किंवा फिकट हिरवे डाग दिसतात",
                "पानाच्या खालच्या बाजूला डागांच्या जागी ऑलिव्ह-हिरवट किंवा काळपट-तपकिरी मखमली बुरशीची थर वाढते",
                "पाने वाळतात, चुरडतात आणि अकाली गळून पडतात, हा रोग खालच्या पानांपासून वर पसरतो"
            ],
            "hi": [
                "पत्तियों की ऊपरी सतह पर हल्के पीले या हरे धब्बे दिखाई देते हैं",
                "पत्तियों की निचली सतह पर मखमली जैतून-हरे या भूरे रंग की फफूंद की परत बन जाती है",
                "पत्तियां सूखकर मुड़ जाती हैं और समय से पहले गिरने लगती हैं"
            ]
        },
        "causes": {
            "en": "Fungal pathogen Passalora fulva thriving in poorly ventilated polyhouses, shade nets, and crowded fields.",
            "mr": "पासलोरा फुल्वा ही बुरशी, जी पॉलिहाऊस, शेडनेट किंवा दाट लागवड केलेल्या शेतात हवा खेळती नसताना वेगाने वाढते.",
            "hi": "पासालोरा फुल्वा कवक जो पॉलीहाउस, शेडनेट अथवा अधिक घनी बुवाई वाले खेतों में नमी के कारण पनपता है।"
        },
        "environmental_factors": {
            "en": "High relative humidity (>85%), warm temperatures (21°C - 26°C), and stagnant air circulation.",
            "mr": "८५% पेक्षा जास्त आर्द्रता, २१° ते २६° से. तापमान आणि हवा खेळती नसलेली जागा.",
            "hi": "८५% से अधिक आर्द्रता, २१° से २६° सेल्सियस तापमान और स्थिर हवा।"
        },
        "spread_mode": {
            "en": "Air currents, splashing water, insects, and clothing of field workers.",
            "mr": "हवेचे प्रवाह, पाण्याचे शिंतोडे, किडे आणि शेतमजुरांचे कपडे.",
            "hi": "हवा के झोंकों, पानी के छींटों और मजदूरों के कपड़ों के माध्यम से।"
        },
        "immediate_actions": {
            "en": [
                "Improve greenhouse and field ventilation; open polyhouse side curtains immediately.",
                "Prune lower suckers and dense older leaves to enhance sunlight penetration and airflow.",
                "Cease all evening waterings to allow foliage to dry completely before sunset."
            ],
            "mr": [
                "पॉलिहाऊस किंवा शेडनेटच्या बाजूचे पडदे वर करून हवा खेळती करा.",
                "झाडाची खालील जुनी पाने आणि अनावश्यक फुटवे छाटा जेणेकरून सूर्यप्रकाश झाडात शिरेल.",
                "संध्याकाळी पाणी देणे थांबवा, जेणेकरून सूर्यास्तापूर्वी पाने कोरडी होतील."
            ],
            "hi": [
                "पॉलीहाउस के पर्दे खोलकर हवा का आवागमन बढ़ाएं।",
                "निचली पत्तियां और अनावश्यक शाखाएं छांटें ताकि धूप अंदर तक पहुंचे।",
                "शाम को पानी देना बंद करें ताकि सूर्यास्त से पहले पत्तियां सूख जाएं।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Select tomato varieties possessing 'Cf' resistance genes (e.g., Cf-2, Cf-4, Cf-9).",
                "Ensure generous spacing between rows (at least 90 cm) and between plants (60 cm).",
                "Disinfect greenhouse interior structures with copper or chlorine solutions between crops."
            ],
            "mr": [
                "लीफ मोल्ड प्रतिरोधी वाण निवडा (Cf जनुक असलेले).",
                "ओळींमध्ये किमान ९० सेमी आणि रोपांमध्ये ६० सेमी अंतर ठेवा.",
                "हंगाम संपल्यावर पॉलिहाऊसच्या बांधकामावर जंतुनाशक फवारून निर्जंतुक करा."
            ],
            "hi": [
                "रोग प्रतिरोधी संकरित बीजों का प्रयोग करें।",
                "पंक्तियों के बीच ९० सेमी और पौधों के बीच ६० सेमी की दूरी रखें।",
                "फसल के बाद ग्रीनहाउस की संरचना को कीटाणुरहित करें।"
            ]
        },
        "expert_threshold": {
            "en": "Consult specialist if mold covers >20% of middle foliage, threatening photosynthetic yield during peak fruiting.",
            "mr": "फळधारणेच्या काळात २०% पेक्षा जास्त पाने बाधित झाल्यास त्वरित सल्ला घ्या.",
            "hi": "फल बनने के समय २०% से अधिक पत्तियां प्रभावित होने पर तुरंत परामर्श लें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Translaminar and multi-site protective fungicides targeting Passalora fungal wall synthesis.",
                "mr": "बुरशीची वाढ रोखण्यासाठी आंतरप्रवाही व स्पर्शजन्य बुरशीनाशकांची फवारणी.",
                "hi": "कवक की वृद्धि को रोकने हेतु प्रभावी कवकनाशी का छिड़काव।"
            },
            "formulations": [
                {"name": "Azoxystrobin 23% SC", "dosage": "1.0 ml per Liter water", "phi_days": "5 days"},
                {"name": "Chlorothalonil 75% WP", "dosage": "2.0 g per Liter water", "phi_days": "7 days"},
                {"name": "Difenoconazole 25% EC", "dosage": "0.5 ml per Liter water", "phi_days": "7 days"}
            ],
            "application_timing": {
                "en": "Spray in early morning, directing nozzles upwards to thoroughly coat undersides of leaves.",
                "mr": "सकाळी फवारणी करताना नोझल खालून वरच्या दिशेने ठेवून पानाच्या खालच्या भागावर औषध बसेल याची खात्री करा.",
                "hi": "सुबह छिड़काव करें और नोजल को नीचे से ऊपर की ओर रखकर पत्तियों के निचले हिस्से को भिगोएं।"
            },
            "safety_precautions": {
                "en": "Ventilate enclosed structures during and after spraying. Wear protective respirator.",
                "mr": "पॉलिहाऊसमध्ये फवारणी करताना मास्क वापरा आणि हवा खेळती ठेवा.",
                "hi": "पॉलीहाउस में छिड़काव करते समय मास्क लगाएं और वेंटिलेशन चालू रखें।"
            },
            "irrigation_guidance": {"en": "Strict drip irrigation. Avoid splashing water onto canopy.", "mr": "केवळ ठिबक सिंचन वापरा.", "hi": "केवल ड्रिप सिंचाई का प्रयोग करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Foliar bio-antagonism using Bacillus and potassium bicarbonate to alter leaf surface pH against fungus.",
                "mr": "पानावरील सामू (pH) बदलून बुरशी नष्ट करण्यासाठी पोटॅशियम बायकार्बोनेट आणि बॅसिलसचा वापर.",
                "hi": "पत्तियों की सतह का पीएच बदलकर कवक को नष्ट करने के लिए पोटैशियम बाइकार्बोनेट और जैविक कवकनाशी का प्रयोग।"
            },
            "bio_agents": [
                {"name": "Potassium Bicarbonate (Food Grade)", "dosage": "3 g per Liter water + 1 ml organic spreader"},
                {"name": "Bacillus amyloliquefaciens (Bio-agent)", "dosage": "3-5 g per Liter water"},
                {"name": "Neem Oil 10000 ppm", "dosage": "3 ml per Liter water"}
            ],
            "sanitation": {"en": "Remove and incinerate all velvety lower leaves.", "mr": "बुरशी आलेली सर्व पाने काढून जाळून टाका.", "hi": "फफूंद लगी निचली पत्तियों को हटाकर नष्ट करें।"},
            "soil_health": {"en": "Maintain balanced potassium to improve leaf cuticle toughness.", "mr": "पाने मजबूत होण्यासाठी पालाशयुक्त सेंद्रिय खते द्या.", "hi": "पत्तियों की मजबूती हेतु पोटाश युक्त जैविक खाद दें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹600 - ₹900 / acre", "organic": "₹300 - ₹500 / acre"},
            "speed": {"chemical": "Curative in 48 hours", "organic": "Suppressive in 3 - 5 days"},
            "phi": {"chemical": "5 - 7 Days", "organic": "0 Days"},
            "eco_impact": {"chemical": "Low if applied with proper PPE", "organic": "Completely safe, zero residue on produce"}
        }
    },

    "Tomato_Septoria_leaf_spot": {
        "scientific_pathogen": "Septoria lycopersici (Fungus)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Septoria Leaf Spot",
            "mr": "सेप्टोरिया पानावरील ठिपके (सेप्टोरिया लीफ स्पॉट)",
            "hi": "सेप्टोरिया पत्ती धब्बा रोग"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Numerous small, circular spots (1.5-3 mm) with dark brown margins and sunken grayish-white centers",
                "Tiny black specks (pycnidia fruiting bodies) visible in the gray center under close inspection",
                "Severely spotted leaves turn completely yellow, wither, and drop, exposing developing fruit to sunscald"
            ],
            "mr": [
                "पानांवर असंख्य लहान गोलाकार ठिपके (१.५-३ मिमी), ज्यांच्या कडा गडद तपकिरी व मध्यभाग राखाडी-पांढरा असतो",
                "ठिपक्यांच्या राखाडी मध्यभागात सूक्ष्म काळे दाणे (बुरशीची फळे/पिक्निडिया) दिसतात",
                "बाधित पाने पूर्ण पिवळी पडून गळतात, ज्यामुळे फळांवर थेट ऊन पडून फळे करपतात (सनस्कॅल्ड)"
            ],
            "hi": [
                "पत्तियों पर अनेक छोटे गोल धब्बे (१.५-३ मिमी) जिनके किनारे गहरे भूरे और केंद्र धूसर-सफेद होते हैं",
                "धब्बों के केंद्र में बारीक काले बिंदु (कवक के बीजाणु) दिखाई देते हैं",
                "प्रभावित पत्तियां पीली होकर गिर जाती हैं जिससे फलों पर सीधी धूप पड़ने से वे झुलस जाते हैं"
            ]
        },
        "causes": {
            "en": "Fungal pathogen Septoria lycopersici overwintering on diseased solanaceous crop debris and weeds.",
            "mr": "सेप्टोरिया लायकोपर्सिकी बुरशी, जी पिकांच्या जुन्या अवशेषांमध्ये व तणांवर जिवंत राहते.",
            "hi": "सेप्टोरिया लाइकोपर्सिकी कवक जो पिछली फसल के अवशेषों और खरपतवार पर जीवित रहता है।"
        },
        "environmental_factors": {
            "en": "Warm temperatures (20°C - 25°C), high humidity, frequent rainfall, and extended dew periods.",
            "mr": "२०° ते २५° से. उबदार तापमान, जास्त आर्द्रता, वारंवार होणारा पाऊस आणि सकाळचे दाट दव.",
            "hi": "२०° से २५° सेल्सियस तापमान, अधिक नमी, रुक-रुक कर होने वाली बारिश और अधिक ओस।"
        },
        "spread_mode": {
            "en": "Rain splashes from soil onto lower leaves, splashing irrigation, insects, and agricultural equipment.",
            "mr": "पावसाचे पाण्याचे शिंतोडे जमिनीवरून खालच्या पानांवर उडाल्यामुळे आणि शेती अवजारांद्वारे.",
            "hi": "मिट्टी से बारिश के छींटों का निचली पत्तियों पर पड़ना और कृषि उपकरणों द्वारा।"
        },
        "immediate_actions": {
            "en": [
                "Prune and destroy all spotted lower foliage immediately to break the upward splash-ladder.",
                "Apply plastic mulch or clean straw around base of plants.",
                "Do not work in the tomato field while leaves are damp with dew or rain."
            ],
            "mr": [
                "मातीपासून रोगाचा संसर्ग वर चढू नये म्हणून खालची सर्व ठिपके पडलेली पाने कापून नष्ट करा.",
                "झाडांच्या बुंध्याशी प्लास्टिक किंवा गवताचे आच्छादन (मल्चिंग) करा.",
                "पाने ओली असताना शेतात खुरपणी किंवा काम करू नका."
            ],
            "hi": [
                "रोग को ऊपर बढ़ने से रोकने के लिए निचली सभी धब्बेदार पत्तियों को तुरंत काटकर जलाएं।",
                "पौधों के आधार पर मल्चिंग शीट या सूखी घास बिछाएं।",
                "पत्तियां गीली होने पर खेत में काम न करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Rotate out of solanaceous crops (tomato, potato, eggplant) for at least 3 years.",
                "Stake and trellis tomato plants to elevate canopy 40-50 cm above soil level.",
                "Deep plow field residues immediately after the final harvest."
            ],
            "mr": [
                "टोमॅटो नंतर ३ वर्षे इतर कुळातील पिकांची फेरपालट करा.",
                "झाडांना काठ्या किंवा तारेचा आधार देऊन वर बांधा.",
                "हंगाम संपताच शेताची खोल नांगरणी करून जुने अवशेष जमिनीत गाडून टाका."
            ],
            "hi": [
                "टमाटर के बाद कम से कम ३ साल तक अन्य फसलों का चक्र अपनाएं।",
                "पौधों को डंडों या तारों के सहारे ऊपर बांधें।",
                "फसल समाप्ति के बाद खेत की गहरी जुताई करें।"
            ]
        },
        "expert_threshold": {
            "en": "If defoliation exceeds 15% before fruit maturity, chemical fungicide protection is required to prevent fruit scald.",
            "mr": "फळे पिकण्यापूर्वी १५% पेक्षा जास्त पाने गळू लागल्यास त्वरित बुरशीनाशक फवारणीसाठी तज्ज्ञांचा सल्ला घ्या.",
            "hi": "फल पकने से पहले यदि १५% से अधिक पत्तियां गिरने लगें तो तुरंत कवकनाशी का छिड़काव करें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Broad-spectrum contact and systemic foliar fungicides to halt fungal pycnidial spore release.",
                "mr": "बुरशीचे बीजाणू रोखण्यासाठी स्पर्शजन्य व आंतरप्रवाही बुरशीनाशकांची फवारणी.",
                "hi": "कवक के बीजाणुओं को रोकने के लिए उपयुक्त कवकनाशी का समयबद्ध छिड़काव।"
            },
            "formulations": [
                {"name": "Chlorothalonil 75% WP", "dosage": "2.0 g per Liter water", "phi_days": "5 days"},
                {"name": "Mancozeb 75% WP", "dosage": "2.5 g per Liter water", "phi_days": "7 days"},
                {"name": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC", "dosage": "1.0 ml per Liter water", "phi_days": "7 days"}
            ],
            "application_timing": {
                "en": "Begin spraying at first sign of lower leaf spotting; repeat every 7-10 days in wet seasons.",
                "mr": "खालच्या पानांवर पहिले ठिपके दिसताच फवारणी सुरू करा; पाऊस असल्यास दर ७-१० दिवसांनी पुनरावृत्ती करा.",
                "hi": "निचली पत्तियों पर पहला धब्बा दिखते ही छिड़काव करें; बारिश में ७-१० दिन में दोहराएं।"
            },
            "safety_precautions": {
                "en": "Avoid water contamination; maintain safe buffer from farm ponds and wells.",
                "mr": "औषध विहीर किंवा पाण्याच्या साठ्यात मिसळणार नाही याची काळजी घ्या.",
                "hi": "दवा का पानी कुएं या तालाब में न जाने दें।"
            },
            "irrigation_guidance": {"en": "Drip irrigation only; morning hours.", "mr": "फक्त सकाळी ठिबक सिंचनाने पाणी द्या.", "hi": "केवल सुबह ड्रिप से सिंचाई करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Copper bactericide/fungicide combined with Trichoderma soil inoculation and reflective mulching.",
                "mr": "तांबायुक्त बुरशीनाशक (कॉपर हायड्रॉक्साइड), ट्रायकोडर्मा आणि मल्चिंगचा एकात्मिक वापर.",
                "hi": "कॉपर आधारित जैविक कवकनाशी, ट्राइकोडर्मा और मल्चिंग का समन्वित उपयोग।"
            },
            "bio_agents": [
                {"name": "Copper Hydroxide 53.8% Dry Granules", "dosage": "2.0 g per Liter water"},
                {"name": "Trichoderma harzianum", "dosage": "5 g per Liter water root drench and spray"},
                {"name": "Fermented Garlic-Chili Extract (Botanical)", "dosage": "15 ml per Liter water"}
            ],
            "sanitation": {"en": "Collect all spotted leaves in bags; never allow them to decompose in the field.", "mr": "ठिपके असलेली पाने पिशवीत गोळा करून शेताबाहेर नष्ट करा.", "hi": "धब्बेदार पत्तियों को एकत्र कर खेत से दूर नष्ट करें।"},
            "soil_health": {"en": "Apply vermicompost mixed with bio-fertilizers to strengthen root defense.", "mr": "गांडूळ खतामध्ये जैविक खते मिसळून झाडांना द्या.", "hi": "वर्मीकंपोस्ट में जैव उर्वरक मिलाकर पौधों को दें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹550 - ₹850 / acre", "organic": "₹250 - ₹450 / acre"},
            "speed": {"chemical": "Fast protection (24 - 48 hours)", "organic": "Gradual preventive (3 - 5 days)"},
            "phi": {"chemical": "5 - 7 Days", "organic": "1 Day"},
            "eco_impact": {"chemical": "Moderate (Follow standard safety)", "organic": "Safe and eco-friendly"}
        }
    },

    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "scientific_pathogen": "Tetranychus urticae (Two-Spotted Spider Mite - Arachnid Pest)",
        "plant_name": {"en": "Tomato", "mr": "टोमॅटो", "hi": "टमाटर"},
        "disease_name": {
            "en": "Two-Spotted Spider Mite Infestation",
            "mr": "लाल कोळी कीड (दोन ठिपक्यांचा कोळी)",
            "hi": "लाल मकड़ी कीट (दो धब्बों वाली मकड़ी)"
        },
        "is_healthy": False,
        "symptoms": {
            "en": [
                "Fine yellow or white stippling (tiny speckled dots) on the upper surface of leaves",
                "Silken webbings spun across leaf undersides, flower clusters, and growing shoot tips",
                "Leaves turn bronze or reddish-brown, dry up, take on a parchment texture, and drop"
            ],
            "mr": [
                "पानांच्या वरच्या भागावर बारीक पिवळसर किंवा पांढरे ठिपके (बारीक छिद्रे) दिसतात",
                "पानांच्या मागच्या बाजूला, फुलांवर आणि शेंड्यावर नाजूक कोळ्याचे जाळे दिसते",
                "पाने तांबूस किंवा तपकिरी पडून वाळतात आणि जळून गेल्यासारखी गळतात"
            ],
            "hi": [
                "पत्तियों की ऊपरी सतह पर हल्के पीले या सफेद बारीक बिंदु (धब्बे) दिखाई देते हैं",
                "पत्तियों के नीचे, फूलों और नई कोपलों पर महीन रेशमी जाला बना होता है",
                "पत्तियां तांबई या भूरी होकर सूख जाती हैं और समय से पहले गिरती हैं"
            ]
        },
        "causes": {
            "en": "Phytophagous mite Tetranychus urticae piercing plant cells with mouth stylets and sucking out chlorophyll contents.",
            "mr": "टेट्रानिकस अर्टिका नावाचा सूक्ष्म लाल कोळी, जो पानांमधील हरितद्रव्य आणि रस शोषून घेतो.",
            "hi": "टेट्रानिकस अर्टिका नामक सूक्ष्म मकड़ी कीट जो पत्तियों की कोशिकाओं से रस और हरित लवक चूसता है।"
        },
        "environmental_factors": {
            "en": "Hot, dry, and dusty weather (temperatures >30°C and relative humidity <50%).",
            "mr": "अतिउष्ण, कोरडे आणि धुळीचे हवामान (३०° से. पेक्षा जास्त तापमान आणि ५०% पेक्षा कमी आर्द्रता).",
            "hi": "अत्यधिक गर्म, सूखा और धूल भरा मौसम (३०° सेल्सियस से अधिक तापमान और कम नमी)।"
        },
        "spread_mode": {
            "en": "Mites produce silken threads and are carried long distances by wind gusts (ballooning) and by farm tools.",
            "mr": "कोळी जाळ्याच्या साहाय्याने वाऱ्याच्या झोतासोबत लांबवर उडून जातात आणि अवजारांद्वारे पसरतात.",
            "hi": "मकड़ियां जाले बनाकर हवा के झोंकों के साथ उड़कर एक खेत से दूसरे खेत में फैलती हैं।"
        },
        "immediate_actions": {
            "en": [
                "Hose down dusty perimeter farm roads to eliminate dust which protects spider mites from predators.",
                "Apply high-pressure overhead water spray in early morning to physically dislodge mites and destroy webs.",
                "Remove and bag heavily webbed plant branches immediately."
            ],
            "mr": [
                "शेताच्या रस्त्यांवर पाणी मारून धूळ शांत करा; धुळीमुळे कोळी किडीचे नैसर्गिक शत्रू नष्ट होतात.",
                "सकाळी पाण्याच्या जोरदार फवाऱ्याने पानांमागील जाळी आणि कोळी धुवून काढा.",
                "जास्त जाळे लागलेल्या फांद्या कापून पिशवीत भरून शेताबाहेर नष्ट करा."
            ],
            "hi": [
                "खेत की मेड़ों पर पानी छिड़क कर धूल शांत करें; धूल में मकड़ी तेजी से पनपती है।",
                "सुबह के समय तेज पानी की धार से पत्तियों के निचले हिस्से को धोकर जाले नष्ट करें।",
                "अत्यधिक जाले वाली शाखाओं को काटकर नष्ट करें।"
            ]
        },
        "preventive_measures": {
            "en": [
                "Conserve natural predatory mites (e.g., Phytoseiulus persimilis and Neoseiulus californicus).",
                "Avoid unnecessary broad-spectrum pyrethroid insecticide sprays which destroy beneficial predatory insects.",
                "Keep soil well-watered to prevent drought stress in crops."
            ],
            "mr": [
                "मित्रकिडींचे (शिकारी कोळी, लेडीबर्ड बीटल) संरक्षण करा.",
                "अनावश्यक रासायनिक कीटकनाशकांची फवारणी टाळा, कारण त्यामुळे मित्रकिडे मरतात.",
                "झाडांना पाण्याचा ताण पडू देऊ नका; जमिनीत ओलावा टिकवून ठेवा."
            ],
            "hi": [
                "मित्र कीटों (शिकारी मकड़ी, लेडीबर्ड बीटल) का संरक्षण करें।",
                "अनावश्यक कीटनाशकों का अंधाधुंध प्रयोग न करें जिससे मित्र कीट नष्ट न हों।",
                "फसल को पानी की कमी न होने दें।"
            ]
        },
        "expert_threshold": {
            "en": "If more than 5 mites per leaf are detected or webs begin draping over growing shoot tips, chemical acaricide is needed.",
            "mr": "एका पानावर ५ पेक्षा जास्त कोळी आढळल्यास किंवा शेंड्यावर जाळे दिसू लागल्यास त्वरित औषध फवारणी करा.",
            "hi": "प्रति पत्ती ५ से अधिक मकड़ियां दिखने या कोपलों पर जाला बनने पर तुरंत विशेषज्ञ की सलाह लें।"
        },
        "chemical_plan": {
            "approach": {
                "en": "Application of true acaricides/miticides specifically targeting spider mite nerve transmission or lipid biosynthesis.",
                "mr": "फक्त कोळी किडीवर प्रभावी ठरणाऱ्या विशिष्ट आंतरप्रवाही कोळीनाशकांची (Acaricides) फवारणी.",
                "hi": "विशेष मकड़ीनाशक (एकैरीसाइड) का उपयोग जो मकड़ी के तंत्रिका तंत्र और अंडों को नष्ट करे।"
            },
            "formulations": [
                {"name": "Abamectin 1.9% EC", "dosage": "0.5 ml per Liter water", "phi_days": "3 days"},
                {"name": "Spiromesifen 22.9% SC", "dosage": "1.0 ml per Liter water", "phi_days": "5 days"},
                {"name": "Fenpyroximate 5% EC", "dosage": "1.0 to 1.5 ml per Liter water", "phi_days": "7 days"}
            ],
            "application_timing": {
                "en": "Spray late afternoon, using high pressure to thoroughly penetrate underleaf webbing.",
                "mr": "संध्याकाळी उच्च दाबाच्या पंपाने पानाच्या खालच्या भागावर औषध पोहचेल अशी फवारणी करा.",
                "hi": "शाम को तेज दबाव वाले पंप से पत्तियों के निचले हिस्से तक दवा पहुंचाते हुए छिड़काव करें।"
            },
            "safety_precautions": {
                "en": "Rotate miticide classes strictly to prevent rapid acaricide resistance (mites develop resistance in 2-4 generations).",
                "mr": "कोळीनाशके बदलून वापरा, कारण कोळी किडीमध्ये औषधाविरुद्ध प्रतिकारशक्ती खूप लवकर तयार होते.",
                "hi": "दवाएं बदल-बदल कर प्रयोग करें ताकि कीटों में प्रतिरोधक क्षमता न बने।"
            },
            "irrigation_guidance": {"en": "Increase irrigation frequency to elevate crop microclimate humidity.", "mr": "शेतात आर्द्रता टिकवण्यासाठी पाणी नियमित द्या.", "hi": "खेत में नमी बनाए रखने के लिए समय पर सिंचाई करें।"}
        },
        "organic_plan": {
            "approach": {
                "en": "Suffocating horticultural mineral oils, sulfur dusting, and bio-miticide formulations.",
                "mr": "सल्फर (गंधक), कडुनिंब तेल आणि विरघळणाऱ्या खनिज तेलाची फवारणी करून कोळी किडीचा नायनाट.",
                "hi": "सल्फर (गंधक), नीम का तेल और घुलनशील वनस्पति तेल के छिड़काव द्वारा दम घोंटकर रोकथाम।"
            },
            "bio_agents": [
                {"name": "Wettable Sulfur 80% WDG", "dosage": "2.5 to 3.0 g per Liter water (do NOT apply if temp >35°C)"},
                {"name": "Cold-Pressed Neem Oil (10000 ppm)", "dosage": "4 to 5 ml per Liter water with soap emulsifier"},
                {"name": "Beauveria bassiana (Entomopathogenic fungus)", "dosage": "5 g per Liter water"}
            ],
            "sanitation": {"en": "Prune and burn webbed branch ends immediately.", "mr": "जाळे असलेल्या फांद्या कापून नष्ट करा.", "hi": "जाले वाली शाखाओं को काटकर तुरंत जलाएं।"},
            "soil_health": {"en": "Apply silica amendments to strengthen leaf epidermal cell walls against stylet piercing.", "mr": "सिलिकॉनयुक्त खतांचा वापर करा.", "hi": "सिलिकॉन युक्त जैविक खादों का प्रयोग करें।"}
        },
        "comparison": {
            "cost": {"chemical": "₹700 - ₹1100 / acre", "organic": "₹350 - ₹550 / acre"},
            "speed": {"chemical": "Fast mortality (within 24 hours)", "organic": "Moderate suffocation/suppression (2 - 4 days)"},
            "phi": {"chemical": "3 - 7 Days", "organic": "0 - 1 Days"},
            "eco_impact": {"chemical": "Toxicity to beneficial mites and aquatic organisms", "organic": "Safe for pollinators and preserves beneficial insect fauna"}
        }
    }
}

CLASS_NAME_LIST = [
    "Tomato_Target_Spot",
    "Tomato_Tomato_mosaic_virus",
    "Tomato_Tomato_YellowLeaf_Curl_Virus",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_healthy",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite"
]

def get_disease_info(class_name, lang="mr"):
    """Retrieve structured disease info for a given predicted class and language."""
    data = DISEASE_KNOWLEDGE_BASE.get(class_name)
    if not data:
        # Graceful fallback if unknown class
        return {
            "class_name": class_name,
            "scientific_pathogen": "Unknown Pathogen",
            "plant_name": "Tomato",
            "disease_name": class_name.replace("_", " "),
            "is_healthy": False,
            "symptoms": ["Unrecognized symptom profile. Please consult local agronomist."],
            "causes": "Condition not cataloged.",
            "environmental_factors": "General agricultural conditions.",
            "spread_mode": "Standard biological vector.",
            "immediate_actions": ["Isolate plant", "Consult local extension worker"],
            "preventive_measures": ["Use certified seed", "Practice crop rotation"],
            "expert_threshold": "Consult an agricultural officer.",
            "chemical_plan": {
                "approach": "Seek certified recommendation.",
                "formulations": [{"name": "Broad spectrum copper protectant", "dosage": "2g/L", "phi_days": "7 days"}],
                "application_timing": "Morning",
                "safety_precautions": "Wear PPE",
                "irrigation_guidance": "Drip"
            },
            "organic_plan": {
                "approach": "Organic bio-fungicide",
                "bio_agents": [{"name": "Trichoderma harzianum", "dosage": "5g/L"}],
                "sanitation": "Remove infected leaves",
                "soil_health": "Apply FYM"
            },
            "comparison": {
                "cost": {"chemical": "Moderate", "organic": "Low"},
                "speed": {"chemical": "Fast", "organic": "Gradual"},
                "phi": {"chemical": "7 Days", "organic": "0 Days"},
                "eco_impact": {"chemical": "Follow precautions", "organic": "Eco-friendly"}
            }
        }
    
    # Extract translated text
    return {
        "class_name": class_name,
        "scientific_pathogen": data["scientific_pathogen"],
        "plant_name": data["plant_name"].get(lang, data["plant_name"]["en"]),
        "disease_name": data["disease_name"].get(lang, data["disease_name"]["en"]),
        "is_healthy": data["is_healthy"],
        "symptoms": data["symptoms"].get(lang, data["symptoms"]["en"]),
        "causes": data["causes"].get(lang, data["causes"]["en"]),
        "environmental_factors": data["environmental_factors"].get(lang, data["environmental_factors"]["en"]),
        "spread_mode": data["spread_mode"].get(lang, data["spread_mode"]["en"]),
        "immediate_actions": data["immediate_actions"].get(lang, data["immediate_actions"]["en"]),
        "preventive_measures": data["preventive_measures"].get(lang, data["preventive_measures"]["en"]),
        "expert_threshold": data["expert_threshold"].get(lang, data["expert_threshold"]["en"]),
        "chemical_plan": {
            "approach": data["chemical_plan"]["approach"].get(lang, data["chemical_plan"]["approach"]["en"]),
            "formulations": data["chemical_plan"]["formulations"],
            "application_timing": data["chemical_plan"]["application_timing"].get(lang, data["chemical_plan"]["application_timing"]["en"]),
            "safety_precautions": data["chemical_plan"]["safety_precautions"].get(lang, data["chemical_plan"]["safety_precautions"]["en"]),
            "irrigation_guidance": data["chemical_plan"]["irrigation_guidance"].get(lang, data["chemical_plan"]["irrigation_guidance"]["en"]),
        },
        "organic_plan": {
            "approach": data["organic_plan"]["approach"].get(lang, data["organic_plan"]["approach"]["en"]),
            "bio_agents": data["organic_plan"]["bio_agents"],
            "sanitation": data["organic_plan"]["sanitation"].get(lang, data["organic_plan"]["sanitation"]["en"]),
            "soil_health": data["organic_plan"]["soil_health"].get(lang, data["organic_plan"]["soil_health"]["en"]),
        },
        "comparison": data["comparison"]
    }
