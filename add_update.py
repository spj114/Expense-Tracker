import streamlit as st
from datetime import datetime
import requests

API_URL = 'http://localhost:8000'

def add_update_tab():
    expense_date = st.date_input('Date:', datetime(2024,8,1), label_visibility="visible")
    response = requests.get(f"{API_URL}/expenses/{expense_date}")
    if response.status_code == 200:
        exsisting_expenses = response.json()
        # st.write(exsisting_expenses)
    else:
        st.error("Failed to Retrieve Expenses")
        exsisting_expenses = []
    
    categories = ["Rent", "Shopping", "Food", "Entertainment", "Other"]
    with st.form(key='expese_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text('Amount')
        with col2:
            st.text('Category')
        with col3:
            st.text('Note')
        
        expenses = []

        for i in range(10):

            if i < len(exsisting_expenses):
                amount = exsisting_expenses[i]['amount']
                category = exsisting_expenses[i]['category']
                note = exsisting_expenses[i]['notes']
            else:
                amount = 0.0
                category = categories[1]
                note = ''
            
            with col1:
                amount_input = st.number_input(label='Amount', min_value=0.0, step=1.0, value = amount, key=f'amount_{i}', label_visibility = "collapsed")
            with col2:
                category_input = st.selectbox(label='Category', options = categories, index = categories.index(category) , key = f"category_{i}", label_visibility = "collapsed")
            with col3:
                notes_input = st.text_input(label='Notes', value = note , key=f'notes_{i}', label_visibility = "collapsed")

            expenses.append({
                'amount' : amount_input,
                'category' : category_input,
                'notes' : notes_input
                            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            requests.post(f'{API_URL}/expenses/{expense_date}', json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expense updated successfully!")
            else:
                st.error("Failed to update expense!")