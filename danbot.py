# python -m streamlit run danbot.py

import streamlit as st
import random
import time

# Load wisdom quotes from the flat file
def load_wisdom(file_path):
    with open(file_path, 'r') as file:
        wisdom_list = file.readlines()
    return [quote.strip() for quote in wisdom_list]

# Function to get a random wisdom quote
def get_random_wisdom(wisdom_list):
    return random.choice(wisdom_list)

# Load wisdom quotes
wisdom_list = load_wisdom('wisdom.txt')

# Streamlit app layout
#st.sidebar.image("danbrain.png", width = 200)
#st.subheader("DanPilot")
st.image("danpilot.png")
st.sidebar.write("Remember - there's no Gain without Payne. \
         Harnessing the power of neural networks and mind downloading,  \
         AI is paving the way for the future. ")
#st.sidebar.image("arinet.png", width=100)


st.subheader('Daisy Daisy, give me your answer do..')
st.subheader('We hope you enjoyed this April 1st fun. Do check back next year for more experiments on SMT')


