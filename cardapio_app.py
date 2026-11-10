import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuração da página para o Cardápio do Cliente
st.set_page_config(
    page_title="Vixe Mainha - Cardápio Online",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo CSS para remover margens, cabeçalhos e barras do Streamlit (Tela Cheia)
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100% !important;
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

# Função para converter as imagens da pasta static em Base64
def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            extensao = caminho.split('.')[-1].lower()
            if extensao == 'jpg':
                extensao = 'jpeg'
            return f"data:image/{extensao};base64,{encoded}"
    return ""

logo_b64 = carregar_imagem_base64("static/logo.jpeg")
cabecalho_b64 = carregar_imagem_base64("static/cabecalho.jpg")

# Lê e injeta as imagens diretamente no cardapio.html
try:
    with open("cardapio.html", "r", encoding="utf-8") as f:
        html_cardapio = f.read()

    if cabecalho_b64:
        html_cardapio = html_cardapio.replace('/app/static/cabecalho.jpg', cabecalho_b64)
        html_cardapio = html_cardapio.replace('./app/static/cabecalho.jpg', cabecalho_b64)
        html_cardapio = html_cardapio.replace('cabecalho.jpg', cabecalho_b64)
        
    if logo_b64:
        html_cardapio = html_cardapio.replace('/app/static/logo.jpeg', logo_b64)
        html_cardapio = html_cardapio.replace('./app/static/logo.jpeg', logo_b64)
        html_cardapio = html_cardapio.replace('logo.jpeg', logo_b64)

    # Renderiza o cardápio em tela cheia
    components.html(html_cardapio, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("O arquivo `cardapio.html` não foi encontrado.")