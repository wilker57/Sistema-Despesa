import streamlit as st
import pandas as pd
from models import add_compra_diversa, get_compras_diversas, update_compra_diversa, delete_compra_diversa

st.title("💳 Compras Diversas")

data = st.date_input("Data")
descricao = st.text_input("Descrição")
valor_total = st.number_input("Valor Total", min_value=0.0, format="%.2f")
valor_wilker = st.number_input("Wilker", min_value=0.0, format="%.2f")
valor_neimara = st.number_input("Neimara", min_value=0.0, format="%.2f")

if st.button("Adicionar"):
    if valor_wilker + valor_neimara == valor_total:
        add_compra_diversa(data, descricao, valor_total, valor_wilker, valor_neimara)
        st.success("Compra adicionada com sucesso!")
    else:
        st.error("Os valores não conferem.")

st.subheader("📋 Compras Diversas Registradas")
df = pd.DataFrame(get_compras_diversas(), columns=["ID", "Data", "Descrição", "Total", "Pessoa1", "Pessoa2"])
st.dataframe(df)

id_to_edit = st.number_input("ID para Editar", min_value=0)
if st.button("Editar"):
    update_compra_diversa(id_to_edit, data, descricao, valor_total, valor_wilker, valor_neimara)
    st.success("Compra atualizada!")

id_to_delete = st.number_input("ID para Excluir", min_value=0)
if st.button("Excluir"):
    delete_compra_diversa(id_to_delete)
    st.success("Compra excluída!")