import streamlit as st
import streamlit.components.v1 as components
import base64
import json
import os

# Configuração da página
st.set_page_config(
    page_title="Vixe Mainha - Cardápio Online",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo CSS para tela cheia e remoção de elementos do Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QSob, .styles_viewerBadge__1yG5_, [data-testid="stStatusWidget"] {
            display: none !important;
            visibility: hidden !important;
        }
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

logo_b64 = carregar_imagem_base64("static/logo.jpeg")
cabecalho_b64 = carregar_imagem_base64("static/cabecalho.jpg")

# Injeta o manifesto do PWA via dado URI (Garante que o celular reconheça o ícone e o nome do app)
manifest_data = {
    "name": "Vixe Mainha Marmitaria",
    "short_name": "Vixe Mainha",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#0f172a",
    "theme_color": "#0f172a",
    "icons": [
        {
            "src": logo_b64,
            "sizes": "192x192 512x512",
            "type": "image/jpeg"
        }
    ]
}
manifest_json = json.dumps(manifest_data)
manifest_uri = f"data:application/manifest+json,{manifest_json}"

try:
    with open("cardapio.html", "r", encoding="utf-8") as f:
        html_cardapio = f.read()

    # Insere o manifesto PWA no HTML dinamicamente
    pwa_tags = f"""
    <link rel="manifest" href="{manifest_uri}">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Vixe Mainha">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#0f172a">
    <link rel="apple-touch-icon" href="{logo_b64}">
    <link rel="icon" type="image/jpeg" href="{logo_b64}">
    """
    
    html_cardapio = html_cardapio.replace('</head>', f'{pwa_tags}\n</head>')

    # Substitui as imagens do cabeçalho e logo
    if logo_b64:
        html_cardapio = html_cardapio.replace('src="/app/static/logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="./app/static/logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="logo.jpeg"', f'src="{logo_b64}"')
        html_cardapio = html_cardapio.replace('src="/app/static/logo.jpg"', f'src="{logo_b64}"')

    if cabecalho_b64:
        html_cardapio = html_cardapio.replace('src="/app/static/cabecalho.jpg"', f'src="{cabecalho_b64}"')
        html_cardapio = html_cardapio.replace('src="./app/static/cabecalho.jpg"', f'src="{cabecalho_b64}"')
        html_cardapio = html_cardapio.replace('src="cabecalho.jpg"', f'src="{cabecalho_b64}"')

    components.html(html_cardapio, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("O arquivo `cardapio.html` não foi encontrado na raiz do repositório.")