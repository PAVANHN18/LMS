from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import db, models, schemas, crud

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

@app.post("/employees/")
def add_employee(employee: schemas.EmployeeCreate, database: Session = Depends(db.get_db)):
    return crud.add_employee(database, employee)

@app.get("/employees/{emp_id}/leave-balance")
def get_leave_balance(emp_id: int, database: Session = Depends(db.get_db)):
    return crud.get_leave_balance(database, emp_id)
