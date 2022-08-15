import streamlit as st
import pandas as pd

@st.cache
def read_excel(path, sheetnumber):
    return pd.read_excel(path, sheetnumber)


#upload file from hd
st.text('enter "0" loads the sheet1')
sheetnumber = st.text_input('Sheet number', '0')
uploaded_file = st.file_uploader("Choose an excel file")
if uploaded_file is not None:
  dataframe = read_excel(uploaded_file, sheetnumber)
  # st.write(dataframe)


#Create three columns/filters
col1, col2, col3 = st.columns(3)

with col1:
    period_list=dataframe["SIM"].unique().tolist()
    period_list.sort(reverse=True)
    year_month = st.selectbox("SIM", period_list, index=0)





#Data prepartion to only retrieve fields that are relevent to this project
sheet_df = read_excel(uploaded_file, sheet)