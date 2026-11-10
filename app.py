import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuração da página
st.set_page_config(
    page_title="Vixe Mainha - Sistema Comercial",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo para tela cheia
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Função para converter imagem da pasta static em Base64
def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            extensao = caminho.split('.')[-1].lower()
            if extensao == 'jpg':
                extensao = 'jpeg'
            return f"data:image/{extensao};base64,{encoded}"
    return ""

# Carrega as imagens da pasta static
logo_b64 = carregar_imagem_base64("static/logo.jpeg")
cabecalho_b64 = carregar_imagem_base64("static/cabecalho.jpg")

# Menu de navegação lateral
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Selecione a tela:", ["Sistema (Index)", "Cardápio (Online)"])

def injetar_imagens_no_html(conteudo_html):
    """Substitui qualquer variação de caminho da imagem pelo Base64 embutido"""
    if cabecalho_b64:
        conteudo_html = conteudo_html.replace('/app/static/cabecalho.jpg', cabecalho_b64)
        conteudo_html = conteudo_html.replace('./app/static/cabecalho.jpg', cabecalho_b64)
        conteudo_html = conteudo_html.replace('cabecalho.jpg', cabecalho_b64)
        
    if logo_b64:
        conteudo_html = conteudo_html.replace('/app/static/logo.jpeg', logo_b64)
        conteudo_html = conteudo_html.replace('./app/static/logo.jpeg', logo_b64)
        conteudo_html = conteudo_html.replace('logo.jpeg', logo_b64)
        
    return conteudo_html

if pagina == "Sistema (Index)":
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_index = f.read()
        html_index = injetar_imagens_no_html(html_index)
        components.html(html_index, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("O arquivo `index.html` não foi encontrado na raiz do projeto.")

elif pagina == "Cardápio (Online)":
    try:
        with open("cardapio.html", "r", encoding="utf-8") as f:
            html_cardapio = f.read()
        html_cardapio = injetar_imagens_no_html(html_cardapio)
        components.html(html_cardapio, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("O arquivo `cardapio.html` não foi encontrado na raiz do projeto.")