from pydantic import BaseModel, Field

class WeatherInput(BaseModel):
    city: str = Field(..., description="City name to get a mock weather for")

def get_weather(x: WeatherInput) -> str:
    # Mocked weather. In Week 2, replace with a real API call.
    return f"Weather in {x.city}: 31°C, clear sky (mock)."
