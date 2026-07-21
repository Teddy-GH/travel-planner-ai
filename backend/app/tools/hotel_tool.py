from app.tools.base_tool import BaseTool


class HotelTool(BaseTool):
    
    name = "hotel"
    
    description = "Search hotels"
    
    parameters = {
        "city": str,
    }
    
    
    async def execute(
        self,
        city: str,
    ):
        return [
            {
                "name": "Palm Resort",
                "price": 180,
                "city": city,
            },
            {
                "name": "Dubai Grand",
                "price": 220,
                "city": city,
            },
        ]