from app.tools.base_tool import BaseTool


class HotelTool(BaseTool):
    
    name = "hotel"
    
    description = "Search hotels"
    
    
    async def execute(
        self,
        city: str,
    ):
        return [
            {
                "name": "Palm Resort",
                "price": 180,
            },
            {
                "name": "Dubai Grand",
                "price": 220,
            },
        ]