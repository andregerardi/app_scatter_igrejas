import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data(persist=None)
def load_dados():
    dados = pd.read_excel('igrejas.xlsx', usecols=['ano', 'numero', 'situação_cadastral_rec', 'RAZÃO SOCIAL', 'IDENTIFICADOR MATRIZ/FILIAL', 'NOME_MUNICIPIO', 'latitude_final', 'longitude_final'])
    dados = dados.reset_index(drop=True)
    dados = dados.sort_values(by=['ano'], ascending=True)
    emp_at_baixa = dados[dados['situação_cadastral_rec'].isin(['Ativa','Baixada'])]
    return dados, emp_at_baixa

@st.cache_data(persist=None)
def load_images():
    img1 = dict(source='https://cebrap.org.br/wp-content/uploads/2023/06/observatorio-religiao3-1536x400.png', xref="paper", yref="paper", x=1.0, y=1.00, sizex=0.4, sizey=0.4, xanchor="right", yanchor="bottom")
    img2 = dict(source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png", xref="paper", yref="paper", x=0.99, y=1.02, sizex=0.1, sizey=0.1, xanchor="right", yanchor="bottom")
    return img1, img2

def create_map_figure(data, img1, img2, map_type, size_column):
    fig = None
    if map_type == "density":
        fig = px.density_mapbox(data,
            width=1200, height=950,
            lat='latitude_final',
            lon='longitude_final',
            z='numero',
            radius=15 if size_column == 'numero' else 10,
            mapbox_style="carto-positron",
            center={"lat": -14.2350, "lon": -53.9253},
            zoom=3.5,
            opacity=0.6,
            animation_frame="ano" if map_type == "density" else "situação_cadastral_rec",
            hover_name='NOME_MUNICIPIO',
            hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL'],
            color_continuous_scale='Viridis')
    elif map_type == "scatter":
        fig = px.scatter_mapbox(emp_at_baixa ,
            width=1200, height=950,
            lat='latitude_final',
            lon='longitude_final',
            size=size_column,
            color_discrete_sequence=['#d62728'],
            hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL', 'ano'],
            hover_name='NOME_MUNICIPIO',
            animation_frame="situação_cadastral_rec",
            zoom=3.5,
            center={"lat": -14.2350, "lon": -53.9253},
            size_max=3,
            mapbox_style="carto-positron")

    fig.update_layout(coloraxis_showscale=False)
    fig.add_layout_image(img1)
    fig.add_layout_image(img2)
    
    return fig

# Titulo
st.markdown("""
<h4 style='text-align: center; color:#54595F;font-family:Segoe UI, sans-serif'><br></h4>
""", unsafe_allow_html=True)

# Esconder rodapé e outros elementos do Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Adicione um botão para carregar dados
dados, emp_at_baixa = load_dados()
img1, img2 = load_images()

# Centralizando o mapa
tab1, tab2, tab3, tab4 = st.tabs(["Density Map por ano", "Scatter Map por ano",
                                  "Density Map por situação cadastral", "Scatter Maps por situação cadastral"])

# Criar os mapas - parte I
with tab1:
    st.plotly_chart(create_map_figure(dados, img1, img2, "density", "numero"), use_container_width=True)
with tab2:
    st.plotly_chart(create_map_figure(dados, img1, img2, "scatter", "numero"), use_container_width=True)
with tab3:
    st.plotly_chart(create_map_figure(emp_at_baixa, img1, img2, "density", "numero"), use_container_width=True)
with tab4:
    st.plotly_chart(create_map_figure(emp_at_baixa, img1, img2, "scatter", "numero"), use_container_width=True)
