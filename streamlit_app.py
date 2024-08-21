import streamlit as st
from openai import OpenAI
import pickle 
st.title("Hello this is my first app")
CYLINDERS=st.number_input("CYLINDERS",min_value=0,max_value=10,value=1)
FUELCONSUMPTION_CITY=st.number_input("FUELCONSUMPTION_CITY",min_value=0,max_value=10,value=1)
engine_size=st.number_input("engine_size",min_value=0,max_value=10,value=1)
with open('model.pkl','rb') as file:
  model=pickle.load(file)
output=model.predict([[CYLINDERS,FUELCONSUMPTION_CITY,engine_size]])
st.write('co2 of car is : ',output[0][0])
