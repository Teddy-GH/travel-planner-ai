from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for every tool.
    """
    
    name: str
    description: str
    
    @abstractmethod
    async def execute(self, **kwargs) -> Any:
        """
        Execute the tool.
        
        Returns: Any
        """
        
        pass
        