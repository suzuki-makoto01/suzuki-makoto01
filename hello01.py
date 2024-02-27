import streamlit as st
import pandas as pd
import openpyxl
import xlrd

#print(pd.__version__)
wb = pd.read_excel(r"C:\Users\owner\Desktop\test_streamlit\test.xlsx")
print(wb)

'''
with st.form('form', clear_on_submit=False):
    name = st.write('OK')
    st.selectbox('box',('1','2','3','4'))
'''    
