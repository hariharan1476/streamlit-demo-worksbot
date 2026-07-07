import streamlit as st
import pandas as pd
import numpy as np
import time
st.title("Streamlit Demo Application")

st.header("Header Example")

st.subheader("Subheader Example")

st.text("This is simple text.")

st.write("Welcome to Streamlit")

st.success("Success Message")

st.info("Information Message")

st.warning("Warning Message")

st.error("Error Message")

st.markdown("### Markdown Example")

st.code("""
print("Hello Streamlit")
""")

agree = st.checkbox("I Agree")

if agree:
    st.write("Checkbox Selected")

gender = st.radio(
    "Select Gender",
    ["Male","Female"]
)

st.write("Selected:",gender)

course = st.selectbox(
    "Choose Department",
    ["AI&DS","CSE","ECE","EEE"]
)

st.write(course)

skills = st.multiselect(
    "Choose Skills",
    ["Python","Java","SQL","Machine Learning"]
)

st.write(skills)

age = st.slider(
    "Select Age",
    18,
    30
)

st.write(age)

marks = st.number_input(
    "Enter Marks"
)

st.write(marks)

name = st.text_input(
    "Enter Name"
)

st.write(name)

address = st.text_area(
    "Enter Address"
)

st.write(address)

date = st.date_input("Select Date")

st.write(date)

time_input = st.time_input("Select Time")

st.write(time_input)

if st.button("Click Me"):
    st.success("Button Clicked")

progress = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i+1)

with st.spinner("Loading..."):
    time.sleep(2)

st.success("Completed")

try:
    st.image("sample.png",width=300)
except:
    st.warning("Image not found")


df=pd.read_csv("sample.csv")

st.subheader("Student Data")

st.dataframe(df)

st.table(df)

st.json({
    "Name":"Hari",
    "Department":"AI&DS",
    "Marks":92
})
st.metric(
    label="Students",
    value=5
)

chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.line_chart(chart_data)

st.bar_chart(chart_data)

st.area_chart(chart_data)

st.sidebar.title("Sidebar")

choice=st.sidebar.selectbox(
    "Menu",
    ["Home","About","Contact"]
)

st.sidebar.write(choice)
uploaded=st.file_uploader("Upload File")

if uploaded:
    st.success("File Uploaded Successfully")