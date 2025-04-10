import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="Mapa", layout="wide")

st.title("Ubicación de los Eventos Deportivos")

data = pd.read_csv("deporte_eventos.csv")

# Filtrar eventos por tipo con un selectbox
eventos_unicos = data['Evento'].unique()
evento_seleccionado = st.selectbox("Selecciona el tipo de evento", eventos_unicos)

# Filtrar datos por evento
data_filtrada = data[data['Evento'] == evento_seleccionado]

# Crear el mapa centrado en la media de las coordenadas
m = folium.Map(location=[data_filtrada["Latitud"].mean(), data_filtrada["Longitud"].mean()], zoom_start=6)

# Agrupar por departamento (o podrías usar cada fila individual si quieres más granularidad)
for idx, row in data_filtrada.iterrows():
    tooltip = f"{row['Departamento']}<br>Participantes: {row['Participantes']}<br>Duración: {row['Duración_Horas']} hrs"
    folium.Marker(
        location=[row['Latitud'], row['Longitud']],
        popup=tooltip,
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# Mostrar el mapa
st.subheader(f"Mapa de eventos: {evento_seleccionado}")
st_folium(m, width=700, height=500)
