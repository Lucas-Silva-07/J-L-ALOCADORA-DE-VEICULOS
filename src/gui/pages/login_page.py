from src.gui.pages.base_page import BasePage
from src.config import EYE_PATH, CLOSE_EYE_PATH
from PIL import Image
import customtkinter


class LoginPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.carregar_recursos()
        self.criar_frame_principal()
        self.criar_logo()
    # ============================================
    # CRIANDO AS LABELS DA JANELA
    # ============================================
        self.criar_label(
            "ACESSE SUA CONTA", row=0, pady=(75, 0), font_size=30, weight="bold"
        )

        self.criar_label(
            "Por favor, insira seus dados.", row=1, font_size=14, color="#625B5B"
        )

        self.criar_label(
            "Email:", row=2, pady=(20, 0), font_size=16
        )

        self.criar_label(
            "Senha:", row=4, pady=(20, 0), font_size=16
        )
    
    # ============================================
    # CRIANDO OS ENTRY DA JANELA
    # ============================================
        self.entry_email = self.criar_entry(
            placeholder="Digite seu email",
            row=3     
        )
        
        self.entry_senha = self.criar_entry(
            placeholder="Digite a senha",
            row=5,
            show="*"
        )

        self.btn_eye = customtkinter.CTkButton(
            self.frame_menu,
            text="", 
            image=self.eye_closed_img, 
            command=self.alternar_password, fg_color="transparent", 
            width=5, 
            hover=None
            )
        
        self.btn_eye.place(x=320, y=300)
    # ============================================
    # CRIANDO BOTÃO ENTRAR
    # ============================================
        self.criar_botoes([
            ("ENTRAR", lambda: self.trocar_tela("MenuPage"), 6, 0, 75, (20, 0))
        ])

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
        if self.entry_senha.cget("show") == "":
            self.entry_senha.configure(show="*")
            self.btn_eye.configure(image=self.eye_closed_img)  # olho fechado
        else:
            self.entry_senha.configure(show="")
            self.btn_eye.configure(image=self.eye_open_img)  # olho aberto


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
