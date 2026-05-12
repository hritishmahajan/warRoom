# 🪖 The War Room

<div align="center">

*"Those who cannot remember the past are condemned to repeat it."*
**— George Santayana**

<br/>

[![Launch App](https://img.shields.io/badge/⚔️%20Enter%20The%20War%20Room-FF4B4B?style=for-the-badge&logoColor=white)](https://hritish.streamlit.app/)

**[ 🚀 https://hritish.streamlit.app/ ]**

<br/>

*An AI-powered World War 1 tutor built by someone who stayed home sick,*
*opened a code editor, and refused to waste the day.*

</div>

---

## 🗺️ The Story Behind This

I've always been fascinated by two things — **history** and **code**. Not separately. Together.

WWI isn't just dates and battles. It's the story of how a single gunshot in Sarajevo unravelled decades of alliances, dragged 30 nations into the bloodiest conflict humanity had ever seen, and reshaped every border on the map. It deserves more than a Wikipedia skim.

So I built a tutor that actually *talks* to you about it.

This project started on a sick day. No gym. Nowhere to go. Just me, a keyboard, and a genuine curiosity about LangChain. Three hours later, Dr. Hritish Mahajan — WWI historian, AI-powered, endlessly patient — was live on the internet.

That's what I love about code. You can build anything.

---

## ⚔️ What The War Room Does

Meet **Dr. Hritish Mahajan** — your personal WWI historian.

Ask him anything:
- *"Why did the assassination of Franz Ferdinand start a World War?"*
- *"What was life like in the trenches on the Western Front?"*
- *"How did the Treaty of Versailles plant the seeds for WW2?"*
- *"Who were the real villains — and were there any heroes?"*

He remembers your conversation. He answers with passion. He brings dates, names, and places alive.

Not a chatbot. A tutor.

---

## 🔧 How It's Built

This is where the history meets the code.

```
User Question
      ↓
ChatPromptTemplate  ←  injects Dr. Hritish Mahajan's persona
      ↓
MessagesPlaceholder ←  injects full conversation history (memory)
      ↓
LLaMA 3.3 70B via Groq  ←  thinks, reasons, responds
      ↓
StrOutputParser  ←  clean string output
      ↓
Streamlit UI  ←  renders the conversation
```

This pipeline is called **LCEL — LangChain Expression Language**. The `|` operator chains each step like Unix pipes. It's elegant, readable, and the modern way to build LangChain apps.

```python
chain = prompt | llm | StrOutputParser()
```

That one line connects everything. That's the magic.

---

## 🛠️ Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| 🧠 AI Framework | LangChain (LCEL) | Modern pipeline architecture |
| ⚡ LLM Inference | Groq + LLaMA 3.3 70B | Fast, free, powerful |
| 🖥️ UI | Streamlit | Python-native web apps |
| 🔐 Env Management | python-dotenv | Keep secrets safe |
| ☁️ Deployment | Streamlit Cloud | Free, GitHub-connected |

---

## 📚 What I Learned Building This

I didn't just learn *about* LangChain. I learned *through* it. Here's what clicked:

**`ChatPromptTemplate`** — prompts aren't just strings. They're structured templates with roles (system, human, AI) that give the model context and personality before the conversation even starts.

**`MessagesPlaceholder`** — the secret behind memory. It's a slot in your prompt that gets filled with the entire conversation history on every call. Without it, the AI forgets you the moment you hit enter.

**LCEL pipelines** — the `|` operator chains steps elegantly. `prompt | llm | parser` is readable, modular, and easy to extend. Old LangChain used `LLMChain`. New LangChain uses this.

**Streamlit `session_state`** — Streamlit reruns your entire script on every interaction. Session state is how you preserve data across those reruns. It's the backbone of any stateful Streamlit app.

**Debugging real errors** — `LLMChain` deprecated. `llama3-8b-8192` decommissioned. `langchain.memory` moved packages. Real development means fighting with dependency hell and winning.

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

# Configure — get a free key at console.groq.com
echo "GROQ_API_KEY=your_key_here" > .env

# Launch
streamlit run app.py
```

Open `http://localhost:8501` and ask Dr. Hritish Mahajan anything about WWI.

---

## 🗂️ Project Structure

```
war-room/
│
├── app.py                 ← Streamlit UI & chat interface
│
├── chains/
│   ├── __init__.py        ← makes chains a Python package
│   └── tutor_chain.py     ← the LCEL pipeline (the brain)
│
├── .env                   ← your secrets (never committed)
├── .gitignore             ← keeps venv & secrets off GitHub
└── requirements.txt       ← dependency manifest
```

---

## 🗓️ Roadmap — Phase 2

The foundation is live. Here's what's coming:

- [ ] 📅 **WWI Timeline** — interactive explorer of key events 1914-1918
- [ ] 🧠 **Quiz Mode** — test your knowledge, get graded by AI
- [ ] ⚔️ **Debate Mode** — argue a WWI position, Dr. Hritish Mahajan judges your case
- [ ] 🔀 **LangGraph upgrade** — replace LCEL with agent-based architecture
- [ ] 📄 **RAG** — feed real WWI documents into the model for source-grounded answers

Each upgrade makes it less of a project and more of a product.

---

## 💭 Why This Matters To Me

I didn't build this to add a line to a resume.

I built it because I genuinely wanted to know how LangChain works — not from a tutorial, but from *building something real*. And I chose WWI because it's the kind of history that deserves more than a Google search.

The war that was supposed to end all wars. The mud of the Somme. The poetry of Wilfred Owen. The maps redrawn in rooms full of men who'd never seen the frontlines.

That history deserves a good tutor.

So I built one.

---

<div align="center">

Built with 🩺 sick day energy + ☕ + genuine curiosity

by **[Hritish Mahajan](https://github.com/hritishmahajan)** 🪖

*If you made it this far — go ask Dr. Hritish Mahajan something about WWI.*
*He's been waiting.*

[![Enter The War Room](https://img.shields.io/badge/⚔️%20Enter%20The%20War%20Room-FF4B4B?style=for-the-badge)](https://hritish.streamlit.app/)

</div>