

from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

class Income (BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the income")
    date: str = Field(min_length=4, max_length=20, title="Name of the income")
    description: str = Field(min_length=4, max_length=100, title="Description of the income")
    value: int = Field(default=0, title="Value of the expense")


def get_all_incomes(list):
    return JSONResponse(content=list, status_code=200)

def get_income_by_id(id,list):
    for income in list:
        if income["id"] == id:
            return JSONResponse(content=income, status_code=200)
    return JSONResponse(content={"message":"Income not found"},status_code=404)

def remove_income(id,list):
    for income in list:
        if income["id"]==id:
            list.remove(income)
            return JSONResponse(content={"message": "Income was removed successfully" }, status_code=200)
        

def create_new_income(expense:Income, list):
    newIncome = expense.model_dump()

    #Validar que el usuario aun no ha sido creado (Esto se hace porque)
    for element in list:
        if newIncome['id'] == element['id']:
            return JSONResponse(content={
                   "message": "Income already exist"
                   }, status_code=400)
    list.append(newIncome)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newIncome
        }, status_code=201) 