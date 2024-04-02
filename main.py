

from fastapi import FastAPI, Body, Path
from typing import List
from expense import Expense, get_all_expenses, get_expense_by_id, remove_expense, create_new_expense
from income import Income, get_all_incomes, get_income_by_id, remove_income, create_new_income

tags_metadata = [{ "name": "Expenses", "description": "Expenses handling endpoints"},{ "name": "Incomes", "description": "Income handling endpoints"}]


app = FastAPI(openapi_tags=tags_metadata)


categorias=[
 { "id":1, "name":"nomina", "description":"" },
 { "id":2, "name":"págo contrato", "description":"" },
 { "id":3, "name":"pago arriendo", "description":"" },
 { "id":4, "name":"mesada", "description":"" },
 { "id":5, "name":"alimentación", "description":"" },
 { "id":6, "name":"transporte", "description":"" },
 { "id":7, "name":"ocio", "description":"" },
 { "id":8, "name":"libros", "description":"" },
]

incomes=[
 { "id":1, "date":"2023-12-05", "description":"Ingreso de nomina por el mes trabajado", "value":"50000","category":1 }, 
 { "id":2, "date":"2024-05-12", "description":"Ingreso de contrato por obra labor", "value":"40000","category":2 }, 
 { "id":3, "date":"2024-05-24", "description":"Ingreso de parte del inquilino", "value":"20000","category":3 }, 
 { "id":4, "date":"2024-03-12", "description":"Mesada mensual para universidad", "value":"40000","category":4 }, 
]

expenses=[
  { "id":1, "date":"2023-10-08", "description":"Gasto para el mercado mensual", "value":"30000","category":5 }, 
 { "id":2, "date":"2024-06-11", "description":"Gasto del transporte mensual para la universidad", "value":"80000","category":6 }, 
 { "id":3, "date":"2024-02-20", "description":"Gasto de fines de semana", "value":"90000","category":7 }, 
 { "id":4, "date":"2024-09-12", "description":"Adquisición de nuevo libro", "value":"20000","category":8 }, 
]


@app.get('/expense',
  tags=['Expenses'],
  response_model=List[Expense],    
  description="Return all expenses"   
)
def get_expenses():
  return get_all_expenses(expenses)

@app.get('/expense/{id}',
  tags=['Expenses'],
  response_model=Expense,    
  description="Return one expense"   
)
def get_expense(id: int)->Expense:
  return get_expense_by_id(id, expenses)

@app.post('/expense',
 tags=['Expenses'],
 response_model=dict,
 description="Creates a new expense")
def create_expense(expense: Expense = Body()):
 return create_new_expense(expense, expenses)

@app.delete('/expense/{id}',
 tags=['Expenses'],
 response_model=dict,
 description="Expense removed sucessfull")
def delete_expense(id: int = Path(ge=1)) -> dict:
  return remove_expense(id,expenses)



@app.get('/income',
  tags=['Incomes'],
  response_model=List[Income],    
  description="Return all incomes"   
)
def get_incomes():
  return get_all_incomes(incomes)

@app.get('/income/{id}',
  tags=['Incomes'],
  response_model=Expense,    
  description="Return one income"   
)
def get_income(id: int)->Income:
  return get_income_by_id(id, incomes)

@app.post('/income',
 tags=['Incomes'],
 response_model=dict,
 description="Creates a new income")
def create_income(income: Income = Body()):
 return create_new_income(income, incomes)

@app.delete('/income/{id}',
 tags=['Incomes'],
 response_model=dict,
 description="Income removed sucessfull")
def delete_income(id: int = Path(ge=1)) -> dict:
  return remove_income(id,incomes)













