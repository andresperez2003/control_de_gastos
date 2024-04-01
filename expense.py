
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

class Expense (BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the expense")
    name: str = Field(min_length=4, max_length=50, title="Name of the expense")
    description: str = Field(min_length=4, max_length=100, title="Description of the expense")
    value: int = Field(default=0, title="Value of the expense")


def get_all_expenses(list):
    return JSONResponse(content=list, status_code=200)

def get_expense_by_id(id,list):
    for expense in list:
        if expense["id"] == id:
            return JSONResponse(content=expense, status_code=200)
    return JSONResponse(content={"message":"Expense not found"},status_code=404)

def remove_expense(id,list):
    for expense in list:
        if expense["id"]==id:
            list.remove(expense)
            return JSONResponse(content={"message": "Expense was removed successfully" }, status_code=200)
        

def create_new_expense(expense:Expense, list):
    newExpense = expense.model_dump()

    #Validar que el usuario aun no ha sido creado (Esto se hace porque)
    for element in list:
        if newExpense['id'] == element['id']:
            return JSONResponse(content={
                   "message": "Expense already exist"
                   }, status_code=400)
    list.append(newExpense)
    return JSONResponse(content={
        "message": "Expense was created successfully",
        "data": newExpense
        }, status_code=201) 