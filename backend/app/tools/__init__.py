from app.tools.registry import ToolRegistry

from app.tools.weather_tool import WeatherTool
from app.tools.currency_tool import CurrencyTool
from app.tools.hotel_tool import HotelTool


tool_registry = ToolRegistry()


tool_registry.register(
    WeatherTool()
)

tool_registry.register(
    CurrencyTool()
)

tool_registry.register(
    HotelTool()
)