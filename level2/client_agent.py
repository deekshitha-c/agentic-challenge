# client_agent.py
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    """Main client function that connects to the MCP server and uses tools."""
    
    # Create connection to the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["weather_mcp.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            print()
            
            # Interactive loop
            print("Weather Agent Ready! Ask me about weather in any city.")
            print("Type 'quit' to exit.\n")
            
            while True:
                # Get user input
                user_input = input("You: ").strip()
                
                if user_input.lower() == 'quit':
                    break
                
                # Simple parsing to extract city name
                city = extract_city(user_input)
                
                if city:
                    # Call the weather tool
                    result = await session.call_tool(
                        "get_weather",
                        arguments={"city": city}
                    )
                    
                    # Process and display the result
                    if result.content:
                        weather_info = result.content[0].text
                        print(f"\nAgent: According to the weather API, in {city} it's {weather_info}\n")
                    else:
                        print(f"\nAgent: I couldn't get weather information for {city}.\n")
                else:
                    print("\nAgent: Please mention a city name to get weather information.\n")

def extract_city(text: str) -> str:
    """Extract city name from user input."""
    
    # Common weather question patterns
    patterns = [
        "weather in ",
        "raining in ",
        "temperature in ",
        "how's the weather in ",
        "what's the weather in ",
        "is it raining in ",
        "is it sunny in ",
        "how hot is it in ",
        "how cold is it in "
    ]
    
    text_lower = text.lower()
    
    for pattern in patterns:
        if pattern in text_lower:
            # Extract the city name after the pattern
            start = text_lower.index(pattern) + len(pattern)
            # Take the rest of the string and clean it
            city = text[start:].strip()
            # Remove common ending words
            city = city.replace("?", "").replace("today", "").replace("now", "").strip()
            return city
    
    # If no pattern matched, look for capitalized words (likely city names)
    words = text.split()
    for word in words:
        if word[0].isupper() and word.lower() not in ['is', 'it', 'what', 'how', 'the']:
            return word
    
    return ""

if __name__ == "__main__":
    asyncio.run(main())