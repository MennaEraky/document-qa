import streamlit as st
from openai import OpenAI
st.title("Hello this is my first app")
st.number_input("CYLINDERS",min_value=0,max_value=10,value=1)
st.number_input("FUELCONSUMPTION_CITY",min_value=0,max_value=10,value=1)
st.number_input("engine_size",min_value=0,max_value=10,value=1)
