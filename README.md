# 🤖 Kelly Technologies Chatbot

A simple AI-powered chatbot that answers user queries based on predefined intents (from a structured JSON file) and falls back to Together AI LLM for unmatched queries. It is built with **FastAPI** for the backend and a lightweight **HTML/CSS/JS** frontend.

---

## 📂 Project Structure

kellytechno-chatbot/
├── main.py # FastAPI backend server
├── kellytechno_structured_data.json # Intent-based responses
├── chatbot.html # Frontend chatbot UI
├── venv/ # Python virtual environment
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Features

- Intent-based response matching using JSON patterns
- LLM fallback (Together AI) when no intent matches
- Clean, responsive chatbot UI
- Quick replies for frequently asked questions
- Supports `Enter` key to submit messages
- Fully open-source and easy to customize

---

## 🧠 Requirements

- Python 3.8+
- `requests`, `together`, `fastapi`, `uvicorn`, `python-dotenv`

---

## ⚙️ Setup & Run Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/Keerthi2040/Kelly_Chatbot.git
cd Kelly_Chatbot
✅ 2. Create & Activate a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On Mac/Linux
✅ 3. Install the Dependencies
bash
Copy code
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy code
pip install fastapi uvicorn python-dotenv requests together
✅ 4. Set Your Together API Key
Create a .env file in the project root:

ini
Copy code
TOGETHER_API_KEY=your_actual_key_here
✅ 5. Run the Backend Server
bash
Copy code
uvicorn main:app --reload
This will start the API at:

cpp
Copy code
http://127.0.0.1:8000
You can test it via:

bash
Copy code
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"question\": \"What is Data Science training?\"}"
💬 Run the Frontend
To serve chatbot.html at http://localhost:8080/chatbot.html:

bash
Copy code
cd kellytechno-chatbot
python -m http.server 8080
Now visit:

bash
Copy code
http://localhost:8080/chatbot.html
✅ Make sure the FastAPI backend is also running.



📌 To-Do Enhancements
Add voice input using Web Speech API

Add session history or chat memory

Deploy to cloud (Render, Railway, etc.)

Convert JSON into MongoDB backend (optional)

🧑‍💻 Author
Keerthi | GitHub | Made with ❤️ for Kelly Technologies
