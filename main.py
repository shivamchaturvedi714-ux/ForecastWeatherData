import streamlit as st
import plotly.express as px
from backend import get_data

#Add title ,text input ,slider,selectbox and subheading
st.title("Weather Forecast fot the Next days")
place= st.text_input("Place: ")
days= st.slider("Forecast Days", min_value=1, max_value=5, help='select the number of forcasted days ' )
option =st.selectbox("Select data to view",
                     ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data= get_data(place, days)
        temperature1=[]
        if option == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperature1= [temperature/10 for temperature in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Create a temperature plot
            figure = px.line(x=dates,y=temperature1, labels={'x':'Date','y':'Temperature (C)'})
            st.plotly_chart(figure)

        if option == "Sky":
            images ={"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                     "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths =[images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths,width=100)
    except KeyError:
        st.error("Please enter a valid place")



