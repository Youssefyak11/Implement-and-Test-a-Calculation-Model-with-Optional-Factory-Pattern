import pytest
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationType

def test_calculation_create_valid_add():
    calc = CalculationCreate(a=2, b=3, type=CalculationType.add)
    assert calc.a == 2
    assert calc.b == 3
    assert calc.type == CalculationType.add

def test_calculation_create_divide_by_zero_rejected():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type=CalculationType.divide)
