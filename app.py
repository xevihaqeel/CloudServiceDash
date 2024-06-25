import streamlit as st
import pandas as pd
import plotly.express as pe


car_data = pd.read_csv('vehicles_us.csv')
st.header('Car Ad Data Study')

if st.checkbox('Show Histogram'):
    price_hist = pe.histogram(car_data, x='price',title="Price Distribution")
    st.plotly_chart(price_hist)

if st.checkbox('Show Scatterplot'):
    year_price  = pe.scatter(car_data, x="model_year", y="price", title="Year vs. Price")
    st.plotly_chart(year_price)