import sys, os
import customtkinter
# ============================================
# Garante que o projeto pode importar src.*
# ============================================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.gui.pages.login_page import LoginPage
from src.gui.pages.menu_page import MenuPage


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    # ============================================
    # CONFIGURAÇÕES DA JANELA PRINCIPAL
    # ============================================
        self.title("JL Alocadora de Veículos")
        largura_janela = 930
        altura_janela = 530
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        x = (largura_tela / 2) - (largura_janela / 2)
        y = (altura_tela / 2) - (altura_janela / 2)

        self.geometry(f"{largura_janela}x{altura_janela}+{int(x)}+{int(y)}")
        self.resizable(False, False)
        self.configure(fg_color="#CECECE")

        # ============================================
        # Container para empilhar os frames
        # ============================================
        self.container = customtkinter.CTkFrame(self, fg_color="#CECECE")
        self.container.pack(fill="both", expand=True)

        # ============================================
        # Garante que o container se expanda
        # ============================================
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # ============================================
        # Criando e armazenando cada página
        # ============================================
        
        # Dicionário de telas
        self.frames = {}

        for Page in (LoginPage, MenuPage):
            nome = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostra a primeira tela
        self.mostrar_tela("LoginPage")

    def mostrar_tela(self, nome_tela):
        """Traz o frame desejado para frente"""
        frame = self.frames[nome_tela]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
