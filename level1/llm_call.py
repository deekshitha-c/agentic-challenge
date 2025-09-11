import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def gemini_simple(prompt: str):
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY not set.")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    question = "Explain to me what agentic AI is."
    print("Prompt:", question)
    print("Response:", gemini_simple(question))
