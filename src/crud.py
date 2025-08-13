from sqlalchemy.orm import Session
from . import models, schemas

def add_employee(db: Session, emp: schemas.EmployeeCreate):
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_leave_balance(db: Session, emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        return {"error": "Employee not found"}
    return {"employee": emp.name, "leave_balance": emp.leave_balance}
