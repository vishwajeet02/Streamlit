import streamlit as st
import pandas as pd

st.subheader('Uploading the CSV File')
df = st.file_uploader("Upload the CSV file:",type = ['csv','xlsx'])

# if df:
#     st.dataframe(df)

st.subheader('Loading the CSV File')
df = pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head())

st.subheader('Dealing with images')
#st.image('img.png')        #Directly
img_file = st.file_uploader('Upload the IMG file',type = ['png','jpeg']) #By Uploading
if img_file is not None:
    st.image('img.png')

st.subheader('Dealing with videos')
#Directly
st.video()
#Uploading





