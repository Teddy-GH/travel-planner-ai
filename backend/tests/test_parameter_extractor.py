from app.extractors.parameter_extractor import ParameterExtractor
from app.tools.weather_tool import WeatherTool

extractor = ParameterExtractor()
weather_tool = WeatherTool()

params = extractor.extract(
    weather_tool,
    "What's the weather in Tokyo?"
)

print(params)