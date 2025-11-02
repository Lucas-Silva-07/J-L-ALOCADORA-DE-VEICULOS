from src.gui.pages.base_page import BasePage


class ConfigurarConta(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()

    # ============================================
    # CRIANDO AS LABELS DA JANELA
    # ============================================
        # TITULO PRINCIPAL DA PAGINA
        self.criar_label(
            "CONFIGURAÇÕES DA CONTA", font_size=30, weight="bold", use_place=True, x=83, y=50, parent=self
        )
        # SUB TITULO
        self.criar_label(
            "Gerenciando informações da conta.", row=0, pady=(95, 0) ,font_size=14, color="#625B5B"
        )
        # TITULO NOME USUARIO
        usuario = "Lucas"
        self.criar_label(
            f"Usuário:   {usuario}", row=1, pady=(20, 0), font_size=16
        )
        # TITULO EMAIL
        email_usuario = "lucas@email.com"
        self.criar_label(
            f"Email:   {email_usuario}", row=2, pady=(20, 0), font_size=16
        )
        # TITULO SENHA
        senha_usuario = "senha teste"
        self.criar_label(
            f"Senha:   {'*'*len(senha_usuario)}", row=3, pady=(20, 0), font_size=16
        )

        self.criar_conta = self.criar_label(
            "EXCLUIR CONTA", row=5, pady=(20, 0), font_size=12, color="#c03838"
        )
        self.criar_conta.bind("<Button-1>", lambda e: self.trocar_tela("LoginPage"))
    

    # ============================================
    # CRIANDO BOTÃO SALVAR ALTERAÇÕES
    # ============================================
        self.criar_botao(
            "SALVAR ALTERAÇÕES", row= 4, padx=75, pady=(20, 0), command=lambda: self.trocar_tela("MenuPage")
        )

    # ============================================
    # FUNÇÃO PARA O BOTÃO ENTRAR
    # ============================================ 
    def btn_entrar(self):
        print("Entrar pressionado")

    # ============================================
    # FUNÇÃO EXIBIR / OCULTAR SENHA 
    # ============================================
    def alternar_password(self):
        if self.entry_senha.cget("show") == "" or self.entry_confirmar_senha.cget("show") == "":
            self.entry_senha.configure(show="*")
            self.entry_confirmar_senha.configure(show="*")
            self.btn_eye.configure(image=self.eye_closed_img)  # olho fechado
        else:
            self.entry_senha.configure(show="")
            self.entry_confirmar_senha.configure(show="")
            self.btn_eye.configure(image=self.eye_open_img)  # olho aberto


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
    root.title("Tela de Teste - CriarConta")
    root.configure(fg_color="#CECECE")
    page = ConfigurarConta(root, FakeController())
    page.pack(fill="both", expand=True)

    root.mainloop()