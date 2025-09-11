import os
import requests
import fastmcp

WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")

server = fastmcp.FastMCP("weather-mcp")

@server.tool()
def get_weather(city: str) -> str:
    """Fetch current weather for a given city using WeatherAPI."""
    if not WEATHERAPI_KEY:
        return "WeatherAPI.com API key not set."

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if "error" in data:
            return f"Could not fetch weather for {city}."
        condition = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        return f"According to WeatherAPI, it's {condition.lower()}, {temp}°C in {city}."
    except Exception as e:
        return f"Error fetching weather: {e}"

if __name__ == "__main__":
    server.run()