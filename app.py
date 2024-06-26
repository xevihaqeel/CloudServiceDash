import streamlit as st
import pandas as pd
import plotly.express as pe


car_data = pd.read_csv('vehicles_us.csv')
st.header('Car Ad Data Study')
#adding a slider to filter data based on price
max_price = int(car_data['price'].max())
min_price = int(car_data['price'].min())
price_filter = st.slider('Select a price range', min_price, max_price, (min_price, max_price))

filtered_data = car_data[(car_data['price'] >= price_filter[0]) & (car_data['price'] <= price_filter[1])]

if st.checkbox('Show Histogram'):
    price_hist = pe.histogram(filtered_data, x='price')
    price_hist.update_layout(title_text='Price Distribution', xaxis_title='Price', yaxis_title='Count')
    st.plotly_chart(price_hist)

if st.checkbox('Show Scatterplot'):
    year_price  = pe.scatter(filtered_data, x="model_year", y="price")
    year_price.update_layout(title_text='Year vs. Price', xaxis_title='Model Year', yaxis_title='Price')
    st.plotly_chart(year_price)

    
if st.checkbox('Exclude Expensive Vehicles'):
    expensive_threshold = st.slider('Select a price threshold to exclude expensive vehicles', min_price, max_price, max_price)
    filtered_data = filtered_data[filtered_data['price'] < expensive_threshold]    