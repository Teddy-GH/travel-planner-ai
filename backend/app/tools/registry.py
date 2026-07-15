from app.tools.base_tool import BaseTool



class ToolRegistry:
    
    def __init__(self):
        
        self.tools: dict[str, BaseTool] = {}
        
    def register(
        self,
        tool: BaseTool
    ): 
        
        self.tools[tool.name] = tool
        
    def get(
        self,
        name: str,
    ) -> BaseTool | None:
        
        return self.tools.get(name)
    
    def all(self):
        
        return list(self.tools.values())        