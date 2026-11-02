"""Learning content for NammaKannada.
Each item: kn (Kannada script), tr (transliteration), en (English), hi (Hindi)."""


def w(kn, tr, en, hi):
    return {"kn": kn, "tr": tr, "en": en, "hi": hi}


LESSONS = [
    {
        "id": 1, "icon": "👋", "title": "Kannada Greetings",
        "tip": "Namaskara works at any time of day and with anyone. Add 'ಅವರೇ' (avare) after a name to show respect.",
        "words": [
            w("ನಮಸ್ಕಾರ", "Namaskara", "Hello", "नमस्कार"),
            w("ಶುಭೋದಯ", "Shubhodaya", "Good morning", "सुप्रभात"),
            w("ಶುಭ ಸಂಜೆ", "Shubha sanje", "Good evening", "शुभ संध्या"),
            w("ಶುಭ ರಾತ್ರಿ", "Shubha ratri", "Good night", "शुभ रात्रि"),
            w("ಧನ್ಯವಾದಗಳು", "Dhanyavadagalu", "Thank you", "धन्यवाद"),
            w("ದಯವಿಟ್ಟು", "Dayavittu", "Please", "कृपया"),
            w("ಕ್ಷಮಿಸಿ", "Kshamisi", "Sorry / Excuse me", "माफ़ कीजिए"),
            w("ಸ್ವಾಗತ", "Swagata", "Welcome", "स्वागत"),
            w("ಹೇಗಿದ್ದೀರಿ?", "Hegiddira?", "How are you?", "आप कैसे हैं?"),
            w("ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ", "Naanu chennagiddene", "I am fine", "मैं ठीक हूँ"),
            w("ಮತ್ತೆ ಸಿಗೋಣ", "Matte sigona", "See you again", "फिर मिलेंगे"),
        ],
    },
    {
        "id": 2, "icon": "📚", "title": "Basic Vocabulary",
        "tip": "Many Kannada nouns end with the vowel sound 'u' (neeru, haalu, hoovu). Listen for it!",
        "words": [
            w("ನೀರು", "Neeru", "Water", "पानी"),
            w("ಊಟ", "Oota", "Meal / Food", "खाना"),
            w("ಮನೆ", "Mane", "House", "घर"),
            w("ಪುಸ್ತಕ", "Pustaka", "Book", "किताब"),
            w("ಅಮ್ಮ", "Amma", "Mother", "माँ"),
            w("ಅಪ್ಪ", "Appa", "Father", "पिता"),
            w("ಸ್ನೇಹಿತ", "Snehita", "Friend", "दोस्त"),
            w("ಶಾಲೆ", "Shaale", "School", "स्कूल"),
            w("ಹಾಲು", "Haalu", "Milk", "दूध"),
            w("ಹೂವು", "Hoovu", "Flower", "फूल"),
            w("ರಸ್ತೆ", "Raste", "Road", "सड़क"),
            w("ಹಣ", "Hana", "Money", "पैसा"),
            w("ಸಮಯ", "Samaya", "Time", "समय"),
            w("ದೊಡ್ಡ", "Dodda", "Big", "बड़ा"),
            w("ಚಿಕ್ಕ", "Chikka", "Small", "छोटा"),
            w("ಒಳ್ಳೆಯ", "Olleya", "Good", "अच्छा"),
        ],
    },
    {
        "id": 3, "icon": "🔢", "title": "Numbers and Counting",
        "tip": "Kannada numerals look different (೧ ೨ ೩) but everyday life mostly uses 1 2 3. Learn the spoken words first.",
        "words": [
            w("ಒಂದು", "Ondu", "One (1)", "एक"),
            w("ಎರಡು", "Eradu", "Two (2)", "दो"),
            w("ಮೂರು", "Mooru", "Three (3)", "तीन"),
            w("ನಾಲ್ಕು", "Naalku", "Four (4)", "चार"),
            w("ಐದು", "Aidu", "Five (5)", "पाँच"),
            w("ಆರು", "Aaru", "Six (6)", "छह"),
            w("ಏಳು", "Eelu", "Seven (7)", "सात"),
            w("ಎಂಟು", "Entu", "Eight (8)", "आठ"),
            w("ಒಂಬತ್ತು", "Ombattu", "Nine (9)", "नौ"),
            w("ಹತ್ತು", "Hattu", "Ten (10)", "दस"),
        ],
    },
    {
        "id": 4, "icon": "🙋", "title": "Introducing Yourself",
        "tip": "To say 'My name is Asha' say: ನನ್ನ ಹೆಸರು ಆಶಾ (Nanna hesaru Asha). Just swap the name.",
        "words": [
            w("ನಿಮ್ಮ ಹೆಸರೇನು?", "Nimma hesarenu?", "What is your name?", "आपका नाम क्या है?"),
            w("ನನ್ನ ಹೆಸರು ...", "Nanna hesaru ...", "My name is ...", "मेरा नाम ... है"),
            w("ನಿಮ್ಮ ಊರು ಯಾವುದು?", "Nimma ooru yaavudu?", "Where are you from?", "आप कहाँ से हैं?"),
            w("ನಾನು ಕನ್ನಡ ಕಲಿಯುತ್ತಿದ್ದೇನೆ", "Naanu Kannada kaliyuttiddene", "I am learning Kannada", "मैं कन्नड़ सीख रहा/रही हूँ"),
            w("ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗಿ ಸಂತೋಷ", "Nimmannu bheti aagi santosha", "Nice to meet you", "आपसे मिलकर खुशी हुई"),
            w("ಹೌದು", "Houdu", "Yes", "हाँ"),
            w("ಇಲ್ಲ", "Illa", "No", "नहीं"),
        ],
    },
]

PHRASES = [
    {"cat": "🛍️ Shopping", **w("ಇದು ಎಷ್ಟು?", "Idu eshtu?", "How much is this?", "यह कितने का है?")},
    {"cat": "🛍️ Shopping", **w("ಸ್ವಲ್ಪ ಕಡಿಮೆ ಮಾಡಿ", "Swalpa kadime maadi", "Please reduce the price a little", "थोड़ा कम कीजिए")},
    {"cat": "🍽️ Food", **w("ನನಗೆ ನೀರು ಬೇಕು", "Nanage neeru beku", "I need water", "मुझे पानी चाहिए")},
    {"cat": "🍽️ Food", **w("ತುಂಬಾ ರುಚಿಯಾಗಿದೆ", "Tumba ruchiyaagide", "It is very tasty", "बहुत स्वादिष्ट है")},
    {"cat": "🍽️ Food", **w("ಬಿಲ್ ಕೊಡಿ", "Bill kodi", "Please give the bill", "बिल दीजिए")},
    {"cat": "🚌 Travel", **w("ಬಸ್ ನಿಲ್ದಾಣ ಎಲ್ಲಿದೆ?", "Bus nildaana ellide?", "Where is the bus stand?", "बस स्टैंड कहाँ है?")},
    {"cat": "🚌 Travel", **w("ಇಲ್ಲಿ ನಿಲ್ಲಿಸಿ", "Illi nillisi", "Stop here", "यहाँ रोकिए")},
    {"cat": "🚌 Travel", **w("ಬಲಕ್ಕೆ ತಿರುಗಿ", "Balakke thirugi", "Turn right", "दाएँ मुड़िए")},
    {"cat": "🚌 Travel", **w("ಎಡಕ್ಕೆ ತಿರುಗಿ", "Edakke thirugi", "Turn left", "बाएँ मुड़िए")},
    {"cat": "💬 Conversation", **w("ನನಗೆ ಅರ್ಥವಾಗಲಿಲ್ಲ", "Nanage arthavaagalilla", "I did not understand", "मुझे समझ नहीं आया")},
    {"cat": "💬 Conversation", **w("ನಿಧಾನವಾಗಿ ಮಾತನಾಡಿ", "Nidhaanavaagi maatanaadi", "Please speak slowly", "धीरे बोलिए")},
    {"cat": "🚨 Emergency", **w("ಸಹಾಯ ಮಾಡಿ", "Sahaaya maadi", "Please help me", "मदद कीजिए")},
    {"cat": "🚨 Emergency", **w("ವೈದ್ಯರನ್ನು ಕರೆಯಿರಿ", "Vaidyarannu kareyiri", "Call a doctor", "डॉक्टर को बुलाइए")},
]

for _l in LESSONS:
    for _w in _l["words"]:
        _w["lesson"] = _l["id"]
for _p in PHRASES:
    _p["lesson"] = 0

ALL_ITEMS = [x for l in LESSONS for x in l["words"]] + PHRASES
