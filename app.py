import streamlit as st
import pandas as pd
import plotly_express as px

vehicles_df = pd.read_csv('C:/Users/angel/OneDrive/Desktop/vehicles_us.csv')
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

fig = px.histogram(vehicles_df, x="odometer")

st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión')

fig = px.scatter(vehicles_df, x="odometer", y="price", title="Scatter plot of Odometer vs Price")

st.plotly_chart(fig, use_container_width=True)

