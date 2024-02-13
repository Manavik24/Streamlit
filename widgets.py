import streamlit as st
import time as t

st.checkbox("Login checkbox")
st.button("Click")
st.radio("Pick your gender",["Male","Female"])
st.selectbox("Choose the deptartment",["Content","Sales","Marketing"])
st.multiselect("Pick your language(s)",["Hindi","English","Marathi"])
st.select_slider("Rating",["Bad","Good","Excelent","Outstanding"])
st.slider("Rating",0,5)

st.number_input("Pick a number",10,20)
st.text_input("Enter your name")
st.date_input("Opening ceremnony")
st.time_input("What time is it?")

st.text_area("Welcome to the my text area")
st.file_uploader("Upload file")
st.color_picker("Color")
st.progress(55)
with st.spinner("Generating"):
    t.sleep(2)
st.balloons()

st.sidebar.title("Hey,I am a sidebar!")
st.sidebar.text_input("Enter name")
