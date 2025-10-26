from src.gui.pages.base_page import BasePage


class NovaConsulta(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()

    # ============================================
    # CRIADO OS TEXTOS DA INTERFACE
    # ============================================
        self.criar_label(
            "NOVA SIMULAÇÃO DE ALUGUEL", row=0, padx=40, pady=(30, 0), font_size=30
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


    # ============================================
    # CRIANDO OS ENTRY DA JANELA
    # ============================================
        self.combobox_categoria = self.criar_combobox(
            row= 2, padx=40
        )
        self.combobox_carroceria = self.criar_combobox(
            row= 4, padx=40
        )
        self.combobox_carro = self.criar_combobox(
            row= 6, padx=40
        )

    # ============================================
    # CRIANDO OS BOTÕES DA JANELA
    # ============================================
        self.criar_botoes([
            ("CONSULTAR VALOR", self.consultar_valor, 7, 0, 40, (20, 0), "nw")
        ])

    def consultar_valor(self):
        print("Consultar valor pressionado")


if __name__ == "__main__":
    import customtkinter

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
