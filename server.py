from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel
from datetime import date
import db_helper



class Expense(BaseModel):
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model= List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)

    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)

    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message" : "Expenses Updated Successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data : List[Dict[str, Any]] = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date) # type: ignore
    if data is None:
        raise HTTPException(status_code=500, detail = 'Failed to retrieve expense summary from the database.')
    
    all_cat_total = sum([row['total'] for row in data])  

    breakdown = {}

    for row in data:
        percentage = (row['total']/all_cat_total) * 100 if all_cat_total != 0 else 0
        breakdown[row["category"]] = { 
            'total' : row["total"], 
            'percentage' : percentage
        }

    return breakdown

@app.get("/analytics_by_month/")
def get_analytics_by_month():
    data : List[Dict[str, Any]]  = db_helper.fetch_analytics_by_month() # type: ignore
    if data is None:
        raise HTTPException(status_code=500, detail = 'Failed to retrieve expense summary from the database.')

    return data