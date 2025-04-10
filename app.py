import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="App con Mapas", layout="wide")

with st.sidebar:
    selected = option_menu("Menú", ["Inicio", "Mapa", "Dashboard"],
        icons=["house", "geo-alt", "bar-chart"], menu_icon="cast", default_index=0)
if selected == "Inicio":
    st.title("Eventos Deportivos")
    st.markdown("Reporte de eventos deportivos en Colombia")
    
elif selected == "Dashboard":
    st.switch_page("pages/Dashboar.py")

elif selected == "Mapa":
    st.switch_page("pages/Mapa.py")