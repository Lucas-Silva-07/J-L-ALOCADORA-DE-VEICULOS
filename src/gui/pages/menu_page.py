from src.gui.pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, controller):
        super().__init__(controller)
        self.configurar_janela()
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()
        self.criar_botoes([
            ("Nova Consulta", self.nova_consulta, 0, 0, 75, (140, 0)),
            ("Carros Alugados", self.carros_alugados, 1, 0, 75, (20, 0)),
            ("Configuração de Conta", self.configuracao_conta, 2, 0, 75, (20, 0)),
            ("Sair da Conta", lambda: self.trocar_tela("LoginPage"), 3, 0, 75, (20, 0))
        ])
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

    def sair_conta(self):
        print("Sair da conta pressionado")


if __name__ == "__main__":
    app = MenuPage(controller=None)
    app.mainloop()
