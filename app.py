import streamlit as st
from add_update import add_update_tab
from analytics_by_category import categorical_analytics_tab
from analytics_by_month import monthly_analytics_tab


st.title("Expense Tracking System")  

tab1, tab2, tab3 = st.tabs(['Add/Update', 'Analytics By Category', 'Analytics By Month'])

with tab1:
    add_update_tab()
with tab2:
    categorical_analytics_tab()
with tab3:
    monthly_analytics_tab()