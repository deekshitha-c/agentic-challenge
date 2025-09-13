import os
import httpx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Weather MCP Server")

# Weather API setup (use env var, fallback to mock mode)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.
    If no API key is provided, returns mock weather data.
    """

    # --- MOCK MODE ---
    if not WEATHER_API_KEY:
        mock_data = {
            "hyderabad": "Cloudy with light rain, 27°C",
            "mumbai": "Sunny, 32°C",
            "delhi": "Hazy, 35°C",
            "bangalore": "Partly cloudy, 25°C"
        }
        return mock_data.get(city.lower(), f"Sunny, 30°C in {city}")

    # --- REAL API MODE ---
    try:
        async with httpx.AsyncClient() as client:
            params = {"key": WEATHER_API_KEY, "q": city, "aqi": "no"}
            response = await client.get(WEATHER_API_URL, params=params)

            if response.status_code == 200:
                data = response.json()
                condition = data["current"]["condition"]["text"]
                temp_c = data["current"]["temp_c"]
                feels_like = data["current"]["feelslike_c"]
                humidity = data["current"]["humidity"]
                return f"{condition}, {temp_c}°C (feels like {feels_like}°C), Humidity: {humidity}%"
            else:
                return f"Could not fetch weather for {city} (status {response.status_code})"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"

if __name__ == "__main__":
    # Run MCP server on stdio
    mcp.run()
