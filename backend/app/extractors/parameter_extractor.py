import re

from app.tools.base_tool import BaseTool


class ParameterExtractor:
    
    def __init__(self):
        
        self.cities = [
            "dubai",
            "tokyo",
            "paris",
            "london",
            "rome",
            "singapore",
            "addis ababa",
        ]
    
    def extract(
        self,
        tool: BaseTool,
        message: str,
    ) -> dict: 
        
        text = message.lower()
        
        for city in self.cities:
            
            if city in text:
                
                return {
                    "city": city.title()
                }
                
            return {
                "city": "Dubai"
            }
        
        # Currency tool (placeholder for now)
        if tool.name == "currency":
            
            return {
                "amount": 100,
                "from_currency": "USD",
                "to_currency": "AED",
            }
            
            
        return {}
    
   
                    
        
        