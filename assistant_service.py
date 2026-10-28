# -*- coding: utf-8 -*-
"""
KrishiMitra AI - Personalized Agricultural Assistant
Multilingual support in Marathi, Hindi, and English.
Integrates with Google Gemini API when GEMINI_API_KEY is configured in .env.
Automatically falls back to verified agronomic rule-based knowledge engine when unconfigured.
"""

import os
import requests
from disease_knowledge_base import DISEASE_KNOWLEDGE_BASE
from schemes_data import GOVERNMENT_SCHEMES

class FarmingAssistant:
    @staticmethod
    def get_answer(query_text, lang="mr", user_profile=None):
        """
        Processes a farmer's query and returns a grounded answer.
        """
        api_key = os.getenv("GEMINI_API_KEY", "")

        # 1. If Gemini API Key is configured, attempt LLM call with strict agronomic grounding
        if api_key and api_key != "your_gemini_api_key_here":
            try:
                system_instruction = (
                    "You are KrishiMitra AI, an expert agricultural assistant for Indian and Maharashtra farmers. "
                    f"Respond in the requested language: '{lang}' (mr=Marathi, hi=Hindi, en=English). "
                    "Provide practical, scientific, safe farming advice. "
                    "Always mention that chemical pesticides require reading the package label and wearing safety gear. "
                    "Include organic alternatives like Jeevamrut, Trichoderma, and Neem oil where applicable. "
                    "Keep answers concise, respectful, and farmer-friendly."
                )
                
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                payload = {
                    "contents": [{
                        "parts": [
                            {"text": f"{system_instruction}\n\nFarmer's Question: {query_text}"}
                        ]
                    }],
                    "generationConfig": {
                        "temperature": 0.3,
                        "maxOutputTokens": 600
                    }
                }
                
                resp = requests.post(url, json=payload, timeout=8)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        content = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                        if content:
                            return {
                                "answer": content,
                                "source": "Gemini AI (Agricultural Knowledge Grounded)"
                            }
            except Exception:
                # Fall back to rule-based engine on any network or API issue
                pass

        # 2. Rule-Based Grounded Agricultural Knowledge Engine
        return {
            "answer": FarmingAssistant._rule_based_response(query_text, lang, user_profile),
            "source": "KrishiMitra Verified Knowledge Base (Rule-Based Engine)"
        }

    @staticmethod
    def _rule_based_response(q, lang, user_profile):
        q_lower = q.lower()

        # Scheme queries
        if any(w in q_lower for w in ["scheme", "yojana", "योजना", "अनुदान", "सब्सिडी", "pm kisan", "pmkisan", "विमा", "bima", "kusum", "solar"]):
            if "pm kisan" in q_lower or "किसान सम्मान" in q_lower or "सन्मान निधी" in q_lower:
                if lang == "mr":
                    return "पीएम-किसान योजनेअंतर्गत पात्र शेतकऱ्यांना दरवर्षी ₹६,००० तीन हप्त्यांत मिळतात. याव्यतिरिक्त महाराष्ट्र शासन 'नमो शेतकरी महासन्मान निधी' अंतर्गत आणखी ₹६,००० देते (एकूण ₹१२,०००). यासाठी ७/१२, आधार संलग्न बँक खाते आणि e-KYC आवश्यक आहे. अधिक माहिती 'सरकारी योजना' विभागात पहा."
                elif lang == "hi":
                    return "पीएम-किसान योजना के तहत पात्र किसानों को प्रति वर्ष ₹६,००० तीन किश्तों में सीधे बैंक खाते में मिलते हैं। महाराष्ट्र में 'नमो शेतकरी योजना' से अतिरिक्त ₹६,००० मिलते हैं (कुल ₹१२,०००)। आधार ई-केवाईसी अनिवार्य है।"
                else:
                    return "Under PM-KISAN, eligible landholding farmers receive ₹6,000 annually in three installments of ₹2,000. In Maharashtra, the Namo Shetkari scheme adds ₹6,000 more (total ₹12,000/yr). Land records and active e-KYC are mandatory."

            if "solar" in q_lower or "kusum" in q_lower or "पंप" in q_lower or "सौर":
                if lang == "mr":
                    return "पीएम-कुसुम आणि महावितरण महाकृषी ऊर्जा अभियानांतर्गत सौर कृषी पंपांवर ९०% पर्यंत अनुदान मिळते. ३, ५ आणि ७.५ एचपी सौर पंपांसाठी शेतकरी हिस्सा फक्त १०% (SC/ST साठी ५%) आहे. अधिक माहितीसाठी 'सरकारी योजना' विभागात कुसुम योजनेची अधिकृत लिंक तपासा."
                elif lang == "hi":
                    return "पीएम-कुसुम योजना के तहत ३, ५ व ७.५ एचपी सौर कृषि पंपों पर ९०% तक सब्सिडी उपलब्ध है। किसान का अंश केवल १०% (एससी/एसटी के लिए ५%) है।"
                else:
                    return "Under PM-KUSUM Component-B, solar water pumps (3, 5, 7.5 HP) receive up to 90% capital subsidy in Maharashtra. The farmer share is only 10% (5% for SC/ST). Check our Government Schemes tab for verified application links."

            if "bima" in q_lower or "insurance" in q_lower or "विमा" in q_lower:
                if lang == "mr":
                    return "महाराष्ट्रात सर्वदूर पीक विमा योजनेअंतर्गत शेतकऱ्यांना फक्त ₹१ भरून पीक विमा उतरवता येतो. नैसर्गिक आपत्तीमुळे नुकसान झाल्यास ७२ तासांच्या आत 'Crop Insurance App' वरून फोटोसह तक्रार नोंदवणे बंधनकारक आहे."
                elif lang == "hi":
                    return "महाराष्ट्र में किसान मात्र ₹१ टोकन राशि में फसल बीमा करा सकते हैं। स्थानीय आपदा होने पर ७२ घंटे के भीतर 'क्रॉप इंश्योरेंस ऐप' से फोटो अपलोड करके क्लेम दर्ज करना आवश्यक है।"
                else:
                    return "In Maharashtra, farmers can enroll in PMFBY crop insurance at a nominal ₹1 premium. In case of localized flood or storm damage, file a claim within 72 hours via the official Crop Insurance Mobile App."

        # Blight / Disease queries
        if any(w in q_lower for w in ["blight", "करपा", "झुलसा", "बुरशी", "ठिपके", "spots", "fungus", "disease"]):
            if "late" in q_lower or "उशीरा" in q_lower or "पछेती" in q_lower:
                if lang == "mr":
                    return "लेट ब्लाइट (उशीरा येणारा करपा) हा थंड व दमट हवामानात वेगाने पसरतो. पानांच्या मागच्या बाजूला पांढरी बुरशी दिसते. उपचारासाठी: सायमोक्सॅनिल + मँकोझेब (२ ग्रॅम/लिटर) किंवा फेनॅमिडोन + मँकोझेब (२.५ ग्रॅम/लिटर) फवारा. सेंद्रिय उपायासाठी १% बोर्डो मिश्रण किंवा ट्रायकोडर्मा वापरा. पाने ओली असताना शेतात काम करू नका."
                elif lang == "hi":
                    return "पछेती झुलसा (लेट ब्लाइट) अधिक नमी और ठंड में तेजी से फैलता है। उपचार हेतु: साइमोक्सानिल + मैनकोजेब (२ ग्राम/लीटर) अथवा डाइमेथोमॉर्फ का छिड़काव करें। जैविक रूप से १% बोर्डो मिश्रण का छिड़काव करें।"
                else:
                    return "Late Blight spreads rapidly during cool, foggy, or rainy conditions. Chemical control: Spray Cymoxanil 8% + Mancozeb 64% WP (2 g/L) or Dimethomorph 50% WP (1 g/L). Organic option: 1% Bordeaux mixture or Trichoderma harzianum. Avoid overhead watering."

            if "early" in q_lower or "लवकर" in q_lower or "अगेती" in q_lower:
                if lang == "mr":
                    return "अल्टरनेरिया करपा (अर्ली ब्लाइट) मध्ये पानांवर चकतीसारखी वर्तुळे (बुलसाई) दिसतात. उपचारासाठी मँकोझेब ७५% WP (२.५ ग्रॅम/लिटर) किंवा डायफेनोकोनॅझोल २५% EC (०.५ ते १ मिली/लिटर) फवारा. झाडांची खालची जमिनीला टेकलेली पाने छाटा आणि प्लास्टिक मल्चिंग करा."
                elif lang == "hi":
                    return "अगेती झुलसा (अर्ली ब्लाइट) में पत्तियों पर गोल छल्लेदार धब्बे बनते हैं। उपचार: मैनकोजेब (२.५ ग्राम/लीटर) या टेबुकोनाजोल का छिड़काव करें। निचली पत्तियों को काट दें और मल्चिंग का प्रयोग करें।"
                else:
                    return "Early Blight exhibits target-like concentric rings on lower leaves. Chemical treatment: Spray Mancozeb 75% WP @ 2.5 g/L or Difenoconazole 25% EC @ 0.75 ml/L. Prune the lowest 30 cm of foliage to break soil spore splashing."

        # Organic inputs queries
        if any(w in q_lower for w in ["jeevamrut", "जिवामृत", "जीवामृत", "सेंद्रिय", "organic", "neem", "कडुनिंब"]):
            if lang == "mr":
                return "जिवामृत तयार करण्याची कृती: २०० लिटर पाण्यासाठी १० किलो ताजे शेण, १० लिटर गोमूत्र, २ किलो गूळ, २ किलो बेसन आणि मूठभर शेतातील सजीव माती एकत्र करून सावलीत पिंपात ठेवा. दिवसातून २ वेळा काठीने घड्याळाच्या दिशेने ढवळा. ४८ तासांनंतर जिवामृत तयार होते; हे एकरी २०० लिटर ठिबकमधून द्या किंवा १०% प्रमाणात फवारा."
            elif lang == "hi":
                return "जीवामृत बनाने की विधि: २०० लीटर पानी में १० किलो ताजा गोबर, १० लीटर गोमूत्र, २ किलो गुड़, २ किलो बेसन और मुट्ठी भर खेत की मिट्टी मिलाकर छांव में रखें। दिन में दो बार लकड़ी से चलाएं। ४८ घंटे बाद २०० लीटर प्रति एकड़ की दर से ड्रिप में चलाएं।"
            else:
                return "Jeevamrut preparation: In a 200 L drum, mix 10 kg fresh cow dung, 10 L cow urine, 2 kg jaggery, 2 kg chickpea flour (besan), and a handful of fertile farm soil. Stir clockwise twice daily in the shade. Ready in 48-72 hours. Apply 200 L/acre through drip or 10% foliar spray."

        # Weather / Spraying queries
        if any(w in q_lower for w in ["spray", "weather", "हवामान", "मौसम", "फवारणी", "छिड़काव"]):
            if lang == "mr":
                return "फवारणीचा नियम: वाऱ्याचा वेग ताशी १२ किमी पेक्षा कमी असावा आणि पुढील ६-८ तासांत पावसाची शक्यता नसावी. सकाळी ७:०० ते १०:०० किंवा संध्याकाळी ४:३० नंतर फवारणी करणे सर्वात उत्तम. कडक उन्हात फवारल्यास औषध बाष्पीभवन होते व पानांना स्कॉर्चिंग होते."
            elif lang == "hi":
                return "छिड़काव नियम: हवा की गति १२ किमी/घंटे से कम हो और बारिश की संभावना न हो। सुबह ७ से १० अथवा शाम ४:३० के बाद का समय सबसे उपयुक्त है। तेज धूप में छिड़काव से बचें।"
            else:
                return "Spraying Guidelines: Ensure wind speed is below 12 km/h and no rainfall is forecasted within the next 6 hours. Optimal application hours are 7:00-10:00 AM or 4:30-6:30 PM. Never spray during peak mid-day heat."

        # General helpful fallback
        if lang == "mr":
            return (
                "मी कृषिमित्र AI आहे. आपण मला पीक रोग निदान, सेंद्रिय खते (जिवामृत, दशपर्णी अर्क), "
                "हवामान सल्ला, शासकीय योजना (पीएम-किसान, पीक विमा, सौर पंप) किंवा बाजार भावांविषयी विचारू शकता. "
                "कृपया आपला प्रश्न स्पष्टपणे नमूद करा."
            )
        elif lang == "hi":
            return (
                "मैं कृषिमित्र AI हूँ। आप मुझसे फसल रोगों के उपचार, जैविक कीटनाशक (जीवामृत), मौसम परामर्श, "
                "सरकारी योजनाओं (पीएम-किसान, फसल बीमा, सोलर पंप) अथवा मंडी भावों के विषय में पूछ सकते हैं।"
            )
        else:
            return (
                "I am KrishiMitra AI. You can ask me about plant disease diagnosis and treatments (chemical and organic), "
                "weather advisories, government schemes (PM-Kisan, PMFBY, Kusum solar pumps), and APMC mandi price trends."
            )
