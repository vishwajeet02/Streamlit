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
# st.markdown('## Hi')
# st.markdown('### Hi')
# st.markdown('#### Hi')
# st.markdown('##### Hi')
st.markdown('Hi')
st.markdown("**Bold Text**")
st.markdown("_Italic Text_")
st.markdown("***Bold & Italic***")
st.markdown("- Item 1\n- Item 2\n- Item 3")  # Bullets
st.markdown("1. First\n2. Second\n3. Third")  # Numbered list
st.markdown("[Visit GeeksforGeeks](https://www.geeksforgeeks.org)")
#st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg)")

st.success('Success !')                 # Success
st.info('Information !')                    # Info
st.warning('Warning !')                     # Warning
st.error('Error !')                         # Error
st.exception(ZeroDivisionError('Div not possible'))           #Exception
#st.toast('This is a temporary message!')
# with st.spinner('Loading...'):              #Loading
#     import time
#     time.sleep(3)
# st.success('Done!')


st.subheader('HELP')
st.help(ZeroDivisionError)
#st.help(ValueError)

st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)
st.write("# Heading 1")
st.write("## Heading 2")
st.write("**Bold Text** and _Italic Text_")
st.write("[Google](https://www.google.com)")  # Displays a hyperlink

st.subheader('CODE')
st.code('x=10\nfor i in range(x):\n\tprint(i)')  #Code

st.subheader('Checkbox:')               #Checkbox
st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write('You are an adult')

st.subheader('Radio Button')                #RadioButton
st.radio('Select: ',('Check','Uncheck'))
button = st.radio('Gender: ',('Male','Female','Other'))
if(button == 'Male'):
    st.write('You are Male')
elif(button == 'Female'):
    st.write('You are Female')
else:
    st.write('You are Others')    


st.subheader('Select Box')                     #SelectBox
SelectBox = st.selectbox("Data Science :",['Data Analayis','Web Scrapping',
                                        'Machine learning','Deep learngin',
                                        'NLP','Stats','Computer Vision'])
st.write("You have selected",SelectBox)

st.subheader('MultiSelect Box')                     #MultiSelectBox
MultiSelBox = st.multiselect("Data Science :",['Data Analayis','Web Scrapping',
                                        'Machine learning','Deep learngin',
                                        'NLP','Stats','Computer Vision'])
st.write("You have selected: ",len(MultiSelBox),"Courses")

st.subheader("BUTTON")                          #Button
if(st.button('BClick me')):
    st.write('Thanks for clicking me')

st.subheader('Slider')                          # SLider
volume = st.slider('Select the Volume',1,100,step=1)
st.write('Volume is: ',volume)

st.subheader('Text Input')                      #Text Input
username = st.text_input('Name : ')
password = st.text_input('Pass : ',type = 'password')

st.subheader('Text Area')                       #Text area
textarea = st.text_area('Write about yourself in 20 words:',max_chars = 20)
st.write(textarea)


st.subheader("Input Number")                           # Input-Number
st.number_input('Select your age',18,110)

st.subheader("Input Date")                              # Input-Date
st.date_input('Date')

st.subheader("Input Time")                              # Input-Time
st.time_input('Time')





