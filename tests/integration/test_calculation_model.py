from sqlalchemy.orm import Session
from app.schemas.calculation import CalculationCreate, CalculationType
from app.services.calculations import create_calculation
from app.models.calculation import Calculation

def test_create_calculation_persists(db_session: Session):
    calc_in = CalculationCreate(a=10, b=5, type=CalculationType.divide)
    calc = create_calculation(db_session, calc_in)

    assert isinstance(calc.id, int)
    assert calc.result == 2

    stored = db_session.query(Calculation).filter_by(id=calc.id).first()
    assert stored is not None
    assert stored.result == 2
