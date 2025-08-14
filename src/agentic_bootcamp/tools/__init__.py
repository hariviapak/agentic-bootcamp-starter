from .math_tool import math_eval, MathEvalInput
from .weather_tool import get_weather, WeatherInput
from .file_reader_tool import read_text_file, FileReadInput
from .unit_converter import unit_converter, UnitConverterInput

TOOLS = {
    "math_eval": {"fn": math_eval, "schema": MathEvalInput},
    "get_weather": {"fn": get_weather, "schema": WeatherInput},
    "read_text_file": {"fn": read_text_file, "schema": FileReadInput},
    "unit_converter": {"fn": unit_converter, "schema": UnitConverterInput},
}
