
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

class Category (BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the income")
    name: str = Field(min_length=4, max_length=50, title="Name of the income")
    description: str = Field(min_length=4, max_length=100, title="Description of the income")


def get_all_cateogyr(list):
    return JSONResponse(content=list, status_code=200)

def get_cateogory_by_id(id,list):
    for category in list:
        if category["id"] == id:
            return JSONResponse(content=category, status_code=200)
    return JSONResponse(content={"message":"Category not found"},status_code=404)

def remove_category(id,list):
    for category in list:
        if category["id"]==id:
            list.remove(category)
            return JSONResponse(content={"message": "Category was removed successfully" }, status_code=200)
        

def create_new_category(category:Category, list):
    newCategory = category.model_dump()

    #Validar que el usuario aun no ha sido creado (Esto se hace porque)
    for element in list:
        if newCategory['id'] == element['id']:
            return JSONResponse(content={
                   "message": "Income already exist"
                   }, status_code=400)
    list.append(newCategory)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newCategory
        }, status_code=201) 