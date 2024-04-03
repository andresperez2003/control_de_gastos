from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.category import Category, get_all_category, get_cateogory_by_id, create_new_category, remove_category

category_router = APIRouter()


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



@category_router.get('/category',
  tags=['Categories'],
  response_model=List[Category],    
  description="Return all categories"   
)
def get_categories():
  return get_all_category(categories)

@category_router.get('/category/{id}',
  tags=['Categories'],
  response_model=Category,    
  description="Return one category"   
)
def get_category(id: int)->Category:
  return get_cateogory_by_id(id, categories)

@category_router.post('/category',
 tags=['Categories'],
 response_model=dict,
 description="Creates a new category")
def create_category(category: Category = Body()):
 return create_new_category(category, categories)

@category_router.delete('/category/{id}',
 tags=['Categories'],
 response_model=dict,
 description="Category removed sucessfull")
def delete_category(id: int = Path(ge=1)) -> dict:
  return remove_category(id,categories)




