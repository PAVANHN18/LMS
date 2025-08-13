from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    joining_date: date
