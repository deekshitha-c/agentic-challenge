# agentic-challenge
# Agentic AI Challenge – Level 1 & Level 2

This repository demonstrates a two-level tasks:

- **Level 1:** Simple LLM API call and PDF reader.
- **Level 2:** MCP server and client agent that fetches real-time weather data from [WeatherAPI](https://www.weatherapi.com/).
---
# LLMs/API used: <br>
- Gemini API  # https://aistudio.google.com/apikey
- Weather API # https://www.weatherapi.com/
---
# Project Structure
agentic_ai/<br>
│<br>
├── level1/<br>
│ ├── llm_call.py # Simple Gemini API call<br>
│ └── pdf_reader.py # Extract text from PDF<br>
├── level2/<br>
│ ├── weather_mcp.py # MCP server providing weather data<br>
│ └── client_agent.py # MCP client connecting to server<br>
├── requirements.txt<br>
└── README.md<br>

## Setup Instructions

1. **Clone the repository**
Commands to be executed in powershell/bash:<br>
git clone https://github.com/deekshitha-c/agentic-challenge.git <br>
cd agentic_ai

3. **Create a virtual environment and activate it**
python -m venv .venv 
.venv\Scripts\activate #for windows powershell<br>
source .venv/bin/activate # Linux/macOS<br>

4. **Install required dependencies**
   pip install -r requirements.txt

# Level 1: LLM Call and PDF Reader

1. **Set your Gemini API key as an environment variable**
   export GEMINI_API_KEY="your_api_key_here"   # Mac/Linux <br>
   setx GEMINI_API_KEY "your_api_key_here"     # Windows <br>
   
2. **Execute to call Gemini**
   python level1/llm_call.py <br>
   Output: <br>
   Prompt: Explain to me what agentic AI is. <br>
   Response: Agentic AI refers to...
   
4. **Extract text from a sample pdf # make sure you have a pdf in the same directory as pdf_reader.py <br>**
   python level1/pdf_reader.py

# Level 2: MCP Weather Server + Client

1. **Set your WeatherAPI key as an environment variable (for Level 2)** <br>
   export WEATHERAPI_KEY="your_api_key_here" # Linux/macOS <br>
   setx WEATHERAPI_KEY "your_api_key_here" # Windows PowerShell
   
3. **Run client_agent.py and enter a question regarding the weather in a city. # ex: How is the weather currently in Bangalore?** <br>
   python level2/client_agent.py



