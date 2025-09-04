##intergrate openai
import os
from constants import openai_key
from langchain.llns import OpenAI
import streamlit as st
os.enviro["OPENAI_API_KEY"] = openai_key
st.title('langchain demo with open ai')
input_text = st.text_input("search the topic you want ") 
##initalizehow much contol agent will ahve
llm =OpenAI(temperature =0.8)

if input_text:
    st.write(llm(input_text))
