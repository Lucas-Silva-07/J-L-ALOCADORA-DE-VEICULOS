from src.gui.pages.base_page import BasePage
from src.config import EYE_PATH, CLOSE_EYE_PATH
from PIL import Image
import customtkinter


class CriarConta(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()

    # ============================================
    # CRIANDO AS LABELS DA JANELA
    # ============================================
        self.criar_label(
            "CRIE SUA CONTA", row=0, pady=(55, 0), font_size=30, weight="bold"
        )

        self.criar_label(
            "Por favor, preencha seus dados para criar uma conta.", row=1, font_size=14, color="#625B5B"
        )

        self.criar_label(
            "Usuário:", row=2, pady=(20, 0), font_size=16
        )
        self.criar_label(
            "Email:", row=3, pady=(20, 0), font_size=16
        )

        self.criar_label(
            "Senha:", row=4, pady=(20, 0), font_size=16
        )
        self.criar_label(
            "Confirmar\nSenha:", row=5, pady=(20, 0), font_size=16
        )
        self.criar_conta = self.criar_label(
            "Já tem uma conta? Clique aqui.", row=7, pady=(20, 0), font_size=12, color="#c03838"
        )
        self.criar_conta.bind("<Button-1>", lambda e: self.trocar_tela("LoginPage"))
    
    # ============================================
    # CRIANDO OS ENTRY DA JANELA
    # ============================================
        self.entry_usuario = self.criar_entry(
            placeholder="Seu nome", width= 229, use_place=True, x=150, y=147
        )
        
        self.entry_email = self.criar_entry(
            placeholder="Digite seu email", width= 229, use_place=True, x=150, y=197
        )
        self.entry_senha = self.criar_entry(
            placeholder="Digite a senha", width= 229, use_place=True, x=150, y=247, show="*"
        )
        self.entry_confirmar_senha = self.criar_entry(
            placeholder="Digite a senha", width= 200, use_place=True, x=178, y=297, show="*"
        )
        

        self.btn_eye = customtkinter.CTkButton(
            self.frame_menu,
            text="", 
            image=self.eye_closed_img, 
            command=self.alternar_password, fg_color="transparent", 
            width=5, 
            hover=None
            )
        
        self.btn_eye.place(x=325, y=303)
    # ============================================
    # CRIANDO BOTÃO ENTRAR
    # ============================================
        self.criar_botao(
            "CRIAR CONTA", row= 6, padx=75, pady=(20, 0), command=lambda: self.trocar_tela("MenuPage")
        )

    # ============================================
    # FUNÇÃO PARA O BOTÃO ENTRAR
    # ============================================ 
    def btn_entrar(self):
        print("Entrar pressionado")
    # ============================================
    # CARREGANDO IMAGENS 
    # ============================================
    def carregar_recursos(self):
        super().carregar_recursos()
        self.eye_open_img = customtkinter.CTkImage(
            Image.open(EYE_PATH),
            size=(35, 15)
        )
        self.eye_closed_img = customtkinter.CTkImage(
            Image.open(CLOSE_EYE_PATH),
            size=(35, 15)
        )
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
    page = CriarConta(root, FakeController())
    page.pack(fill="both", expand=True)

    root.mainloop()