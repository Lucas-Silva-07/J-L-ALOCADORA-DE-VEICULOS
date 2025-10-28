from src.gui.pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()
    # ============================================
    # CRIANDO BOTÕES DA TELA
    # ============================================
        self.criar_botao(
            "Nova Consulta", row= 0, padx=75, pady=(140, 0), command=lambda: self.trocar_tela("NovaConsulta")
        )
        self.criar_botao(
            "Carros Alugados", row= 1, padx=75, pady=(20, 0), command=self.carros_alugados
        )
        self.criar_botao(
            "Configuração de Conta", row= 2, padx=75, pady=(20, 0), command= self.configuracao_conta
        )
        self.criar_botao(
            "Sair da Conta", row= 3, padx=75, pady=(20, 0), command=lambda: self.trocar_tela("LoginPage")
        )

    # ============================================
    # TEXTO PRINCIPAL
    # ============================================
        self.criar_label(
            "MENU PRINCIPAL", 
            font_size=34,
            color="#3F3F3F",
            use_place=True,
            x=320,
            y=40,
            parent=self
        )
    # ============================================
    # FUNÇÕES DOS BOTÕES
    # ============================================
    def nova_consulta(self):
        print("Nova consulta pressionado")

    def carros_alugados(self):
        print("Carros alugados pressionado")

    def configuracao_conta(self):
        print("Configuração de conta pressionado")


if __name__ == "__main__":
    app = MenuPage(controller=None)
    app.mainloop()
