import streamlit as st
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

def factorial(x):
    return math.factorial(int(x))

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Streamlit UI Design
st.set_page_config(page_title=" Calculator", page_icon="🧮", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #f8f9fa;
        }
        .calculator-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='calculator-container'><h2>Calculator 🧮</h2></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Operations")
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide", "Power"], key='basic')
    num1 = st.number_input("Enter first number", step=0.01, key='num1')
    num2 = st.number_input("Enter second number", step=0.01, key='num2')
    if st.button("Calculate Basic", key='basic_calc'):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        st.success(f"Result: {result}")

with col2:
    st.subheader("Advanced Operations")
    adv_operation = st.selectbox("Select advanced operation:", ["Square Root", "Logarithm", "Factorial", "Sine", "Cosine", "Tangent"], key='advanced')
    if adv_operation in ["Square Root", "Logarithm", "Factorial"]:
        num = st.number_input("Enter number", step=0.01, key='adv_num')
        if adv_operation == "Logarithm":
            base = st.number_input("Enter base", step=0.01, value=10.0, key='log_base')
    else:
        num = st.number_input("Enter angle in degrees", step=0.01, key='angle')
    if st.button("Calculate Advanced", key='adv_calc'):
        if adv_operation == "Square Root":
            result = square_root(num)
        elif adv_operation == "Logarithm":
            result = logarithm(num, base)
        elif adv_operation == "Factorial":
            result = factorial(num)
        elif adv_operation == "Sine":
            result = sine(num)
        elif adv_operation == "Cosine":
            result = cosine(num)
        elif adv_operation == "Tangent":
            result = tangent(num)
        st.success(f"Result: {result}")