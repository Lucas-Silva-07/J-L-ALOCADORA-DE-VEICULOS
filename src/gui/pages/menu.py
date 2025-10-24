from src.gui.pages.base_page import BasePage
import customtkinter


class MenuPage(BasePage):
    def __init__(self, controller=None):
        super().__init__(controller)
        self.configurar_janela()
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()
        self.criar_botoes([
            ("Nova Consulta", self.nova_consulta),
            ("Carros Alugados", self.carros_alugados),
            ("Configuração de Conta", self.configuracao_conta),
            ("Sair da Conta", self.sair_conta)
        ])
        self.texto_principal = customtkinter.CTkLabel(self,
            text="MENU PRINCIPAL", 
            font=("Poppins SemiBold", 34), 
            text_color="#3F3F3F", 
            fg_color="transparent", 
            bg_color="transparent", 
            )
        self.texto_principal.place(x=320, y=40)

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
