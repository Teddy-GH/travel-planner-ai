from app.tools.base_tool import BaseTool


class WeatherTool(BaseTool):
    
    name = "weather"
    
    description = "Get weather information"
    
    parameters = {
        "city": str
    }
    
    
    async def execute(
        self, 
        city: str,
        ):
        
        # Mock implementation
        return {
            "city": city,
            "temperature": 35,
            "condition": "Sunny",
            "humidity": 48,
        }