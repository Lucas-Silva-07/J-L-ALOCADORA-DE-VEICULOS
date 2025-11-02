from src.gui.pages.base_page import BasePage
from src.config import IMG_CONSULTA
from PIL import Image
import customtkinter

class NovaConsulta(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo(x=500, y=-75)
    # ============================================
    # CRIADO OS TEXTOS DA INTERFACE
    # ============================================
        self.criar_label(
            "NOVA SIMULAÇÃO DE ALUGUEL", row=0, padx=40, pady=(30, 0), font_size=28
        )
        self.criar_label(
            "Escolha a Categoria de Custo:", row=1, padx=40, pady=(0, 0), font_size=16
        )
        self.criar_label(
            "Escolha a Carroceria:", row=3, padx=40, pady=(20, 0), font_size=16
        )
        self.criar_label(
            "Modelo do Carro:", row=5, padx=40, pady=(20, 0), font_size=16
        )

        self.criar_label(
            "R$ 3.500,00", font_size=30, use_place=True, x=580, y=140, parent=self, bg_color="white"
        )

    # ============================================
    # CRIANDO OS COMBOBOX DA JANELA
    # ============================================
        self.combobox_categoria = self.criar_combobox(
            row=2, padx=40, texto="Selecione a Categoria"
        )
        self.combobox_carroceria = self.criar_combobox(
            row=4, padx=40, texto="Selecione a Carroceria"
        )
        self.combobox_carro = self.criar_combobox(
            row=6, padx=40, texto="Selecione o Modelo"
        )

    # ============================================
    # CRIANDO OS BOTÕES DA JANELA
    # ============================================
        self.criar_botao(
            "CONSULTAR VALOR", row= 7, padx=40, pady=(20, 0)
        )

        self.criar_botao(
            "VOLTAR", row= 8, padx=40, pady=(20, 0), tamanho= (150, 40), command=lambda: self.trocar_tela("MenuPage")
        )

        self.criar_botao(
            "LIMPAR", use_place=True, parent=self,tamanho= (150, 40), x=500, y=415, command= self.limpar_todos_combobox
        )

        self.criar_botao(
            "ACEITAR", use_place=True, parent=self,tamanho= (150, 40), x=700, y=415
        )

    # ============================================
    # CARREGANDO IMAGEM ONDE FICA O VALOR 
    # ============================================
    def carregar_recursos(self):
        super().carregar_recursos()
        self.img_logo = customtkinter.CTkImage(
            Image.open(IMG_CONSULTA),
            size=(350, 350)
        )

if __name__ == "__main__":
    # Classe "fake" simulando o controller
    class FakeController:
        def mostrar_tela(self, nome_tela):
            print(f"Trocando para: {nome_tela}")
    
    # Janela principal fake
    root = customtkinter.CTk()
    largura_janela = 930
    altura_janela = 530
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    x = (largura_tela / 2) - (largura_janela / 2)
    y = (altura_tela / 2) - (altura_janela / 2)

    root.geometry(f"{largura_janela}x{altura_janela}+{int(x)}+{int(y)}")
    root.resizable(False, False)
    root.title("Tela de Teste - MenuPage")
    root.configure(fg_color="#CECECE")
    page = NovaConsulta(root, FakeController())
    page.pack(fill="both", expand=True)

    root.mainloop()