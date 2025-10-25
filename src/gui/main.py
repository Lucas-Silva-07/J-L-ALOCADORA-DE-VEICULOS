import sys, os

# Garante que a raiz do projeto esteja no sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.gui.pages.login_page import LoginPage
from src.gui.pages.menu_page import MenuPage


class Controller:
    def __init__(self):
        self.tela_atual = None
        self.mostrar_tela("LoginPage")

    def mostrar_tela(self, nome_tela):
        """Cria e mostra a janela solicitada"""
        if nome_tela == "LoginPage":
            self.tela_atual = LoginPage(self)
        elif nome_tela == "MenuPage":
            self.tela_atual = MenuPage(self)
        else:
            raise ValueError(f"Tela {nome_tela} não encontrada.")

        self.tela_atual.mainloop()


if __name__ == "__main__":
    Controller()
