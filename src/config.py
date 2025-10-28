import os
# ============================================
# CAMINHO ATE A RAIZ DO PROJETO
# ============================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ANTERIOR = os.path.dirname(BASE_DIR)
#CAMINHO DO BANCO DE DADOS
DB_PATH = os.path.join(PASTA_ANTERIOR, "src", "database", "cars.db")
#CAMINHO DO ICONE
ICO_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "jl_icon.ico")
#CAMINHO DA FONTE DE TEXTO
FONT_POPINS = os.path.join(PASTA_ANTERIOR, "assets", "fonts", "Poppins-SemiBold.ttf")
#CAMINHO DA LOGO
LOGO_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "logo.png")
#CAMINHO PARA O OLHO DE VISIVEL/OCULTO
EYE_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "eye.png")
CLOSE_EYE_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "invisible.png")
#CAMINHO DA IMAGEM DO BOTÃO
BTN_NORMAL = os.path.join(PASTA_ANTERIOR, "assets", "images", "btn_normal.png")

IMG_CONSULTA = os.path.join(PASTA_ANTERIOR, "assets", "images", "img_consulta.png")
