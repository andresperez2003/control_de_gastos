

from fastapi import FastAPI, Body, Path
from typing import List
from expense import Expense, get_all_expenses, get_expense_by_id, remove_expense, create_new_expense
from income import Income, get_all_incomes, get_income_by_id, remove_income, create_new_income
from category import Category, get_all_category, get_cateogory_by_id, create_new_category, remove_category
from reports import general_report, expanded_report


tags_metadata = [{ "name": "Expenses", "description": "Expenses handling endpoints"},{ "name": "Incomes", "description": "Income handling endpoints"},{ "name": "Categories", "description": "Category handling endpoints"},{ "name": "Reports", "description": "Report handling endpoints"}]


app = FastAPI(openapi_tags=tags_metadata)


categories=[
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
 { "id":1, "date":"2023-12-05", "description":"Ingreso de nomina por el mes trabajado", "value":500000,"category":1 }, 
 { "id":2, "date":"2023-20-09", "description":"Ingreso de nomina por el segundo trabajo", "value":600000,"category":1 }, 
 { "id":3, "date":"2024-05-12", "description":"Ingreso de contrato por obra labor", "value":400000,"category":2 }, 
 { "id":4, "date":"2024-05-24", "description":"Ingreso de parte del inquilino", "value":20000,"category":3 }, 
 { "id":5, "date":"2024-03-12", "description":"Mesada de padre mensual para universidad", "value":40000,"category":4 }, 
 { "id":6, "date":"2024-06-14", "description":"Mesada mensual para universidad", "value":60000,"category":4 }, 
]

expenses=[
  { "id":1, "date":"2023-10-08", "description":"Gasto para el mercado mensual", "value":30000,"category":5 }, 
 { "id":2, "date":"2024-06-11", "description":"Gasto del transporte mensual para la universidad", "value":80000,"category":6 }, 
 { "id":3, "date":"2024-02-20", "description":"Gasto de fines de semana", "value":90000,"category":7 }, 
 { "id":4, "date":"2024-09-12", "description":"Adquisición de nuevo libro", "value":20000,"category":8 }, 
  { "id":5, "date":"2024-10-22", "description":"Adquisición de libro", "value":40000,"category":8 }, 
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



@app.get('/category',
  tags=['Categories'],
  response_model=List[Income],    
  description="Return all categories"   
)
def get_categories():
  return get_all_category(categories)

@app.get('/category/{id}',
  tags=['Categories'],
  response_model=Expense,    
  description="Return one category"   
)
def get_category(id: int)->Income:
  return get_cateogory_by_id(id, categories)

@app.post('/category',
 tags=['Categories'],
 response_model=dict,
 description="Creates a new category")
def create_category(category: Category = Body()):
 return create_new_category(category, categories)

@app.delete('/category/{id}',
 tags=['Categories'],
 response_model=dict,
 description="Category removed sucessfull")
def delete_category(id: int = Path(ge=1)) -> dict:
  return remove_category(id,categories)


@app.get('/general_report',
  tags=['Reports'],    
  description="Return general report"   
)
def get_general_report():
  return general_report(expenses,incomes)


@app.get('/expanded_report',
  tags=['Reports'],   
  description="Return expanded report"   
)
def get_expanded_report():
  return expanded_report(categories,expenses, incomes)







