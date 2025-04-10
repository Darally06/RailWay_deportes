import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Descriptivo de variables")

data = pd.read_csv("deporte_eventos.csv")

col1, col2 = st.columns(2)

with col1:
    # Histograma para la variable 'Participantes'
    st.subheader("Distribución de Participantes")
    fig1 = px.histogram(data, x="Participantes", nbins=20, color_discrete_sequence=['#c7522a'])
    fig1.update_traces(marker_line_color='white', marker_line_width=1)
    fig1.update_layout(title="Histograma de Participantes",
                    xaxis_title="Número de Participantes",
                    yaxis_title="Frecuencia")
    st.plotly_chart(fig1, use_container_width=True)

    # Histograma para la variable 'Duración_Horas'
    st.subheader("Distribución de Duración en Horas")
    fig2 = px.histogram(data, x="Duración_Horas", nbins=20, color_discrete_sequence=['#e5c185'])
    fig2.update_traces(marker_line_color='white', marker_line_width=1)
    fig2.update_layout(title="Histograma de Duración en Horas",
                    xaxis_title="Duración (Horas)",
                    yaxis_title="Frecuencia")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    # Gráfico de barras para la variable 'Evento'
    st.subheader("Frecuencia de Eventos")
    event_counts = data['Evento'].value_counts().reset_index()
    event_counts.columns = ['Evento', 'Frecuencia']

    fig3 = px.bar(event_counts, x='Evento', y='Frecuencia', color_discrete_sequence=['#74a892'])
    fig3.update_layout(title="Eventos",
                    xaxis_title="Evento",
                    yaxis_title="Frecuencia",
                    xaxis_tickangle=45)
    st.plotly_chart(fig3, use_container_width=True)

    # 
    st.subheader("Eventos por Departamento")
    eventos_departamento = data["Departamento"].value_counts().reset_index()
    eventos_departamento.columns = ["Departamento", "Frecuencia"]
    fig = px.bar(eventos_departamento, 
                x="Frecuencia", 
                y="Departamento", 
                orientation='h',
                color_discrete_sequence=['#008585'])
    fig.update_layout(yaxis=dict(categoryorder='total ascending'))
    st.plotly_chart(fig, use_container_width=True)