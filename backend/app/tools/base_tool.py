from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for every tool.
    
    Every tool must define:
    - name
    - description
    - parameters
    - execute()
    """
    
    name: str
    
    description: str
    
    # Metadata describing the expected inputs
    parameters: dict[str, type]
    
    @abstractmethod
    async def execute(self, **kwargs) -> Any:
        """
        Execute the tool.
        
        Returns: Any
        """
        
        raise NotImplementedError
        