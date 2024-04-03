
from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.report import general_report, expanded_report

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
expenses=[
  { "id":1, "date":"2023-10-08", "description":"Gasto para el mercado mensual", "value":30000,"category":5 }, 
 { "id":2, "date":"2024-06-11", "description":"Gasto del transporte mensual para la universidad", "value":80000,"category":6 }, 
 { "id":3, "date":"2024-02-20", "description":"Gasto de fines de semana", "value":90000,"category":7 }, 
 { "id":4, "date":"2024-09-12", "description":"Adquisición de nuevo libro", "value":20000,"category":8 }, 
  { "id":5, "date":"2024-10-22", "description":"Adquisición de libro", "value":40000,"category":8 }, 
]
incomes=[
 { "id":1, "date":"2023-12-05", "description":"Ingreso de nomina por el mes trabajado", "value":500000,"category":1 }, 
 { "id":2, "date":"2023-20-09", "description":"Ingreso de nomina por el segundo trabajo", "value":600000,"category":1 }, 
 { "id":3, "date":"2024-05-12", "description":"Ingreso de contrato por obra labor", "value":400000,"category":2 }, 
 { "id":4, "date":"2024-05-24", "description":"Ingreso de parte del inquilino", "value":20000,"category":3 }, 
 { "id":5, "date":"2024-03-12", "description":"Mesada de padre mensual para universidad", "value":40000,"category":4 }, 
 { "id":6, "date":"2024-06-14", "description":"Mesada mensual para universidad", "value":60000,"category":4 }, 
]

report_router = APIRouter()





@report_router.get('/general_report',
  tags=['Reports'],    
  description="Return general report"   
)
def get_general_report():
  return general_report(expenses,incomes)


@report_router.get('/expanded_report',
  tags=['Reports'],   
  description="Return expanded report"   
)
def get_expanded_report():
  return expanded_report(categories,expenses, incomes)
