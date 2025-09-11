# agentic-challenge
# Agentic AI Challenge – Level 1 & Level 2

This repository demonstrates a two-level tasks:

- **Level 1:** Simple LLM API call and PDF reader.
- **Level 2:** MCP server and client agent that fetches real-time weather data from [WeatherAPI](https://www.weatherapi.com/).

---

## Setup Instructions

1. **Clone the repository**
Commands to be executed in powershell/bash:
git clone https://github.com/deekshitha-c/agentic-challenge.git
cd agentic-challenge

2. **Create a virtual environment and activate it**
python -m venv .venv #for windows powershell
.venv\Scripts\activate # Linux/macOS
source .venv/bin/activate

3. **Install required dependencies**
   pip install -r requirements.txt

4. **Set your WeatherAPI key as an environment variable (for Level 2)**

# Linux/macOS
export WEATHERAPI_KEY="your_api_key_here"
# Windows PowerShell
setx WEATHERAPI_KEY "your_api_key_here"


3
