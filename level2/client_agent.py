import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

async def main():
    # Use StdioTransport to spawn the weather_mcp.py server
    transport = StdioTransport("python level2/weather_mcp.py")
    client = Client(transport)

    await client.start()

    # Call the weather tool
    result = await client.call_tool("get_weather", {"city": "Hyderabad"})
    print("Weather Result:", result)

    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
