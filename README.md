# 🎙️ VOYA — Voice Opportunity Intelligence

> **Connecting Indian college talent to localized weekend micro-gigs through natural speech.**  
> *Built for The Great Indian AI Internship Challenge by Gnani AI.*

---

## 📌 Project Overview

Across India, millions of college students in Tier-2 and Tier-3 cities possess practical digital skills like video editing, graphic design, painting, coding, or language translation. However, they face significant barriers when navigating traditional job boards that require complex English resumes.

**VOYA (Voice Opportunity Intelligence)** eliminates this barrier by offering a voice-first opportunity engine. Students simply speak their skills naturally in Hindi, Hinglish, or English. VOYA processes the audio stream via **Gnani AI's Prisma STT engine**, extracts core skill intent, and dynamically matches them to relevant weekend micro-gigs with a real-time **100% Match** score.

---

## ✨ Key Features

- **🎙️ Voice-First Input Processing:** Students record spoken skills in natural Hindi, Hinglish, or English (*"Mujhe video editing aati hai..."*).
- **⚡ Powered by Gnani AI Prisma STT:** Real-time audio buffer parsing tuned for Indian regional accents and code-mixed phrasing.
- **🏷️ Bilingual Skill Extraction Engine:** Custom regex and keyword parsing across multi-category domains (Video Editing, Visual Art/Painting, Music, Dance, Coding, Translation).
- **🎯 Dynamic Gig Recommendation:** Real-time opportunity database filtering that surfaces top-matched gigs to position #1 with a green verification score badge.
- **🎨 Dark Glassmorphism UI:** Responsive, modern dashboard built with Python, Streamlit, and custom CSS styling.

---

## 🛠️ Tech Stack

- **Frontend & UI Framework:** Python, Streamlit
- **Speech-to-Text Engine:** Gnani AI Prisma STT API
- **Audio Interface:** `audio-recorder-streamlit`
- **Environment Management:** `python-dotenv`
- **Deployment:** Streamlit Cloud & GitHub

---

## 🚀 Quick Start & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/lavyuppadhaya-svg/voya.git](https://github.com/lavyuppadhaya-svg/voya.git)
cd voya