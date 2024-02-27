import streamlit as st
import openpyxl as xl
import subprocess
import time
import pandas as pd

#st.snow()
#st.title('hello')
#btn_1 = st.button('hello')
#st.slider('slider',0,100,50)

#st.sidebar.text_input('input')
#st.number_input('数値入力',min(0,0),max(0,100))
#st.file_uploader('ファイルを選んでください')
#st.color_picker('色を選んでください','#000000')
dt = pd.DataFrame({
    '1列' : [1,2,3,4],
    '2列' : [10,20,30,40]
})

#st.write(dt)

excel_1 = pd.read_excel(r"C:\Users\owner\Desktop\2024年02月現在　稼働時間.xlsm",sheet_name=0, header=2, usecols='B,C,D,H,AE')

excel_2 = excel_1[(excel_1['取引先'] == 'ｴｰｼﾝ工業') & (excel_1['機械名'] == '350A')]
excel_3 = excel_2.sort_values(by='時間N', ascending=True)

st.write(excel_3)
#print(excel_1)

if st.button('印刷'):
    cmd = r'soffice -p C:\Users\owner\Desktop\test_streamlit\test.xlsx'
    subprocess.run(cmd, cwd=r'C:\Program Files\LibreOffice\program' ,shell=True)
 
    with st.spinner('処理中'):
        print('印刷完了')
        time.sleep(4)

if 'increment' not in st.session_state: # 初期化
    st.session_state['increment'] = 0

if st.button('count'):
    st.session_state["increment"] += 1
    print(st.session_state["increment"])
    a = st.session_state["increment"]
    wb = xl.load_workbook(r"C:\Users\owner\Desktop\test_streamlit\test.xlsx")
    ws = wb.worksheets[0]
    st.write("count",st.session_state["increment"])
    ws['A1'].value = st.session_state['increment']
    wb.save(r"C:\Users\owner\Desktop\test_streamlit\test" + str(a) + ".xlsx")