import pytest
from app.schemas.calculation import CalculationType
from app.services.calculations import (
    CalculationFactory,
    AddOperation,
    SubOperation,
    MultiplyOperation,
    DivideOperation,
)

def test_factory_returns_correct_strategies():
    assert isinstance(CalculationFactory.get_strategy(CalculationType.add), AddOperation)
    assert isinstance(CalculationFactory.get_strategy(CalculationType.sub), SubOperation)
    assert isinstance(CalculationFactory.get_strategy(CalculationType.multiply), MultiplyOperation)
    assert isinstance(CalculationFactory.get_strategy(CalculationType.divide), DivideOperation)

def test_factory_invalid_type_raises():
    with pytest.raises(ValueError):
        CalculationFactory.get_strategy("BadType")  # type: ignore[arg-type]
