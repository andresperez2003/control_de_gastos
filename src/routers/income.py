from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.income import Income, get_all_incomes, get_income_by_id, remove_income, create_new_income

incomes=[
 { "id":1, "date":"2023-12-05", "description":"Ingreso de nomina por el mes trabajado", "value":500000,"category":1 }, 
 { "id":2, "date":"2023-20-09", "description":"Ingreso de nomina por el segundo trabajo", "value":600000,"category":1 }, 
 { "id":3, "date":"2024-05-12", "description":"Ingreso de contrato por obra labor", "value":400000,"category":2 }, 
 { "id":4, "date":"2024-05-24", "description":"Ingreso de parte del inquilino", "value":20000,"category":3 }, 
 { "id":5, "date":"2024-03-12", "description":"Mesada de padre mensual para universidad", "value":40000,"category":4 }, 
 { "id":6, "date":"2024-06-14", "description":"Mesada mensual para universidad", "value":60000,"category":4 }, 
]

income_router = APIRouter()

@income_router.get('/income',
  tags=['Incomes'],
  response_model=List[Income],    
  description="Return all incomes"   
)
def get_incomes():
  return get_all_incomes(incomes)

@income_router.get('/income/{id}',
  tags=['Incomes'],
  response_model=Income,    
  description="Return one income"   
)
def get_income(id: int)->Income:
  return get_income_by_id(id, incomes)

@income_router.post('/income',
 tags=['Incomes'],
 response_model=dict,
 description="Creates a new income")
def create_income(income: Income = Body()):
 return create_new_income(income, incomes)

@income_router.delete('/income/{id}',
 tags=['Incomes'],
 response_model=dict,
 description="Income removed sucessfull")
def delete_income(id: int = Path(ge=1)) -> dict:
  return remove_income(id,incomes)