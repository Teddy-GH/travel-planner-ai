from app.tools.base_tool import BaseTool


class CurrencyTool(BaseTool):
    
    name = "currency"
    
    description = "Convert currencies"
    
    
    async def execute(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
        ):
        
        return {
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "converted": amount * 55,
        }
    
    
    