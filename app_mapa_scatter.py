# Importar bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Importar os dados
@st.cache(allow_output_mutation=True, persist=True)
def load_dados():
    # Seu código para carregar os dados
    dados = pd.read_excel('igrejas.xlsx')[['ano', 'numero', 'situação_cadastral_rec', 'RAZÃO SOCIAL', 'IDENTIFICADOR MATRIZ/FILIAL', 'NOME_MUNICIPIO', 'latitude_final', 'longitude_final']]
    # drop index
    dados = dados.reset_index(drop=True)
    # sort
    dados = dados.sort_values(by=['ano'], ascending=True)
    # return dados
    return dados

# Chama função
dados = load_dados()

##Titulo
st.markdown("""
<br>
<h4 style='text-align: center; color:#54595F;font-family:Segoe UI, sans-serif'>Presença de templos segundo situação cadastral e ano</h4>
""", unsafe_allow_html=True)
st.markdown("---")

##retira o made streamlit no fim da página##
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Centralizando o mapa
fig = px.scatter_mapbox(dados,
                        width=1100, height=950,
                        lat='latitude_final',
                        lon='longitude_final',
                        size='numero',
                        color_discrete_sequence=['#d62728'],
                        hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL'],
                        hover_name='NOME_MUNICIPIO',
                        animation_frame="ano",
                        zoom=3.5,
                        center={"lat": -14.2350, "lon": -51.9253},
                        size_max=3,
                        mapbox_style="open-street-map")

# Exibir o mapa no Streamlit
st.plotly_chart(fig, use_container_width=True)


