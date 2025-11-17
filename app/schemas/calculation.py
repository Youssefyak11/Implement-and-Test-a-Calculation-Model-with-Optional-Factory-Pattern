from enum import Enum
from pydantic import BaseModel, field_validator, model_validator
from pydantic import ConfigDict  # optional, to avoid the warning


class CalculationType(str, Enum):
    add = "Add"
    sub = "Sub"
    multiply = "Multiply"
    divide = "Divide"


class CalculationBase(BaseModel):
    a: float
    b: float
    type: CalculationType


class CalculationCreate(CalculationBase):
    @model_validator(mode="after")
    def non_zero_for_division(self):
        if self.type == CalculationType.divide and self.b == 0:
            raise ValueError("Divisor (b) cannot be zero for division.")
        return self


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: CalculationType
    result: float | None = None

    model_config = ConfigDict(from_attributes=True)
    # if you don't care about the warning, you can keep:
    # class Config:
    #     from_attributes = True
