import streamlit as st
import plotly.express as px

st.title("Weather Forecast fot the Next days")
place= st.text_input("Place: ")
days= st.slider("Forecast Days", min_value=1, max_value=5, help='select the number of forcasted days ' )
option =st.selectbox("Select data to view",
                     ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
def get_data(days):
    dates =["2025-25-10","2025-26-10","2025-27-10"]
    temperature = [10,12,11]
    temperature= [days * i for i in temperature]
    return dates, temperature

d, t = get_data(days)

figure = px.line(x=dates,y=temperature, labels={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(figure)