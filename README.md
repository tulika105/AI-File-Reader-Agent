# 📄 AI File Reader Agent

An AI-powered file understanding system built using **modern LangChain (LCEL)** and **Groq (LLaMA models)**.  
The system reads a text file, understands the user’s intent, and dynamically applies the appropriate AI-powered operation such as summarization, key point extraction, or explanation.

This project is designed to deeply understand **agent fundamentals, tool design, and LCEL-based orchestration**, without relying on legacy agent abstractions or LangGraph.

---

## 🎯 What This Project Does

- Reads and validates `.txt` files
- Accepts natural language instructions from the user
- Uses an LLM to **reason about intent**
- Dynamically routes the request to the correct tool
- Uses LLM to transform the content
- Displays clean, readable output in the terminal

---
## 🧠 How It Works

The system is built using modern LangChain concepts.

### Core Components

- **LLM (AI Brain)**  
  Understands your instruction and decides what should be done.

- **Tools**  
  Small functions that actually do the work:
  - Summarizing
  - Extracting key points
  - Explaining text

- **LCEL (LangChain Expression Language)**  
  Connects everything together and controls the flow.

### Execution Flow
User Input
->
File Loader (preprocessing & validation)
->
LLM-based Intent Reasoning
->
Tool Routing (LCEL)
->
LLM-powered Tool Execution
->
Final Output

> Note: In modern LangChain, LCEL-based systems rely on **explicit control flow**, not autonomous ReAct loops.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **LangChain Core (LCEL)**
- **Groq (LLaMA 3 models)**
- **python-dotenv**
- **Pathlib**

---

### ⚙️ How to Set Up and Run

### 1️⃣ Clone the project
git clone https://github.com/<your-username>/file-reader-agent.git
cd file-reader-agent

### 2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your API key
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here

### ▶️ Run the Agent
python agent.py

- You will be asked to:
- Enter the file path
- Enter what you want to do with the file

### Example
- Enter file path:
- sample_files/sample.txt

- What do you want to do with this file?
- Summarize this content
