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
    ## base empresa ativa e baixada
    emp_at_baixa = dados[dados['situação_cadastral_rec'].isin(['Ativa','Baixada'])]
    # return dados
    return dados, emp_at_baixa

# Chama função
dados, emp_at_baixa = load_dados()


##Titulo - Presença de espaços de culto por ano e situação cadastral
st.markdown("""
<h4 style='text-align: center; color:#54595F;font-family:Segoe UI, sans-serif'><br></h4>
""", unsafe_allow_html=True)

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
tab1, tab2, tab3, tab4 = st.tabs(["Density Map por ano", "Scatter Map por ano",
                                 "Density Map por situação cadastral", "Scatter Maps por situação cadastral"])


# Criar o density_mapbox by year
fig = px.density_mapbox(dados,
                    width = 1200, height = 950,
                    lat='latitude_final',  # Substitua 'latitude' pelo nome da coluna que contém a latitude
                    lon='longitude_final',  # Substitua 'longitude' pelo nome da coluna que contém a longitude
                    z='numero',
                    radius=15,
                    mapbox_style="carto-positron",
                    center={"lat": -14.2350, "lon": -53.9253},
                    zoom=3.5,
                    opacity=0.6,
                    animation_frame="ano",
                    hover_name='NOME_MUNICIPIO',  # Use 'NM_MUN' como hover_name
                    hover_data=['situação_cadastral_rec','RAZÃO SOCIAL'],
                    color_continuous_scale='Viridis')  # Escolha uma escala de cores apropriada
# Remove a legenda de cores
fig.update_layout(coloraxis_showscale=False)

# Add image
fig.add_layout_image(
dict(
    source='https://cebrap.org.br/wp-content/uploads/2023/06/observatorio-religiao3-1536x400.png',
    xref="paper", yref="paper",
    x=1.0, y=.99,
    sizex=0.4, sizey=0.4,
    xanchor="right", yanchor="bottom"
 )
)

# Add image
fig.add_layout_image(
dict(
    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
    xref="paper", yref="paper",
    x=0.99, y=1.03,
    sizex=0.1, sizey=0.1,
    xanchor="right", yanchor="bottom"
 )
)

# Criar o scatter_mapbox by year
fig2 = px.scatter_mapbox(dados,
                    width=1200, height=950,
                    lat='latitude_final',
                    lon='longitude_final',
                    size='numero',
                    color_discrete_sequence=['#d62728'],
                    hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL'],
                    hover_name='NOME_MUNICIPIO',
                    animation_frame="ano",
                    zoom=3.5,
                    center={"lat": -14.2350, "lon": -53.9253},
                    size_max=3,
                    mapbox_style="carto-positron")
# Add image
fig2.add_layout_image(
dict(
    source='https://cebrap.org.br/wp-content/uploads/2023/06/observatorio-religiao3-1536x400.png',
    xref="paper", yref="paper",
    x=1.0, y=1.00,
    sizex=0.4, sizey=0.4,
    xanchor="right", yanchor="bottom"
 )
)

# Add image
fig2.add_layout_image(
dict(
    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
    xref="paper", yref="paper",
    x=0.99, y=1.03,
    sizex=0.1, sizey=0.1,
    xanchor="right", yanchor="bottom"
 )
)

# Criar o density_mapbox geral
fig3 = px.density_mapbox(emp_at_baixa,
                    width = 1200, height = 950,
                    lat='latitude_final',  # Substitua 'latitude' pelo nome da coluna que contém a latitude
                    lon='longitude_final',  # Substitua 'longitude' pelo nome da coluna que contém a longitude
                    z='numero',
                    radius=10,
                    mapbox_style="carto-positron",
                    center={"lat": -14.2350, "lon": -53.9253},
                    zoom=3.5,
                    opacity=0.6,
                    animation_frame="situação_cadastral_rec",
                    hover_name='NOME_MUNICIPIO',  # Use 'NM_MUN' como hover_name
                    hover_data=['situação_cadastral_rec','RAZÃO SOCIAL'],
                    color_continuous_scale='Viridis')  # Escolha uma escala de cores apropriada
# Remove a legenda de cores
fig3.update_layout(coloraxis_showscale=False)

# Add image
fig3.add_layout_image(
dict(
    source='https://cebrap.org.br/wp-content/uploads/2023/06/observatorio-religiao3-1536x400.png',
    xref="paper", yref="paper",
    x=1.0, y=1.00,
    sizex=0.4, sizey=0.4,
    xanchor="right", yanchor="bottom"
 )
)

# Add image
fig3.add_layout_image(
dict(
    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
    xref="paper", yref="paper",
    x=0.99, y=1.03,
    sizex=0.1, sizey=0.1,
    xanchor="right", yanchor="bottom"
 )
)

# Criar o scatter_mapbox
fig4 = px.scatter_mapbox(emp_at_baixa,
                    width=1200, height=950,
                    lat='latitude_final',
                    lon='longitude_final',
                    size='numero',
                    color_discrete_sequence=['#d62728'],
                    hover_data=['situação_cadastral_rec', 'RAZÃO SOCIAL', 'ano'],
                    hover_name='NOME_MUNICIPIO',
                    animation_frame="situação_cadastral_rec",
                    zoom=3.5,
                    center={"lat": -14.2350, "lon": -53.9253},
                    size_max=3,
                    mapbox_style="carto-positron")
# Add image
fig4.add_layout_image(
dict(
    source='https://cebrap.org.br/wp-content/uploads/2023/06/observatorio-religiao3-1536x400.png',
    xref="paper", yref="paper",
    x=1.0, y=1.00,
    sizex=0.4, sizey=0.4,
    xanchor="right", yanchor="bottom"
 )
)

# Add image
fig4.add_layout_image(
dict(
    source="https://cebrap.org.br/wp-content/themes/cebrap/images/logo-nav.png",
    xref="paper", yref="paper",
    x=0.99, y=1.03,
    sizex=0.1, sizey=0.1,
    xanchor="right", yanchor="bottom"
 )
)

with tab1:  
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    st.plotly_chart(fig2, use_container_width=True)
with tab3:
    st.plotly_chart(fig3, use_container_width=True)
with tab4:
    st.plotly_chart(fig4, use_container_width=True)




