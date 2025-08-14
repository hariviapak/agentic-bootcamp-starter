from pydantic import BaseModel, Field

class MathEvalInput(BaseModel):
    expression: str = Field(..., description="A valid Python arithmetic expression, e.g., '2+2*5'")

def math_eval(x: MathEvalInput) -> str:
    # Safe eval subset (only digits and operators). In production, swap for a proper math parser.
    allowed = set("0123456789+-*/(). %")
    if not set(x.expression) <= allowed:
        raise ValueError("Invalid characters in expression.")
    try:
        result = eval(x.expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Math error: {e}"
