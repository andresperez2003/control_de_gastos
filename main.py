

from fastapi import FastAPI, Body, Path
from typing import List



from src.routers.category import category_router
from src.routers.income import income_router
from src.routers.expense import expense_router
from src.routers.report import report_router
from src.middlwares.error_handler import ErrorHandler

tags_metadata = [{ "name": "Expenses", "description": "Expenses handling endpoints"},{ "name": "Incomes", "description": "Income handling endpoints"},{ "name": "Categories", "description": "Category handling endpoints"},{ "name": "Reports", "description": "Report handling endpoints"}]


app = FastAPI(openapi_tags=tags_metadata)
app.add_middleware(ErrorHandler)

app.title = "Product API"
app.summary = "Product REST API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.2"
app.contact = {
 "name": "Asdrubal Andres Perez Ascanio",
 "url": "https://www.linkedin.com/in/andres-perez-wb/",
 "email": "asdrubala.pereza@autonoma.edu.co",
} 

app.include_router(prefix="/categories", router=category_router)
app.include_router(prefix="/expenses", router=expense_router)
app.include_router(prefix="/reports", router=report_router)
app.include_router(prefix="/incomes", router=income_router)






















