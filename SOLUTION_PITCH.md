# VOYA: Voice Opportunity Intelligence
**Voice-Driven Skill Extraction & Micro-Gig Matching for Indian College Students**
*Author:* Lavyanika Uppadhaya | B.Tech, Raj Kumar Goel Institute of Technology  
*Challenge:* The Great Indian AI Internship Challenge (Gnani AI)  
*Live App:* https://voya-studio.streamlit.app | *Repository:* https://github.com/lavyuppadhaya-svg/voya

---

### Executive Summary
Millions of students across India’s Tier 2 and Tier 3 cities possess high-demand digital skills (such as video editing, graphic design, and web development) but face significant language and structural barriers when navigating traditional, English-heavy resume portals. **VOYA (Voice Opportunity Intelligence)** eliminates traditional resume friction by enabling students to describe their capabilities naturally in Hindi, Hinglish, or English using voice input. Powered by **Gnani AI’s Prisma STT engine**, VOYA transcribes spoken intent in real-time, extracts core technical skills, and dynamically matches students with verified weekend micro-gigs.

---

### Problem Statement
1. **Resume Barrier:** Traditional freelance platforms require complex written English resumes, excluding non-native speakers with strong practical skills.
2. **Skill Misalignment:** Indian micro-employers need immediate, task-focused weekend talent (e.g., reels editing, subtitle translation), but existing job boards prioritize full-time traditional hiring formats.
3. **Accent & Dialect Exclusion:** Standard global Speech-to-Text (STT) engines struggle to parse Indian accent variations and code-mixed speech (Hinglish).

---

### Technical Architecture & Gnani AI Integration
* **Frontend UI:** Glassmorphic Streamlit web application with custom CSS styling and responsive session state control.
* **Audio Capture:** Real-time browser audio recording via `audio-recorder-streamlit`.
* **Speech-to-Text Engine:** Integrated with **Gnani AI Prisma STT API** (`/api/v1/stt`) configured for high-accuracy Indian language processing (`language: hi`, `model: prisma`).
* **NLP & Skill Engine:** Pattern-matching keyword extraction engine parsing transcribed text into structured skill categories (*Video Editing*, *Language Translation*, *Graphic Design*, *Software Development*).
* **State & Authentication:** Custom session-state authentication layer managing student profiles, institutional email verification, and interactive popover navigation.

---

### Key Features & Workflow
1. **Glassmorphic Student Portal:** Dual-mode authentication for existing accounts and institutional signup (`.edu.in`).
2. **Voice Studio:** Direct one-click recording supporting natural Hindi/Hinglish speech inputs.
3. **Real-Time Skill Matching:** Automated skill tag extraction pairing users directly with active weekend gigs showing visual match scores (`✦ 100% MATCHED VIA VOYA`).
4. **Fallback Text Analyzer:** Dual-input model supporting both spoken audio and typed intent queries.

---

### Impact & Market Opportunity
VOYA democratizes gig access for over 30 million Indian college students. By converting natural voice into structured opportunity matching, VOYA enables Tier 2/3 youth to achieve financial independence through localized weekend micro-work.