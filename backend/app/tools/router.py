from app.tools import tool_registry


class ToolRouter:
    
    def route(
        self,
        message: str,
    ):
        
        
        text = message.lower()
        
        if "weather" in text:
            return tool_registry.get("weather")
        
        if "hotel" in text:
            return tool_registry.get("hotel")
        
        if "currency" in text:
            return tool_registry.get("currency")
        
        return None