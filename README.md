# 🪖 The War Room
### Your Personal WWI History Tutor — Dr. Hritish Mahajan

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://hritish.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge)](https://langchain.com)

> **[🚀 Launch The War Room](https://hritish.streamlit.app/)**

---

## What is this?

The War Room is an AI-powered World War 1 tutor built with LangChain and Groq. Ask anything about WWI — battles, causes, key figures, treaties, the human cost — and get deep, historically rich answers from Dr. Hritish Mahajan, your personal WWI historian.

The app remembers your conversation, so you can go deep on any topic without repeating yourself.

---

## Features

- 🧠 **AI Tutor** — Ask anything about WWI and get detailed, passionate answers
- 💬 **Conversation Memory** — The tutor remembers what you've discussed
- ⚡ **Powered by Groq** — Fast inference using LLaMA 3.3 70B
- 🔗 **Built with LangChain LCEL** — Modern AI pipeline architecture

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | AI pipeline framework (LCEL) |
| Groq | LLM inference (LLaMA 3.3 70B) |
| Streamlit | Web interface |
| Python | Core language |

---

## Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/hritishmahajan/warRoom.git
cd warRoom
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file:
```
GROQ_API_KEY=your_groq_key_here
```

Get a free Groq API key at https://console.groq.com

**5. Run the app**
```bash
streamlit run app.py
```

---

## What I Learned

This project was built to learn LangChain from scratch. Key concepts covered:

- **LCEL (LangChain Expression Language)** — chaining `prompt | llm | parser` pipelines
- **ChatPromptTemplate** — building reusable prompts with system personas and variables
- **MessagesPlaceholder** — injecting conversation history for memory
- **Streamlit session_state** — persisting data across reruns
- **Deploying AI apps** — GitHub + Streamlit Cloud workflow

---

## Project Structure

```
war-room/
├── app.py              # Streamlit UI
├── chains/
│   ├── __init__.py
│   └── tutor_chain.py  # LangChain LCEL pipeline
├── .env                # API keys (not committed)
├── .gitignore
└── requirements.txt
```

---

## Roadmap (Phase 2)

- [ ] WWI Timeline explorer
- [ ] Quiz mode — test your WWI knowledge
- [ ] Debate Mode — argue a position, AI judges your argument
- [ ] Upgrade to LangGraph
- [ ] RAG with real WWI documents

---

Built by [Hritish Mahajan](https://github.com/hritishmahajan) 🪖