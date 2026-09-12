from fastapi import FastAPI

app = FastAPI()

expenses = []

@app.get("/")
def home():
    return {"message": "Expense Tracker API"}

@app.get("/expenses")
def get_expenses():
    return expenses

@app.post("/expenses")
def add_expense(expense: dict):
    expenses.append(expense)
    return {"message": "Expense added", "expense": expense}