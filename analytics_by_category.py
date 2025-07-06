import streamlit as st
from datetime import datetime
import requests
from pandas import DataFrame

API_URL = 'http://localhost:8000'

def categorical_analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start Date', datetime(2024,8,1))
    with col2:
        end_date = st.date_input('End Date', datetime(2024,8,5))

    if st.button("Get Analytics"):
        pay_load = {
                        'start_date' : start_date.strftime('%Y-%m-%d'),
                        'end_date' : end_date.strftime('%Y-%m-%d')
                   }

        response = requests.post(f"{API_URL}/analytics",json = pay_load)
        response = response.json()

        data = {
            "Category" : list(response.keys()),
            "Total" : [response[element]["total"] for element in response],
            "Percentage" : [round(response[element]['percentage'],2) for element in response]
        }

        analytics_df = DataFrame(data)
        df_sorted = analytics_df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown by Category")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"], use_container_width = True)

        df_sorted['Total'] = df_sorted['Total'].map("{:.1f}".format)
        df_sorted['Percentage'] = df_sorted['Percentage'].map("{:.2f}".format)

        st.table(df_sorted)
        # st.write(response)