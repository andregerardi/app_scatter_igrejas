# Importar bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
import numpy as np

# Importar os dados
dados = pd.read_excel(r'igrejas.xlsx')

# sort data
dados = dados.sort_values(by=['ano'], ascending=True)

# select columns
dados = dados[['ano','numero','situação_cadastral_rec','RAZÃO SOCIAL',
               'IDENTIFICADOR MATRIZ/FILIAL','NOME_MUNICIPIO',
               'latitude_final','longitude_final']]

# drop index
dados = dados.reset_index(drop=True)

# Criar dot map
fig = px.scatter_mapbox(dados,
                        title='Presença de templos segundo situação cadastral e ano',
                        width=1100, height=950,
                        lat='latitude_final',
                        lon='longitude_final',
                        size='numero',
                        color_discrete_sequence=['#d62728'],
                        hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL'],
                        hover_name='NOME_MUNICIPIO',
                        animation_frame="ano",
                        zoom=3.5,
                        center={"lat": -14.2350, "lon": -47.9253},
                        size_max=3,
                        mapbox_style="open-street-map")

# Exibir o mapa no Streamlit
st.plotly_chart(fig)
