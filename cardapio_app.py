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

# Estilo CSS para zerar margens e forçar tela cheia
st.markdown("""
    <style>
        /* Esconde cabeçalho, rodapé e menu do Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Esconde o botão flutuante de 'Hosted with Streamlit' */
        .viewerBadge_container__1QSob, .styles_viewerBadge__1yG5_, [data-testid="stStatusWidget"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Força o site a ocupar 100% da tela sem margens */
        .block-container {
            padding: 0rem !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 999999;
        }
    </style>
""", unsafe_allow_html=True)

def carregar_imagem_base64(caminho):
    """Procura a imagem no caminho indicado ou com extensão alternativa (.jpg / .jpeg)"""
    if not os.path.exists(caminho):
        if caminho.endswith('.jpeg'):
            caminho = caminho.replace('.jpeg', '.jpg')
        elif caminho.endswith('.jpg'):
            caminho = caminho.replace('.jpg', '.jpeg')

    if os.path.exists(caminho):
        with open(caminho, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            ext = caminho.split('.')[-1].lower()
            if ext == 'jpg':
                ext = 'jpeg'
            return f"data:image/{ext};base64,{encoded}"
    return ""

# Carrega as imagens
logo_b64 = carregar_imagem_base64("static/logo.jpeg")
cabecalho_b64 = carregar_imagem_base64("static/cabecalho.jpg")

try:
    with open("cardapio.html", "r", encoding="utf-8") as f:
        html_cardapio = f.read()

    # Substitui todas as formas possíveis de src da logo no HTML
    if logo_b64:
        html_cardapio = html_cardapio.replace('src="/app/static/logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="./app/static/logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="/app/static/logo.jpg"', f'src="{logo_b64}"')

    # Substitui todas as formas possíveis de src do cabeçalho no HTML
    if cabecalho_b64:
        html_cardapio = html_cardapio.replace('src="/app/static/cabecalho.jpg"', f'src="{cabecalho_b64}"')
        html_cardapio = html_cardapio.replace('src="./app/static/cabecalho.jpg"', f'src="{cabecalho_b64}"')
        html_cardapio = html_cardapio.replace('src="cabecalho.jpg"', f'src="{cabecalho_b64}"')

    # Renderiza o HTML modificado no iframe do Streamlit
    components.html(html_cardapio, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("O arquivo `cardapio.html` não foi encontrado na raiz do repositório.")