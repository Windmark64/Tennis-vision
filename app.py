import streamlit as st
import os
import time
from google import genai

def load_api_key() -> str:
    key = os.getenv("GOOGLE_API_KEY", "").strip()
    if key:
        return key

    try:
        import config  # Optional local fallback for development only
        return str(getattr(config, "GOOGLE_API_KEY", "")).strip()
    except Exception:
        return ""


api_key = load_api_key()
if not api_key:
    st.error("Missing API key. Set GOOGLE_API_KEY as an environment variable.")
    st.stop()

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Language Definitions
MESSAGES = {
    "en": {"title": "🎾 Tennis Coach Pro - Timmy's Vision Lab", "button": "Start Analysis", "reset": "New Analysis", "spinner": "Analyzing technique...", "report_header": "## 📊 Detailed Technical Diagnostic Report"},
    "zh": {"title": "🎾 网球教练专业版 - Timmy 的视觉实验室", "button": "开始分析", "reset": "开始新分析", "spinner": "正在进行深度技术诊断...", "report_header": "## 📊 深度技术诊断报告"}
}

# Session State
if 'lang' not in st.session_state: st.session_state.lang = 'en'
if 'report_en' not in st.session_state: st.session_state.report_en = None
if 'report_zh' not in st.session_state: st.session_state.report_zh = None

def reset_analysis():
    st.session_state.report_en = None
    st.session_state.report_zh = None
    st.rerun()

def change_lang():
    st.session_state.lang = "en" if st.session_state.lang_picker == "English" else "zh"

st.set_page_config(page_title="Tennis Coach Pro", layout="wide")
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>", unsafe_allow_html=True)

# Header Layout
col1, col2 = st.columns([8, 1])
with col1: st.markdown(f"## {MESSAGES[st.session_state.lang]['title']}")
with col2:
    options = ["English", "中文"]
    idx = 0 if st.session_state.lang == 'en' else 1
    st.selectbox("🌐", options, index=idx, key="lang_picker", on_change=change_lang, label_visibility="collapsed")

uploaded_file = st.file_uploader("Upload video", type=['mov', 'mp4'])

# Buttons Layout (Always visible, centered below uploader)
c1, c2, c3, c4 = st.columns([1, 2, 2, 1])
with c2:
    if st.button(MESSAGES[st.session_state.lang]["reset"], type="secondary", use_container_width=True):
        reset_analysis()
with c3:
    start_btn = st.button(MESSAGES[st.session_state.lang]["button"], type="primary", use_container_width=True)

# Analysis Logic
if start_btn:
    if uploaded_file is None:
        st.warning("Please upload a video first.")
    else:
        temp_path = os.path.join("/tmp", uploaded_file.name)
        with open(temp_path, "wb") as f: f.write(uploaded_file.getbuffer())

        with st.spinner(MESSAGES[st.session_state.lang]["spinner"]):
            video_file = client.files.upload(file=temp_path)
            while video_file.state.name == "PROCESSING":
                time.sleep(5)
                video_file = client.files.get(name=video_file.name)

            prompt = """
            Analyze this tennis training video for technical form based on USTA NTRP/UTR standards.
            Provide an EXHAUSTIVE technical report.
            Structure in TWO sections separated by [ZH_MARK]:
            [EN] English Report...
            [ZH_MARK]
            [ZH] 中文报告...
            """

            response = client.models.generate_content(
                model='gemini-3.1-pro-preview', contents=[video_file, prompt]
            )

            full_text = response.text
            if "[ZH_MARK]" in full_text:
                parts = full_text.split("[ZH_MARK]")
                st.session_state.report_en = parts[0].replace("[EN]", "").strip()
                st.session_state.report_zh = parts[1].replace("[ZH]", "").strip()
            else:
                st.session_state.report_en = full_text
                st.session_state.report_zh = full_text
            st.rerun()

# Display Results
if st.session_state.report_en:
    st.markdown(MESSAGES[st.session_state.lang]["report_header"])
    st.markdown(st.session_state.report_en if st.session_state.lang == 'en' else st.session_state.report_zh)
