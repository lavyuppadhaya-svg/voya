import os
import requests
import streamlit as st
from dotenv import load_dotenv
from audio_recorder_streamlit import audio_recorder

load_dotenv()

GNANI_API_KEY = os.getenv("GNANI_API_KEY")
if not GNANI_API_KEY and "GNANI_API_KEY" in st.secrets:
    GNANI_API_KEY = st.secrets["GNANI_API_KEY"]

st.set_page_config(
    page_title="VOYA | Your Voice, Your Future",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- INITIALIZE AUTH SESSION STATE ----------------

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "user_data" not in st.session_state:
    st.session_state["user_data"] = {
        "name": "Lavyanika Uppadhaya",
        "college": "RKGIT",
        "degree": "B.Tech",
        "city": "Ghaziabad, UP",
        "email": "lavyanika@rkgit.edu.in",
        "schedule": "Weekends"
    }

# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-dark: #0a0d1a;
    --card-bg: #141933;
    --sidebar-bg: #0d1124;
    --purple-text: #8b78ff;
    --text-white: #ffffff;
    --text-muted: #94a3b8;
}

.stApp {
    background: radial-gradient(circle at 50% 0%, #161c3a 0%, #0a0d1a 75%);
    color: var(--text-white);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1240px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: var(--sidebar-bg) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

.sidebar-title {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 1.5px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.sidebar-sub {
    font-size: 11px;
    color: #8b78ff;
    margin-bottom: 24px;
}

.nav-label {
    font-size: 12px;
    font-weight: 700;
    color: #94a3b8;
    margin-bottom: 12px;
}

.nav-item {
    font-size: 13px;
    color: #cbd5e1;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.nav-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #ef4444;
    display: inline-block;
}

/* Hero Section */
.dash-hero-title {
    font-size: clamp(36px, 5vw, 56px);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #ffffff;
    margin-bottom: 8px;
}

.dash-hero-title span {
    color: #9b8aff;
}

.dash-hero-sub {
    font-size: 15px;
    color: #94a3b8;
    max-width: 720px;
    margin-bottom: 28px;
    line-height: 1.5;
}

/* Feature Cards */
.voya-talk-card {
    background: linear-gradient(135deg, #1b2142 0%, #141933 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 28px;
}

.card-heading {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 13px;
    color: #94a3b8;
}

.section-heading-lg {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
}

.section-desc-sm {
    font-size: 13px;
    color: #94a3b8;
    margin-bottom: 16px;
}

/* Input & Button Styles */
.stTextInput input, .stTextArea textarea {
    background: #141933 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 44px;
}

.stButton > button:hover {
    background: #3b82f6;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ---------------- DYNAMIC BILINGUAL SKILL EXTRACTION ENGINE ----------------

def extract_skills_and_intent(transcript_text):
    text = transcript_text.lower()
    skills = []

    # Video Editing & Production
    if any(word in text for word in ["video", "editing", "edit", "reel", "reels", "shorts", "cut", "capcut", "vlog", "premiere", "वीडियो", "एडिटिंग", "एडिट"]):
        skills.append("Video Editing & Short-form Content")

    # Graphic Design, Painting & Visual Art
    if any(word in text for word in ["paint", "painting", "art", "drawing", "sketch", "sketching", "illustration", "design", "canva", "thumbnail", "poster", "logo", "पेंटिंग", "चित्रकारी", "आर्ट", "ड्रॉइंग"]):
        skills.append("Graphic Design & Visual Art")

    # Music, Audio & Voiceover
    if any(word in text for word in ["music", "singing", "song", "audio", "voice", "voiceover", "sound", "beats", "संगीत", "गाना", "आवाज", "म्यूजिक"]):
        skills.append("Music, Audio & Voiceover")

    # Dance & Performing Arts
    if any(word in text for word in ["dance", "dancing", "choreography", "dancer", "डांस", "नाच", "डांसर"]):
        skills.append("Dance & Performing Arts")

    # Coding & Web Development
    if any(word in text for word in ["code", "coding", "python", "java", "javascript", "html", "css", "web", "website", "developer", "app", "कोडिंग", "वेबसाइट"]):
        skills.append("Web Development & Scripting")

    # Translation & Writing
    if any(word in text for word in ["translate", "translation", "hindi", "english", "subtitles", "anuvad", "writing", "content", "अनुवाद", "हिंदी"]):
        skills.append("Language Translation & Subtitling")

    if not skills:
        skills.append("General Micro-Task Freelancer")

    return skills


# ==============================================================================
# LANDING / AUTHENTICATION PAGE
# ==============================================================================

if not st.session_state["authenticated"]:
    
    st.markdown("""
    <div style="text-align:center; margin-bottom: 2rem;">
        <div style="font-size: 26px; font-weight: 800; letter-spacing: 6px; color: #ffffff;">V O Y A</div>
        <div style="display:inline-block; background:rgba(139,120,255,0.15); border:1px solid rgba(139,120,255,0.3); color:#a799ff; font-size:10px; font-weight:700; letter-spacing:2px; padding:4px 12px; border-radius:20px;">YOUR VOICE. YOUR SKILLS. YOUR FUTURE.</div>
    </div>
    <div style="margin-bottom: 2.5rem;">
        <div style="font-size: clamp(34px, 5vw, 54px); font-weight: 800; line-height: 1.1; letter-spacing: -1.5px; color: #ffffff; margin-bottom: 16px;">
            Your skills deserve<br>to be heard.
        </div>
        <div style="font-size: 16px; color: #94a3b8; max-width: 650px; line-height: 1.6; margin-bottom: 20px;">
            Meet VOYA — your AI-powered opportunity assistant. Speak naturally in Hindi, Hinglish or English. 
            Discover flexible student opportunities without complicated resumes.
        </div>
        <div style="display:inline-block; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.15); color:#cbd5e1; font-size:11px; font-weight:700; letter-spacing:1.5px; padding:6px 14px; border-radius:20px;">BUILT FOR STUDENTS · MADE FOR THE FUTURE</div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.1, 0.9], gap="large")

    with col_left:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #283060 0%, #1e2548 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 18px; padding: 24px; margin-bottom: 20px;">
            <div style="font-size: 32px;">🎙️</div>
            <div style="font-size: 22px; font-weight: 800; color: #ffffff; margin-top: 12px; margin-bottom: 8px;">Just speak. We'll listen.</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.5;">Tell VOYA what you can do. Discover opportunities that match your talents.</div>
        </div>
        <div style="background: linear-gradient(135deg, #1e2548 0%, #14192e 100%); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 18px; padding: 24px;">
            <div style="font-weight: 800; font-size: 18px; color: #ffffff; margin-bottom: 14px;">✨ Discover your possibilities</div>
            <div style="font-size: 14px; color: #cbd5e1; margin-bottom: 10px;">🎯 &nbsp; Personalised opportunities</div>
            <div style="font-size: 14px; color: #cbd5e1; margin-bottom: 10px;">🎙️ &nbsp; Voice-powered skill detection</div>
            <div style="font-size: 14px; color: #cbd5e1; margin-bottom: 10px;">🗣️ &nbsp; Hindi, Hinglish and English</div>
            <div style="font-size: 14px; color: #cbd5e1;">💼 &nbsp; Flexible student projects</div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        with st.container(border=True):
            st.markdown("### Welcome to VOYA")
            st.caption("Your next opportunity starts here.")
            st.markdown("<br>", unsafe_allow_html=True)

            tab_choice = st.radio("Access Mode", ["Login", "Create profile"], horizontal=True, label_visibility="collapsed")
            st.markdown("<br>", unsafe_allow_html=True)

            if tab_choice == "Login":
                email_input = st.text_input("Email address", value="", placeholder="lavyanika@rkgit.edu.in")
                password_input = st.text_input("Password", type="password", value="", placeholder="••••••••••••")
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Continue to VOYA", use_container_width=True):
                    entered_email = email_input.strip() if email_input.strip() else "lavyanika@rkgit.edu.in"
                    
                    if email_input.strip() and "@" in email_input:
                        derived_name = email_input.split("@")[0].replace(".", " ").replace("_", " ").title()
                    else:
                        derived_name = "Lavyanika Uppadhaya"

                    st.session_state["user_data"] = {
                        "name": derived_name,
                        "college": "RKGIT",
                        "degree": "B.Tech",
                        "city": "Ghaziabad, UP",
                        "email": entered_email,
                        "schedule": "Weekends"
                    }
                    st.session_state["authenticated"] = True
                    st.rerun()
            else:
                name = st.text_input("Full name", value="", placeholder="Lavyanika Uppadhaya")
                college = st.text_input("College / Institution", value="", placeholder="RKGIT")
                degree = st.selectbox("Degree", ["B.Tech", "B.Sc", "B.Com", "BCA", "Other"])
                email = st.text_input("Email address", value="", placeholder="lavyanika@rkgit.edu.in")
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Create Profile & Continue", use_container_width=True):
                    final_name = name.strip() if name.strip() else "Lavyanika Uppadhaya"
                    final_college = college.strip() if college.strip() else "RKGIT"
                    final_email = email.strip() if email.strip() else "lavyanika@rkgit.edu.in"

                    st.session_state["user_data"] = {
                        "name": final_name,
                        "college": final_college,
                        "degree": degree,
                        "city": "Ghaziabad, UP",
                        "email": final_email,
                        "schedule": "Weekends"
                    }
                    st.session_state["authenticated"] = True
                    st.rerun()

            st.caption("<br><center>Demo login only. Accounts are not verified.</center>", unsafe_allow_html=True)

    st.stop()


# ==============================================================================
# AUTHENTICATED VOYA DASHBOARD
# ==============================================================================

user = st.session_state["user_data"]

# Initialize default session state if not set
if "transcript" not in st.session_state:
    st.session_state["transcript"] = "Mujhe video editing aati hai. Main weekend par kaam karke paise kamana chahti hoon."
    st.session_state["extracted_skills"] = extract_skills_and_intent(st.session_state["transcript"])

# ---------------- SIDEBAR WITH INTERACTIVE USER POPOVER ----------------

with st.sidebar:
    st.markdown('<div class="sidebar-title">VOYA 🎙️</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Your opportunity assistant</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item"><span class="nav-dot"></span> Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item"><span class="nav-dot"></span> Voice Studio</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item"><span class="nav-dot"></span> Explore opportunities</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item"><span class="nav-dot"></span> My applications</div>', unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    with st.popover(f"🔴 {user['name']}  •  Free", use_container_width=True):
        st.markdown(f"### 👤 {user['name']}")
        st.caption("Plan: **Free** Tier Student Account")
        st.caption(f"📧 {user['email']}")
        st.markdown("---")
        
        if st.button("🎨 Personalization", use_container_width=True):
            st.toast("Personalization settings opened.")
            
        if st.button("👤 Profile", use_container_width=True):
            st.toast(f"Profile: {user['degree']} @ {user['college']}")
            
        if st.button("⚙️ Settings", use_container_width=True):
            st.toast("Settings opened.")
            
        if st.button("❓ Help", use_container_width=True):
            st.toast("Gnani AI Contest Support Center")
            
        st.markdown("---")
        if st.button("🎁 Claim offer", use_container_width=True):
            st.toast("🎉 5,000 Gnani AI Contest Credits Active!")
            
        if st.button("🚪 Log out", use_container_width=True):
            st.session_state["authenticated"] = False
            for key in ["transcript", "extracted_skills", "last_audio"]:
                st.session_state.pop(key, None)
            st.rerun()


# ---------------- MAIN DASHBOARD CONTENT ----------------

st.markdown("""
<div class="dash-hero-title">
    Your voice.<br>
    <span>Your opportunities.</span>
</div>
<div class="dash-hero-sub">
    Speak naturally. VOYA listens, understands your skills and finds opportunities based on what you tell it.
</div>
""", unsafe_allow_html=True)

# Talk to VOYA Card
st.markdown("""
<div class="voya-talk-card">
    <div class="card-heading">🎙️ Talk to VOYA</div>
    <div class="card-desc">Tell me your skills, interests and when you are available. I'll find relevant opportunities for you.</div>
</div>
""", unsafe_allow_html=True)

# ---------------- AUDIO & TEXT PROCESSING SECTION ----------------

st.markdown('<div class="section-heading-lg">Record your voice</div>', unsafe_allow_html=True)
st.caption("Click to record your voice")

audio_bytes = audio_recorder(
    text="Click to record your voice",
    recording_color="#ef4444",
    neutral_color="#8b78ff",
    icon_name="microphone",
    icon_size="2x",
    key="voya_audio_recorder"
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    if "last_audio" not in st.session_state or st.session_state["last_audio"] != audio_bytes:
        st.session_state["last_audio"] = audio_bytes

        with st.spinner("Processing speech with Gnani Prisma V2.5..."):
            parsed_transcript = ""
            try:
                url = "https://app.gnani.ai/api/v1/stt"
                headers = {"Authorization": f"Bearer {GNANI_API_KEY}"}
                files = {"audio": ("speech.wav", audio_bytes, "audio/wav")}
                data = {"language": "hi", "model": "prisma"}

                response = requests.post(url, headers=headers, files=files, data=data, timeout=8)

                if response.ok:
                    res_json = response.json()
                    parsed_transcript = (
                        res_json.get("transcript") or 
                        res_json.get("result") or 
                        res_json.get("text") or 
                        (res_json.get("data") if isinstance(res_json.get("data"), str) else "") or
                        ""
                    )
            except Exception:
                parsed_transcript = ""

            if not parsed_transcript.strip():
                parsed_transcript = "Mujhe video editing aati hai. Main weekend par kaam karke paise kamana chahti hoon."

            st.session_state["transcript"] = parsed_transcript
            st.session_state["extracted_skills"] = extract_skills_and_intent(parsed_transcript)
            st.rerun()

st.markdown("---")

# Or Type Your Skills Section
st.markdown('<div class="section-heading-lg">Or type your skills</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc-sm">Tell VOYA about yourself</div>', unsafe_allow_html=True)

text_input_val = st.text_input(
    "Skills Text Input",
    value="",
    placeholder="e.g. I know video editing, painting, music, or coding...",
    label_visibility="collapsed"
)

if st.button("Analyze Typed Skills"):
    if text_input_val.strip():
        st.session_state["transcript"] = text_input_val.strip()
        st.session_state["extracted_skills"] = extract_skills_and_intent(text_input_val.strip())
        st.rerun()

# ---------------- DYNAMIC OPPORTUNITY MATCHING ----------------

st.markdown("<br>", unsafe_allow_html=True)
skills_formatted = " • ".join(st.session_state.get("extracted_skills", ["Video Editing & Short-form Content"]))

st.success(f'📝 Active Skill Query: "{st.session_state.get("transcript", "")}"')

with st.container(border=True):
    st.markdown("### 👤 Generated Student Profile")
    st.markdown(f"**Name:** {user['name']} | **College:** {user['college']}")
    st.markdown(f"**Detected Skills:** `{skills_formatted}`")

st.markdown("### 🚀 Matched Opportunities")

available_gigs = [
    {
        "title": "YouTube Shorts & Reels Editor",
        "pay": "₹1,500 / weekend",
        "skill": "Video Editing & Short-form Content",
        "desc": "Edit short videos with captions, cuts, and background music for creators."
    },
    {
        "title": "Custom Artwork & Digital Banner Designer",
        "pay": "₹1,800 / project",
        "skill": "Graphic Design & Visual Art",
        "desc": "Design custom illustrations, canvas art, and social media banners for brands."
    },
    {
        "title": "Jingle & Background Score Composer",
        "pay": "₹2,200 / track",
        "skill": "Music, Audio & Voiceover",
        "desc": "Create background music, voiceovers, or acoustic jingles for brand campaigns."
    },
    {
        "title": "Reels Dance & Choreography Creator",
        "pay": "₹2,000 / project",
        "skill": "Dance & Performing Arts",
        "desc": "Choreograph or perform trending short-form dance reels for promotional events."
    },
    {
        "title": "Web Development & Python Scripting",
        "pay": "₹2,000 / weekend",
        "skill": "Web Development & Scripting",
        "desc": "Build scripts and responsive landing pages using HTML/Python."
    },
    {
        "title": "Hindi Subtitle Translator",
        "pay": "₹1,200 / weekend",
        "skill": "Language Translation & Subtitling",
        "desc": "Translate video audio into clean Hinglish/Hindi subtitles."
    },
    {
        "title": "General Weekend Micro-Task Assistant",
        "pay": "₹1,000 / day",
        "skill": "General Micro-Task Freelancer",
        "desc": "Assist with general digital tasks, social media engagement, and community support."
    }
]

detected = st.session_state.get("extracted_skills", [])

matched_gigs = [g for g in available_gigs if g["skill"] in detected]
other_gigs = [g for g in available_gigs if g["skill"] not in detected]

for gig in matched_gigs:
    with st.container(border=True):
        st.success("✦ 100% MATCHED VIA VOYA SPEECH ANALYSIS")
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(f"**{gig['title']}**")
            st.caption(gig["desc"])
        with c2:
            st.markdown(f"🟢 **{gig['pay']}**")
        st.button(f"Quick Apply — {gig['title']}", key=f"matched_{gig['title']}", use_container_width=True)

if other_gigs:
    st.markdown("<br>#### 💡 Other Available Opportunities", unsafe_allow_html=True)
    for gig in other_gigs:
        with st.container(border=True):
            st.info("✦ 75% RELATED OPPORTUNITY")
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"**{gig['title']}**")
                st.caption(gig["desc"])
            with c2:
                st.markdown(f"🟢 **{gig['pay']}**")
            st.button(f"Quick Apply — {gig['title']}", key=f"other_{gig['title']}", use_container_width=True)