from app.tools.base_tool import BaseTool


class WeatherTool(BaseTool):
    
    name = "weather"
    
    description = "Get weather information"
    
    
    async def execute(
        self, 
        city: str,
        ):
        
        return {
            "city": city,
            "temperature": 37,
            "condition": "Sunny",
        }