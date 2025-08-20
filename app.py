import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(
    'C:/Users/quiqu/Desktop/Data_Analyst/Proyecto_sprint7/sprint_7_proyect/vehicles_us.csv')  # cargar datos

st.header('Análisis de modelos de vehículos desde 1908 hasta 2019')

# Boton para construir histograma
hist_check = st.checkbox('Construir histograma')

if hist_check:
    st.write('Construyendo histograma...')  # Boton en acción
    fig = px.histogram(car_data, x='odometer',
                       title='Histograma de Odometro')  # crea histograma
    st.plotly_chart(fig, use_container_width=True)  # muestra histograma
    st.write('Histograma construido con éxito!')  # Mensaje de éxito


# Boton para construir gráfico de dispersión
scatter_check = st.checkbox('Construir gráfico de dispersión')

if scatter_check:
    st.write('Construyendo gráfico de dispersión...')  # Boton en acción
    fig_2 = px.scatter(car_data, x='odometer', y='price',
                       title='Gráfico de dispersión de odómetro vs precio')  # crea gráfico de dispersión
    # muestra gráfico de dispersión
    st.plotly_chart(fig_2, use_container_width=True)
    st.write('Gráfico de dispersión construido con éxito!')  # Mensaje de éxito

# Boton para construir gráfico de pastel
pie_check = st.checkbox('Construir gráfico de pastel')

if pie_check:
    st.write('Construyendo gráfico de pastel...')  # Boton en acción
    # crea gráfico de pastel
    fig_3 = px.pie(car_data, names='type',
                   title='Gráfico de pastel de tipos de vehículo')
    # muestra gráfico de pastel
    st.plotly_chart(fig_3, use_container_width=True)
    st.write('Gráfico de pastel construido con éxito!')  # Mensaje de éxito

bubble_check = st.checkbox('Contruir gráfico de burbujas')

if bubble_check:
    bubble_chart = px.scatter(car_data, x='odometer',
                              y='price', size='price', color='type')
    # Muestra el gráfico de burbujas
    st.plotly_chart(bubble_chart, use_container_width=True)

# ahora haremos un comparador de histogramas para los modelos
Histogram_compare = st.checkbox('Comparar histogramas')

if Histogram_compare:
    st.write('Selecciona los modelos para comparar histogramas')  # Instrucciones
    first_hist = st.selectbox(
        "Selecciona el primer modelo", car_data['model'].unique())
    st.write("Modelo seleccionado número 1", first_hist)
    second_hist = st.selectbox(
        "Selecciona el segundo modelo", car_data['model'].unique())
    st.write("Modelo seleccionado número 2", second_hist)

    car_data_filtrado = car_data[(car_data['model'] == first_hist) | (car_data['model'] == second_hist)
                                 ]  # Filtramos los datos seleccionados para usar comom base para los histogramas

    histogram_compare = px.histogram(
        car_data_filtrado, x='odometer', color='model', barmode='overlay')
    # Mostramos el histograma
    st.plotly_chart(histogram_compare, use_container_width=True)
