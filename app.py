import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar toda a largura
st.set_page_config(
    page_title="Vixe Mainha - Gestão Comercial",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeção de CSS personalizado para zerar margens e maximizar o iframe
st.markdown("""
    <style>
        /* Remove o cabeçalho padrão, o menu superior e o rodapé do Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        #root > div:nth-child(1) > div > div > div > div {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }

        /* Remove as margens e paddings do container principal */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* Oculta barras extras de rolagem do container pai */
        .stApp {
            margin: 0;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Seletor de páginas na barra lateral (Sidebar)
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Selecione a tela:", ["Sistema (Index)", "Cardápio (Online)"])

if pagina == "Sistema (Index)":
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_index = f.read()
        # Componente renderizado em altura estendida ocupando toda a tela
        components.html(html_index, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("O arquivo `index.html` não foi encontrado na raiz do projeto.")

elif pagina == "Cardápio (Online)":
    try:
        with open("cardapio.html", "r", encoding="utf-8") as f:
            html_cardapio = f.read()
        components.html(html_cardapio, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("O arquivo `cardapio.html` não foi encontrado na raiz do projeto.")