from app.tools import tool_registry


async def get_tools():
    tool = tool_registry.get("weather")

    result = await tool.execute(
        city="Dubai"
    )

    print(result)
    
    return result