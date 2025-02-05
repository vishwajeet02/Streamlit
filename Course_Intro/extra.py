import streamlit as st
import datetime

st.title("Interactive Streamlit App 🚀")  # Main title

# ✅ Button Widget
if st.button('Click Me'):
    st.success("You clicked the button!")  # Displays success message when clicked

# ✅ Text Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")  # Greets the user when they enter a name

# ✅ Slider for numerical input
age = st.slider("Select your age:", 0, 100, 25)  # Default value = 25
st.write(f"You selected: {age}")

# ✅ Selectbox (Dropdown)
option = st.selectbox("Choose a language:", ["Python", "Java", "C++"])
st.write(f"You selected: {option}")

# ✅ Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")  # Displays message when checked

# ✅ Radio Buttons
gender = st.radio("Select Gender:", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")

# ✅ File Uploader
uploaded_file = st.file_uploader("Upload a file", type=["jpg", "png", "pdf"])
if uploaded_file is not None:
    st.success("File uploaded successfully!")  # Displays when a file is uploaded

# ✅ Date Picker
date = st.date_input("Pick a date", datetime.date.today())  # Default: Today
st.write(f"Selected date: {date}")

# ✅ Status Messages
st.success("Success Message!")  # Green success box
st.info("Information Message!")  # Blue info box
st.warning("Warning Message!")   # Orange warning box
st.error("Error Message!")       # Red error box

# ✅ Exception Handling
try:
    result = 1 / 0  # This will cause an error
except ZeroDivisionError as e:
    st.exception(e)  # Displays exception message in Streamlit

# ✅ Toast Notification (Temporary message)
st.toast('This is a temporary message!')

# ✅ Spinner (Loading simulation)
with st.spinner('Processing...'):
    import time
    time.sleep(2)
st.success('Done!')
