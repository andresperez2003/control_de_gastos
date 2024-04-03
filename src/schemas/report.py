from fastapi.responses import JSONResponse

def general_report(listExpense, ListIncome):
    totalExpense = 0
    totalIncome = 0
    for expense in listExpense:
        totalExpense +=expense["value"]
    for income in ListIncome:
        totalIncome+= income["value"]
    subs = totalIncome-totalExpense
    return JSONResponse(content={
        "General report":{
        "Income": "$" + str(totalIncome),
        "Expense": "$" + str(totalExpense),
        "Substraction": "$" + str(subs)
        }

        },
    status_code=200)


def expanded_report(listCategories, listExpense, listIncome):
    diccionary = {category["id"]: [] for category in listCategories}

    for category, valor in diccionary.items():
        for expense in listExpense:
            if category == expense["category"]:
                addExpense = {"expense": expense}
                valor.append(addExpense)
        for income in listIncome:
            if category == income["category"]:
                addIncome = {"income": income}
                valor.append(addIncome)

    report = change_id_categories(listCategories, diccionary)
    return JSONResponse(content={
        "Expanded report":report
        },
    status_code=200)


def change_id_categories(categories, diccionary):
    newDict = {}
    # diccionario que mapee los id de las categorías a sus nombres
    category_id_to_name = {category["id"]: category["name"] for category in categories}


    for key, value in diccionary.items():
        #Aqui esta cogiendo el valor de category_id_to_name y lo esta poniendo como llave en el nuevo diccionario y le asigna el valor que tenia antes
        newDict[category_id_to_name[key]] = value
    return newDict