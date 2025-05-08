from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from dotenv import load_dotenv
import together
from difflib import SequenceMatcher

# Load environment variables
load_dotenv()
together.api_key = os.getenv("TOGETHER_API_KEY")

# Load structured intents
with open("kellytechno_structured_data.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "✅ KellyTech Chatbot API is live. Use POST /chat to talk to the bot."}

# Match query with best intent
def find_best_match(user_input):
    user_input = user_input.lower()
    best_score = 0
    best_response = None

    for intent in intents:
        for pattern in intent["patterns"]:
            score = SequenceMatcher(None, user_input, pattern.lower()).ratio()
            if score > best_score:
                best_score = score
                best_response = intent["response"]

    if best_score > 0.6:
        return best_response
    return None

# Fallback to Together AI
def call_together_ai(prompt):
    print("⚠️ Falling back to Together AI...")
    response = together.Complete.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        prompt=f"You are an IT training institute chatbot. {prompt}",
        max_tokens=200,
        temperature=0.7
    )
    try:
        return response['output']['choices'][0]['text'].strip()
    except Exception:
        return "Sorry, I couldn’t fetch a response from the language model right now."

@app.post("/chat")
def chat(query: Query):
    user_question = query.question.strip()
    matched_response = find_best_match(user_question)

    if matched_response:
        return {
            "source": "json",
            "response": matched_response
        }
    else:
        fallback = call_together_ai(user_question)
        return {
            "source": "together_llm",
            "response": fallback
        }
