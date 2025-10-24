import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ANTERIOR = os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(PASTA_ANTERIOR, "src", "database", "cars.db")

ICO_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "jl_icon.ico")

FONT_POPINS = os.path.join(PASTA_ANTERIOR, "assets", "fonts", "Poppins-SemiBold.ttf")

LOGO_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "logo.png")

EYE_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "eye.png")
CLOSE_EYE_PATH = os.path.join(PASTA_ANTERIOR, "assets", "images", "invisible.png")

BTN_NORMAL = os.path.join(PASTA_ANTERIOR, "assets", "images", "btn_normal.png")
