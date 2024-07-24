import streamlit as st
import pandas as pd
import pickle


# carregando o modelo já treinado

with open ("modelo_treinado.pkl", "rb") as file:
    modelo = pickle.load(file)

def calcula_valor(metragem):
    dados = pd.DataFrame({'m2': [metragem]})
    valor = modelo.predict(dados)[0][0]
    return valor


st.set_page_config(
    page_title="Meu Projeto de ML",
    page_icon="🤖"

)

st.title("Prevendo valores de imóveis")
st.divider()

menu = st.sidebar
metragem = menu.number_input("Digite o tamanho do imóvel (m²):")
previsao = menu.button("Calcular valor do imóvel")

if previsao:
    if not metragem:
        st.write(metragem)
        st.error("O valor do imóvel não pode ser R$0", icon="❗")
    else:
        valor = calcula_valor(metragem)
        st.write(f"O valor do imóvel de {metragem:.2f} m² é de R${valor:,.2f}")
        st.success("Valor calculado com sucesso!", icon="✅")