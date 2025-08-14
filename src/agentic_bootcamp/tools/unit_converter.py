from pydantic import BaseModel, Field

class UnitConverterInput(BaseModel):
    value: float = Field(..., description="The value to convert")
    from_unit: str = Field(..., description="The unit to convert from")
    to_unit: str = Field(..., description="The unit to convert to")

def unit_converter(x: UnitConverterInput) -> str:
    if x.from_unit == "km" and x.to_unit == "miles":
        return f"{x.value} km = {x.value * 0.621371:.2f} miles"
    return "Conversion not supported."