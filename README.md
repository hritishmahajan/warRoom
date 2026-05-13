# 🪖 The War Room

<div align="center">

*"Those who cannot remember the past are condemned to repeat it."*
**— George Santayana**

<br/>

[![Launch App](https://img.shields.io/badge/⚔️%20Enter%20The%20War%20Room-FF4B4B?style=for-the-badge&logoColor=white)](https://hritish.streamlit.app/)

**[ 🚀 https://hritish.streamlit.app/ ]**

<br/>

*An AI-powered World War 1 learning platform built by someone who stayed home sick,*
*opened a code editor, and refused to waste the day.*

</div>

---

## 🗺️ The Story Behind This

I've always been fascinated by two things — **history** and **code**. Not separately. Together.

WWI isn't just dates and battles. It's the story of how a single gunshot in Sarajevo unravelled decades of alliances, dragged 30 nations into the bloodiest conflict humanity had ever seen, and reshaped every border on the map. It deserves more than a Wikipedia skim.

So I built a platform that actually *engages* you with it.

This project started on a sick day. No gym. Nowhere to go. Just me, a keyboard, and a genuine curiosity about LangChain. A few hours later, The War Room was live — an AI historian, an interactive timeline, a quiz engine, and a live voice debate mode. All in one app.

That's what I love about code. You can build anything.

---

## ⚔️ What The War Room Does

### 🧠 WWI Tutor
Meet **Dr. Hritish Mahajan** — your personal WWI historian. Ask him anything:
- *"Why did the assassination of Franz Ferdinand start a World War?"*
- *"What was life like in the trenches on the Western Front?"*
- *"How did the Treaty of Versailles plant the seeds for WW2?"*

He remembers your conversation. He answers with passion. He brings dates, names, and places alive.

---

### 📅 WWI Timeline
An interactive explorer of key events from 1914 to 1918. Click any event to expand the full story — the assassination, the Somme, the American entry, the Armistice. Each event comes with historical context and significance.

---

### 🎯 Quiz Mode
Test your WWI knowledge with an AI-powered quiz engine. Dr. Hritish Mahajan generates challenging multiple choice questions, waits for your answer, evaluates it, explains the correct answer with historical depth, then fires the next question. No two sessions are the same.

---

### 🎤 Debate Mode — Voice
The most unique feature. Pick a WWI position to defend:
- *"Germany was solely responsible for WWI"*
- *"The Treaty of Versailles was fair and justified"*
- *"Britain should have stayed out of WWI"*

Then **speak your argument out loud**. Dr. Hritish Mahajan listens, challenges you hard, cites specific dates and events, and pushes back on every weak point. When you're done, say **"Judge"** — he scores your argument out of 10 with detailed feedback.

Powered by **Whisper** (speech-to-text) and **gTTS** (text-to-speech). A real voice debate with an AI historian.

---

## 🔧 How It's Built

### The LangChain LCEL Pipeline

```
User Input
      ↓
ChatPromptTemplate  ←  persona + conversation history
      ↓
LLaMA 3.3 70B via Groq  ←  reasoning and response
      ↓
StrOutputParser  ←  clean string output
      ↓
Streamlit UI  ←  renders the response
```

Every feature — tutor, quiz, debate — runs on its own LangChain LCEL chain. Same building blocks, different behavior.

```python
chain = prompt | llm | StrOutputParser()
```

That one line is the entire pipeline.

### The Debate Mode Audio Flow

```
You speak
    ↓
Whisper (local) transcribes your argument
    ↓
Groq generates Dr. Hritish Mahajan's challenge
    ↓
gTTS converts response to British-accented speech
    ↓
You hear his pushback
    ↓
Repeat until you say "Judge"
```

---

## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| 🧠 AI Framework | LangChain (LCEL) | Pipeline architecture |
| ⚡ LLM Inference | Groq + LLaMA 3.3 70B | Fast, free inference |
| 🎤 Speech to Text | OpenAI Whisper (local) | Transcribe your arguments |
| 🔊 Text to Speech | gTTS | Dr. Hritish Mahajan's voice |
| 🖥️ UI | Streamlit | Multipage web app |
| 🔐 Env Management | python-dotenv | API key security |
| ☁️ Deployment | Streamlit Cloud | Free, GitHub-connected |

---

## 📚 What I Learned Building This

**LCEL pipelines** — `prompt | llm | parser` is the modern LangChain way. Readable, modular, easy to extend.

**ChatPromptTemplate** — prompts are structured templates with roles. System prompts define persona and rules. MessagesPlaceholder injects conversation history.

**Streamlit session_state** — Streamlit reruns the entire script on every interaction. Session state preserves data across those reruns. It's the backbone of any stateful app.

**Whisper locally** — the same model OpenAI charges for, running entirely on your machine. No API key, no cost, no latency from network calls.

**Debugging real errors** — `LLMChain` deprecated. `llama3-8b-8192` decommissioned. `langchain.memory` moved packages. Real development means fighting dependency hell and winning.

**Audio UX in Streamlit** — managing recording keys, audio hashing, and rerun cycles to build a smooth voice interaction loop.

---

## 🚀 Run It Yourself

```bash
# Clone
git clone https://github.com/hritishmahajan/warRoom.git
cd warRoom

# Setup
python -m venv venv
source venv/bin/activate

# Install
pip install -r requirements.txt

# Install ffmpeg (required for Whisper)
brew install ffmpeg  # Mac
# sudo apt install ffmpeg  # Linux

# Configure
echo "GROQ_API_KEY=your_key_here" > .env
# Get a free key at console.groq.com

# Launch
streamlit run app.py
```

---

## 🗂️ Project Structure

```
war-room/
│
├── app.py                   ← Tutor — main chat interface
│
├── pages/
│   ├── 1_Timeline.py        ← Interactive WWI timeline
│   ├── 2_Quiz.py            ← AI-powered quiz engine
│   └── 3_Debate.py          ← Voice debate mode
│
├── chains/
│   ├── __init__.py
│   ├── tutor_chain.py       ← LCEL tutor pipeline
│   ├── quiz_chain.py        ← LCEL quiz pipeline
│   └── debate_chain.py      ← LCEL debate pipeline
│
├── .env                     ← API keys (never committed)
├── .gitignore
└── requirements.txt
```

---

## 🗓️ Roadmap — Phase 2

- [ ] 🔀 **LangGraph upgrade** — agent-based architecture replacing LCEL
- [ ] 📄 **RAG** — real WWI documents feeding the AI for source-grounded answers
- [ ] 🎨 **Frontend redesign** — dark war-room aesthetic with custom CSS
- [ ] 🌍 **More timeline events** — all fronts, not just Western
- [ ] 📊 **Debate scoreboard** — track your debate scores over time

---

## 💭 Why This Matters To Me

I didn't build this to add a line to a resume.

I built it because I genuinely wanted to know how LangChain works — not from a tutorial, but from building something real. And I chose WWI because it's the kind of history that deserves more than a Google search.

The war that was supposed to end all wars. The mud of the Somme. The poetry of Wilfred Owen. The maps redrawn in rooms full of men who'd never seen the frontlines.

That history deserves a good tutor. A good quiz. A good debate.

So I built them.

---

<div align="center">

Built with 🩺 sick day energy + ☕ + genuine curiosity

by **[Hritish Mahajan](https://github.com/hritishmahajan)** 🪖

*Four features. Three chains. One sick day.*

[![Enter The War Room](https://img.shields.io/badge/⚔️%20Enter%20The%20War%20Room-FF4B4B?style=for-the-badge)](https://hritish.streamlit.app/)

</div>