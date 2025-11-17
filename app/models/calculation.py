from sqlalchemy import Column, Integer, Float, String
from app.db import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String(20), nullable=False)
    result = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Calculation id={self.id} type={self.type} a={self.a} b={self.b} result={self.result}>"
