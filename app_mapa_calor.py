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

# Criar o density_mapbox
fig = px.density_mapbox(dados,
                        width = 1200, height = 950,
                        lat='latitude_final',  # Substitua 'latitude' pelo nome da coluna que contém a latitude
                        lon='longitude_final',  # Substitua 'longitude' pelo nome da coluna que contém a longitude
                        z='numero',
                        radius=20,
                        mapbox_style="carto-positron",
                        center={"lat": -14.2350, "lon": -51.9253},
                        zoom=3.5,
                        opacity=0.6,
                        animation_frame="ano",
                        hover_name='NOME_MUNICIPIO',  # Use 'NM_MUN' como hover_name
                        hover_data=['situação_cadastral_rec','RAZÃO SOCIAL'],
                        color_continuous_scale='Viridis')  # Escolha uma escala de cores apropriada

# Adicionando o mapa ao contêiner
with container:
    st.plotly_chart(fig, use_container_width=True)
