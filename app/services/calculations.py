from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationType

class CalculationStrategy(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        ...

class AddOperation(CalculationStrategy):
    def compute(self, a: float, b: float) -> float:
        return a + b

class SubOperation(CalculationStrategy):
    def compute(self, a: float, b: float) -> float:
        return a - b

class MultiplyOperation(CalculationStrategy):
    def compute(self, a: float, b: float) -> float:
        return a * b

class DivideOperation(CalculationStrategy):
    def compute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

class CalculationFactory:
    @staticmethod
    def get_strategy(calc_type: CalculationType):
        if calc_type == CalculationType.add:
            return AddOperation()
        if calc_type == CalculationType.sub:
            return SubOperation()
        if calc_type == CalculationType.multiply:
            return MultiplyOperation()
        if calc_type == CalculationType.divide:
            return DivideOperation()
        raise ValueError(f"Unsupported calculation type: {calc_type}")

def create_calculation(db: Session, calc_in: CalculationCreate):
    strategy = CalculationFactory.get_strategy(calc_in.type)
    result = strategy.compute(calc_in.a, calc_in.b)

    db_calc = Calculation(
        a=calc_in.a,
        b=calc_in.b,
        type=calc_in.type.value,
        result=result,
    )
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc
