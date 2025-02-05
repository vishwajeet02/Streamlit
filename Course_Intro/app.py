import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Title  ->  Hello Geeks, Welcome to Geeks for Geeks')   #Title
st.header('Header  ->  Geeks for Geeks')      #Header
st.subheader('Subheader  ->  Geeks for Geeks')      #SubHeader
st.text('Text  ->  Geeks for Geeks')                #Text

# Markdown
st.markdown('# Hi')             
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

st.success('Success !')                 # Success
st.info('Information !')                    # Info
st.warning('Warning !')                     # Warning
st.error('Error !')                         # Error
st.exception(ZeroDivisionError('Div not possible'))           #Exception

st.subheader('HELP')
st.help(ZeroDivisionError)
st.help(ValueError)

st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)
st.write(3*3)
st.write("# Heading 1")
st.write("## Heading 2")
st.write("**Bold Text** and _Italic Text_")
st.write("[Google](https://www.google.com)")  # Displays a hyperlink


data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

st.write(df)  # Automatically renders as a table


x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.write(fig)  # Displays the Matplotlib chart