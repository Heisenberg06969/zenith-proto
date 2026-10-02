# 🎙️ Zenith Proto

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Speech_Recognition-Google_STT-EA4335?style=for-the-badge&logo=google&logoColor=white" alt="Speech" />
  <img src="https://img.shields.io/badge/TTS-Edge_TTS-0078D7?style=for-the-badge&logo=microsoft&logoColor=white" alt="TTS" />
  <img src="https://img.shields.io/badge/Status-Prototype_Archive-yellow?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <strong>The foundational proof-of-concept prototype for the Zenith autonomous voice assistant platform.</strong>
</p>

---

## 🌟 Overview

**Zenith Proto** is the early testbed and architectural prototype that laid the groundwork for Zenith 2.0. It demonstrates a multi-layered local execution loop combining voice activity recognition, intent parsing, identity/personality management, persistent conversational memory, and desktop application/search automation.

```text
       🎙️ Microphone
             │
             ▼ (Google Speech Recognition)
     Voice Audio Stream
             │
             ▼
     ┌────────────────────────┐
     │  Layered Pipeline      │
     ├────────────────────────┤
     │ 1. Activation Check    │ ("ok zenith")
     │ 2. Memory Handler      │ (Context store)
     │ 3. Identity Check      │ (Persona lookup)
     │ 4. Search Handler      │ (Web / YouTube)
     │ 5. App Launcher        │ (System targets)
     └────────────────────────┘
             │
             ▼
      🔊 Speech Synthesis (Edge TTS)
```

---

## ✨ Features

- **Wake Word Activation:** Hands-free gating with `"ok zenith"` and `"sleep"` voice triggers.
- **Layered Architecture:** Sequential intent filters for memory, identity responses, web searches, and application execution.
- **Natural Voice Synthesis:** Offline/edge neural speech output using Microsoft Edge TTS.
- **Persistent State Storage:** Lightweight JSON-based memory handler for recall across sessions.

---

## 📁 Repository Structure

```text
Zentih Proto/
├── config/
│   ├── apps.py                 # Registered application launch paths
│   └── websites.py             # Target website shortcuts
├── handlers/
│   ├── open_handler.py         # System application launcher
│   └── search_handler.py       # Google and YouTube search automation
├── identity/
│   ├── general_info/           # Persona facts and self-identity
│   └── memory/                 # JSON memory store & recall handler
├── utils/
│   └── speak.py                # Edge TTS voice driver
├── zenith_proto_main.py        # Main continuous listening loop
└── zenith.bat                  # Windows batch launcher
```

---

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install speechrecognition edge-tts pyaudio
   ```
2. **Run the prototype:**
   ```bash
   cd "Zentih Proto"
   python zenith_proto_main.py
   ```

---

## 🔗 Evolution

For the next-generation, Groq-accelerated voice assistant with live web HUD and agentic tool execution, visit [Zenith 2.0](https://github.com/Heisenberg06969/zenith-2.0).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).