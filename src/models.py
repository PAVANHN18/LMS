from sqlalchemy import Column, Integer, String, Date
from .db import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String)
    joining_date = Column(Date)
    leave_balance = Column(Integer, default=20)
