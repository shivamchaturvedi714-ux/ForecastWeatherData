import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for happiness")
x_option = st.selectbox("Select the data in the X-axis",
                        ("happiness", "gdp", "generosity"))
y_option = st.selectbox("Select the data in the Y-axis",
                        ("happiness", "gdp", "generosity"))

st.subheader(f"{x_option} and {y_option}")

df=pd.read_csv("happy.csv")

match x_option:
    case "happiness":
        x_array = df["happiness"]
    case "gdp":
        x_array = df["gdp"]
    case "generosity":
        x_array = df["generosity"]

match y_option:
    case "happiness":
        y_array = df["happiness"]
    case "gdp":
        y_array = df["gdp"]
    case "generosity":
        y_array = df["generosity"]

figure = px.scatter(x=x_array, y=y_array,
                 labels={'x':x_option, 'y':y_option})
st.plotly_chart(figure)
