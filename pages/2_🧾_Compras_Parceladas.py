import streamlit as st
import pandas as pd
from models import add_compra_parcelada, get_compras_parceladas, update_compra_parcelada, delete_compra_parcelada

st.title("🧾 Compras Parceladas")

data = st.date_input("Data")
descricao = st.text_input("Descrição")
valor_total = st.number_input("Valor Total", min_value=0.0, format="%.2f")
total_parcelas = st.number_input("Total Parcelas", min_value=1)
parcelas_pagas = st.number_input("Parcelas Pagas", min_value=0)
parcelas_restantes = total_parcelas - parcelas_pagas
st.write(f"Parcelas Restantes: {parcelas_restantes}")

valor_wilker = st.number_input("Wilker", min_value=0.0, format="%.2f")
valor_neimara = st.number_input("Neimara", min_value=0.0, format="%.2f")

if st.button("Adicionar"):
    if valor_wilker + valor_neimara == valor_total:
        add_compra_parcelada(data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_wilker, valor_neimara)
        st.success("Compra parcelada adicionada!")
    else:
        st.error("Os valores não conferem.")

st.subheader("📋 Compras Parceladas Registradas")
df = pd.DataFrame(get_compras_parceladas(), columns=["ID", "Data", "Descrição", "Total", "Total Parcelas", "Pagas", "Restantes", "Pessoa1", "Pessoa2"])
st.dataframe(df)

id_to_edit = st.number_input("ID para Editar", min_value=0, key="edit_parcelada")
if st.button("Editar", key="editar_parcelada"):
    update_compra_parcelada(id_to_edit, data, descricao, valor_total, total_parcelas, parcelas_pagas, parcelas_restantes, valor_wilker, valor_neimara)
    st.success("Compra atualizada!")

id_to_delete = st.number_input("ID para Excluir", min_value=0, key="delete_parcelada")
if st.button("Excluir", key="excluir_parcelada"):
    delete_compra_parcelada(id_to_delete)
    st.success("Compra excluída!")