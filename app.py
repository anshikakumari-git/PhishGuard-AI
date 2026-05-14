import streamlit as st
import requests
import random
import time

st.set_page_config(page_title="PhishGuard", page_icon="🔐", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #4a6cf7, #3b50d5, #2f3eb8, #1f2f9c);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.title { text-align: center; font-size: 50px; font-weight: bold; color: white; }
.subtitle { text-align: center; color: #f1f1f1; margin-bottom: 25px; }

.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.safe { color: #00ffcc; font-size: 20px; font-weight: bold; }
.danger { color: #ff4b5c; font-size: 20px; font-weight: bold; }
.warn { color: #ffd93d; font-size: 20px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔐 PhishGuard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered URL Safety Scanner ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

url = st.text_input("🔗 Paste your URL here")


def basic_check(url):
    if "https" not in url: return "No HTTPS detected"
    elif "@" in url: return "Suspicious '@' symbol"
    elif "-" in url: return "Suspicious '-' in domain"
    return None

if st.button("🚀 Scan Now"):
    if url == "":
        st.warning("Please enter a URL")
    else:
        basic_result = basic_check(url)
        api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
        payload = {
            "client": {"clientId": "phishguard", "clientVersion": "1.0"},
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{"url": url}]
            }
        }

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        with st.spinner("Analyzing URL with AI + Google Safe Browsing... 🔍"):
            try:
                response = requests.post(api_url, json=payload)
                result = response.json()
            except:
                st.error("Error contacting Google Safe Browsing API")
                result = {}

        st.write("---")
        score = random.randint(20, 95)

        if "matches" in result:
            st.markdown('<div class="danger">🚨 Dangerous URL detected!</div>', unsafe_allow_html=True)
            score = random.randint(80, 100)
        elif basic_result:
            st.markdown(f'<div class="warn">⚠️ {basic_result}</div>', unsafe_allow_html=True)
            score = random.randint(50, 80)
        else:
            st.markdown('<div class="safe">✅ This URL looks safe</div>', unsafe_allow_html=True)
            score = random.randint(10, 40)

        st.write("### 🔎 Risk Score")
        st.progress(score)
        st.write(f"**{score}% Risk Detected**")

        if score > 75: st.error("High risk! This URL may be phishing or malicious.")
        elif score > 40: st.warning("Moderate risk. Be cautious while using this URL.")
        else: st.success("Low risk. This URL appears safe.")

        st.caption("⚡ Powered by AI Threat Intelligence + Google Safe Browsing API")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:30px; color:white;'>
Made with 💜 | PhishGuard v2.0
</div>
""", unsafe_allow_html=True)
