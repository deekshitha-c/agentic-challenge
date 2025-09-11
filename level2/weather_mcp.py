import os
import httpx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Weather MCP Server")

# You can get a free API key from https://www.weatherapi.com/
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "8df3a7ad5688406dbde173946251109")
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.
    
    Args:
        city: Name of the city to get weather for
        
    Returns:
        Current weather conditions and temperature
    """
    
    # If no API key is set, return mock data
    if WEATHER_API_KEY == "8df3a7ad5688406dbde173946251109":
        # Mock data for testing
        mock_data = {
            "hyderabad": "Cloudy with light rain, 27°C",
            "mumbai": "Sunny, 32°C",
            "delhi": "Hazy, 35°C",
            "bangalore": "Partly cloudy, 25°C"
        }
        return mock_data.get(city.lower(), f"Sunny, 30°C in {city}")
    
    # Make actual API call
    try:
        async with httpx.AsyncClient() as client:
            params = {
                "key": WEATHER_API_KEY,
                "q": city,
                "aqi": "no"
            }
            response = await client.get(WEATHER_API_URL, params=params)
            
            if response.status_code == 200:
                data = response.json()
                condition = data["current"]["condition"]["text"]
                temp_c = data["current"]["temp_c"]
                humidity = data["current"]["humidity"]
                feels_like = data["current"]["feelslike_c"]
                
                return f"{condition}, {temp_c}°C (feels like {feels_like}°C), Humidity: {humidity}%"
            else:
                return f"Could not fetch weather for {city}"
                
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

if __name__ == "__main__":
    # Run the MCP server
    # By default, it will run on stdio
    mcp.run()