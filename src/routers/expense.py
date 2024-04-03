from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.expense import Expense, get_all_expenses, get_expense_by_id, remove_expense, create_new_expense


expense_router = APIRouter()


expenses=[
  { "id":1, "date":"2023-10-08", "description":"Gasto para el mercado mensual", "value":30000,"category":5 }, 
 { "id":2, "date":"2024-06-11", "description":"Gasto del transporte mensual para la universidad", "value":80000,"category":6 }, 
 { "id":3, "date":"2024-02-20", "description":"Gasto de fines de semana", "value":90000,"category":7 }, 
 { "id":4, "date":"2024-09-12", "description":"Adquisición de nuevo libro", "value":20000,"category":8 }, 
  { "id":5, "date":"2024-10-22", "description":"Adquisición de libro", "value":40000,"category":8 }, 
]


@expense_router.get('/expense',
  tags=['Expenses'],
  response_model=List[Expense],    
  description="Return all expenses"   
)
def get_expenses():
  return get_all_expenses(expenses)

@expense_router.get('/expense/{id}',
  tags=['Expenses'],
  response_model=Expense,    
  description="Return one expense"   
)
def get_expense(id: int)->Expense:
  return get_expense_by_id(id, expenses)

@expense_router.post('/expense',
 tags=['Expenses'],
 response_model=dict,
 description="Creates a new expense")
def create_expense(expense: Expense = Body()):
 return create_new_expense(expense, expenses)

@expense_router.delete('/expense/{id}',
 tags=['Expenses'],
 response_model=dict,
 description="Expense removed sucessfull")
def delete_expense(id: int = Path(ge=1)) -> dict:
  return remove_expense(id,expenses)