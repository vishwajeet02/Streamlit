import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['Line_1','Line_2','Line_3'])
st.dataframe(chart_data)

st.header('1. Charts with Random Number')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.2 Bar Chart')
st.bar_chart(chart_data)

st.header('2. Visulaization with matplotlib & Seaborn')
st.subheader('2.1 Loading with DataFrame')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Grpah with Matplotlib')
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution plot with seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3. Multiple Graphs in one columns')
col1,col2 = st.columns(2)
with col1:
    col1.header('KDE = False')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],kde = False)
    st.pyplot(fig1)

with col2:
    col2.header('Hist = False')
    fig2 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],hist = False)
    st.pyplot(fig2)


st.header('4. Changing Style')
col1,col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(df['petal_length'],hist = False)
    st.pyplot(fig)

st.header('5. Exploring different Graphs')
st.subheader('5.1 Scatter Plots')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count Plots')
fig = plt.figure(figsize=(15,8))
sns.countplot(df,x='species')
st.pyplot(fig)

st.subheader('5.3 Box Plots')
fig = plt.figure(figsize=(15,8))
sns.boxplot(df,x='species',y='petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin Plots')
fig = plt.figure(figsize=(15,8))
sns.violinplot(df,x='species',y='petal_length')
st.pyplot(fig)