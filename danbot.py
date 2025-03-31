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
st.sidebar.image("danbrain.png", width = 200)
#st.subheader("DanPilot")
st.image("danpilot.png")
st.sidebar.write("Remember - there's no Gain without Payne. \
         Harnessing the power of neural networks and mind downloading,  \
         AI is paving the way for the future. ")
#st.sidebar.image("arinet.png", width=100)

# Set the text you want to display
text = "> initialising system...."

# Use HTML to style the text
st.markdown(f"<p style='font-family:Courier New;'>{text}</p>", unsafe_allow_html=True)

st.write("Ask me anything:")

# User input
user_input = st.text_input("You:", "")
#st.image("animated_neurons.gif")

# Display a random wisdom quote when user inputs text
# Submit button
if st.button("Submit"):
#if user_input:    
    if user_input:
        with st.spinner(text="a symphony of neurons firing...."):
            time.sleep(4)    
        wisdom_quote = get_random_wisdom(wisdom_list)
        st.header("ARINet-DanBot:")
        st.subheader(f"{wisdom_quote}")
        time.sleep(10)
        st.subheader('but wait....')
        time.sleep(4)
        st.subheader("there's more....")
        time.sleep(5)
        st.subheader('APRIL FOOLS')
        time.sleep(5)
        st.write("We haven't really wired up Dan to a Neural Network (Yet). But we are developing exciting new \
                 ways of interacting with our data and insights including chat. \
                 Do Check out the data and analytics centre on sharepoint for more info.")
st.divider()
st.image("neurons2.gif")
