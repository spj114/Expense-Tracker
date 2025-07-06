import streamlit as st
import requests 
import pandas as pd

API_URL = 'http://localhost:8000'

def monthly_analytics_tab():
    
    response = requests.get(f"{API_URL}/analytics_by_month")
    response = response.json()

    monthly_analytics_df = pd.DataFrame(response)

    st.title("Expense Breakdown by Month")
    st.bar_chart(data=monthly_analytics_df.set_index("month")["total_expenses"], use_container_width=True)

    monthly_analytics_df['total_expenses'] = monthly_analytics_df['total_expenses'].map("{:.1f}".format)

    st.table(monthly_analytics_df)
    # st.write(response)