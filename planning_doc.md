## AI German Tutor - Desktop App Development Blueprint

### Project Goals

1. **Primary Goal:** Create a desktop AI German Tutor to practice speaking and listening, helping improve German language skills through conversational practice.
2. **Secondary Goal:** Learn and demonstrate end-to-end AI/LLM software development skills, including local AI integration, STT/TTS, and cross-platform app development.

---

### High-Level Architecture

```
[User Voice Input]
       │
       ▼
[STT: Whisper large-v3-turbo]  ---> German speech → text
       │
       ▼
[AI Model: Ollama + OpenEuroLLM-German]  ---> German conversation with adaptive difficulty
       │
       ▼
[TTS: Coqui TTS + German Thorsten voice]  ---> Natural German speech output
       │
       ▼
[React Frontend + FastAPI Backend]  ---> Local web app (localhost)
```

* All processing stays **local and offline** on MacBook M2.
* FastAPI (Python) orchestrates all AI components.
* React frontend handles UI and audio recording/playback.

---

### Optimized Tech Stack

| Component             | Technology | Notes                                             |
| --------------------- | ---------- | ------------------------------------------------- |
| Frontend              | React      | Audio recording, chat interface, conversation history |
| Backend               | FastAPI (Python) | Orchestrates STT → LLM → TTS pipeline |
| STT (Speech-to-Text)  | Whisper large-v3-turbo | Excellent German accuracy, 8x faster than large |
| AI Model              | Ollama + OpenEuroLLM-German (7B) | Purpose-built for German conversation |
| TTS (Text-to-Speech)  | Coqui TTS + German Thorsten voice | Natural German pronunciation |
| Packaging (later)     | Tauri | Simpler than Electron, Rust-based |

**System Requirements:** MacBook Air M2 + 16GB RAM (perfect for this project!)

---

### MVP Features

1. **Voice conversation:** Speak German → AI responds in German with natural voice output
2. **Adaptive difficulty:** AI adjusts complexity slightly above user's current level
3. **Conversation history:** Display and review past conversations
4. **Learning feedback:** Grammar tips and vocabulary suggestions
5. **Voice controls:** Start/stop recording, replay responses, clear history

---

### Development Phases - AI Learning Focused

**Phase 1: AI Foundation Setup (Days 1-3)**
**Learning Goals:** Local AI ecosystem, model management
* Install Ollama and explore local model management
* Test German models: SmolLM2-German → OpenEuroLLM-German  
* Set up FastAPI project structure
* Create basic LLM chat endpoint and verify M2 performance

**Phase 2: Speech Processing Pipeline (Days 4-6)** 
**Learning Goals:** Audio processing, STT/TTS integration
* Integrate Whisper for German speech-to-text
* Add Coqui TTS for German text-to-speech  
* Create voice processing FastAPI endpoints
* Test complete STT → LLM → TTS pipeline

**Phase 3: Frontend Integration (Days 7-10)**
**Learning Goals:** AI-powered UI, real-time audio
* Create React app with audio recording capabilities
* Connect to FastAPI backend endpoints
* Build conversation interface with history
* Add real-time feedback during AI processing

**Phase 4: Intelligent Tutoring Features (Days 11-14)**
**Learning Goals:** Advanced AI features, prompt engineering
* Design adaptive difficulty system (stays slightly above user level)
* Add conversation context management for learning progression
* Implement grammar feedback and vocabulary building
* Build conversation insights and learning analytics

**Phase 5: Production & Distribution (Days 15-21)**
**Learning Goals:** AI deployment, performance optimization, distribution
* Optimize performance and response times
* Add comprehensive error handling for all AI components  
* Create Docker configuration for easy sharing
* Package as desktop app using Tauri (optional)
* Create demo video and portfolio documentation
* **Distribution:** Docker image + setup instructions for classmates

---

### Key Learning Outcomes

By completing this project, you'll master:
* **Local AI model management** with Ollama
* **Speech processing pipelines** (STT/TTS integration)
* **AI application architecture** (FastAPI + React patterns)
* **Prompt engineering** for language learning applications
* **End-to-end AI software development** from prototype to packaged app

---

### Portfolio Strategy

* **Demo video:** Show natural German conversation with voice interaction
* **GitHub repository:** Well-documented code demonstrating AI integration skills
* **Technical blog post:** Document the learning process and AI development insights
* **Desktop app:** Demonstrates real engineering skill and local AI deployment

---

### Distribution Strategy for German Class Sharing

**Development:** Local setup on your MacBook M2 (optimal performance)
**Sharing Options:**
1. **Docker Distribution** - `docker run german-tutor` (recommended for consistency)
2. **Desktop Executables** - Single-file apps for Mac/Windows/Linux  
3. **Setup Scripts** - Automated installation for each platform

**Hardware Adaptation:**
* **High-end machines:** OpenEuroLLM-German (7B) - full experience
* **Lower-spec machines:** SmolLM2-German (360M) - lightweight version
* **Automatic detection:** App selects best model based on available RAM

---

### Architecture Benefits

* **Completely FREE:** No API costs, runs entirely on student devices
* **Privacy-focused:** All data stays local, works offline  
* **Shareable:** Easy distribution to classmates via Docker or executables
* **Learning-optimized:** Understand every component of the AI pipeline
* **Portfolio-worthy:** Real AI software development + deployment experience
* **Scalable:** Can add features like lesson generation, conversation export, or mobile deployment later
