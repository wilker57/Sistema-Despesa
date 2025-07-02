import streamlit as st
import pandas as pd
from database import create_tables
from models import get_compras_diversas, get_compras_parceladas


create_tables()

st.set_page_config(page_title="Dashboard - Gerenciador de Despesas", layout="wide")
st.title("Dashboard")


# Dashboard: mesmo conteúdo do arquivo da página de Dashboard
diversas = pd.DataFrame(get_compras_diversas(), columns=["ID", "Data", "Descrição", "Total", "Wilker", "Neimara"])
parceladas = pd.DataFrame(get_compras_parceladas(), columns=["ID", "Data", "Descrição", "Total", "Total Parcelas", "Pagas", "Restantes", "Wilker", "Neimara"])

st.subheader("Compras Diversas")
st.write(f"Total Wilker: R$ {diversas['Wilker'].sum():.2f}")
st.write(f"Total Neimara: R$ {diversas['Neimara'].sum():.2f}")

st.subheader("Compras Parceladas")
st.write(f"Total Wilker: R$ {parceladas['Wilker'].sum():.2f}")
st.write(f"Total Neimara: R$ {parceladas['Neimara'].sum():.2f}")

st.bar_chart({
    "Wilker": [diversas['Wilker'].sum(), parceladas['Wilker'].sum()],
    "Neimara": [diversas['Neimara'].sum(), parceladas['Neimara'].sum()],
})

st.sidebar.success("Use o menu lateral para navegar pelas funcionalidades.")
