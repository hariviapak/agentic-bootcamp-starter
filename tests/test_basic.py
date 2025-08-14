from src.agentic_bootcamp.tools.math_tool import math_eval, MathEvalInput

def test_math_eval():
    assert math_eval(MathEvalInput(expression="2+2")) == "4"
