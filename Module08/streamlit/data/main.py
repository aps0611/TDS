import streamlit as st
import pandas as pd

header = st.container()
userInput = st.container()
output = st.container()

with header:
	st.title('Welcome to my awesome Streamlit Project!')
	st.subheader('USECASE: Substraction of two given numbers')


with userInput:
	st.subheader('Please enter the input')
	st.text('The output is a - b')
	num1 = st.number_input(label="Enter a",step=1.,format="%.2f")
	num2 = st.number_input(label="Enter b",step=1.,format="%.2f")


def sub(num1,num2):
	ans = num1 - num2
	return ans

ans = sub(num1,num2)

with output:
	st.subheader('Please see the output below  :')
	st.markdown(f'Answer is {ans}')



