from src.config import ICO_PATH, LOGO_PATH, BOTAO_LOGIN, BOTAO_LOGIN_HOVER, EYE_PATH, CLOSE_EYE_PATH, FONT_POPINS
from PIL import Image
import customtkinter


class LoginPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Configurações da janela
        self.title("JL Alocadora de Veículos")
        self.largura_janela = 930
        self.altura_janela = 530
        self.largura_tela = self.winfo_screenwidth()
        self.altura_tela = self.winfo_screenheight()
        x = (self.largura_tela / 2) - (self.largura_janela / 2)
        y = (self.altura_tela / 2) - (self.altura_janela / 2)
        self.geometry(f"{self.largura_janela}x{self.altura_janela}+{int(x)}+{int(y)}")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure((0, 1), weight=0)
        self.configure(fg_color="#CECECE")
        self.iconbitmap(ICO_PATH)
        self.resizable(False, False)
        
        #Criando Frame login
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nw')        
        self.checkbox_frame.configure(fg_color="#CECECE")
        #Fonte personalizada
        customtkinter.FontManager.load_font(FONT_POPINS)
        #Label Bem Vindo
        self.texto1 = customtkinter.CTkLabel(self.checkbox_frame, text="ACESSE SUA CONTA", font=("Poppins SemiBold", 30, "bold"), text_color="black")
        self.texto1.grid(row=0, column=0, padx=75, pady=(75, 0), sticky='w')
        #Label pedindo email 
        self.texto2 = customtkinter.CTkLabel(self.checkbox_frame, text="Por favor, insira seus dados.", font=("Poppins SemiBold", 14), text_color="#625B5B")
        self.texto2.grid(row=1, column=0, padx=75, pady=(0, 0), sticky='w')
        #Label email
        self.texto3 = customtkinter.CTkLabel(self.checkbox_frame, text="Email", font=("Poppins SemiBold", 16), text_color="black")
        self.texto3.grid(row=2, column=0, padx=75, pady=(20, 0), sticky='w')
        #Caixa entrada email
        self.entry_email = customtkinter.CTkEntry(self.checkbox_frame, text_color= "black", placeholder_text="Digite seu email", fg_color="#CECECE", border_color="#ADADAD", width=300, height=40, font=("Poppins SemiBold", 12))
        self.entry_email.grid(row=3, column=0, padx=75, pady=(0, 0), sticky='w')
        #Label Senha
        self.texto4 = customtkinter.CTkLabel(self.checkbox_frame, text="Senha", font=("Poppins SemiBold", 16), text_color="black")
        self.texto4.grid(row=4, column=0, padx=75, pady=(20, 0), sticky='w')       
        #Caixa entrada senha
        self.entry_senha = customtkinter.CTkEntry(self.checkbox_frame, text_color= "black", show="*", placeholder_text="Digite a senha", fg_color="#CECECE", border_color="#ADADAD", width=300, height=40, font=("Poppins SemiBold", 12))
        self.entry_senha.grid(row=5, column=0, padx=75, pady=(0, 0), sticky='w')
        # Botão do olhinho ao lado do entry
        self.eye_open_img = customtkinter.CTkImage(Image.open(EYE_PATH), size=(35, 15))
        self.eye_closed_img = customtkinter.CTkImage(Image.open(CLOSE_EYE_PATH), size=(35, 15))
        self.btn_eye = customtkinter.CTkButton(self.checkbox_frame, text="", image=self.eye_closed_img, command=self.alternar_password, fg_color="transparent", width=5, hover=None)
        self.btn_eye.place(x=320, y=300)  # ajusta posição conforme necessário

        #Botão entrar
        #Imagem botão normal
        self.img_normal = customtkinter.CTkImage(
            light_image=Image.open(BOTAO_LOGIN),
            dark_image=Image.open(BOTAO_LOGIN),
            size=(300, 40)
        )
        #Imagem quando ficar com mouse em cima
        self.img_hover = customtkinter.CTkImage(
            light_image=Image.open(BOTAO_LOGIN_HOVER),
            dark_image=Image.open(BOTAO_LOGIN_HOVER),
            size=(300, 40)
        )
        self.button = customtkinter.CTkButton(self.checkbox_frame, text="",
                                                    command=self.button_callback,
                                                    width=300, 
                                                    height=40, 
                                                    fg_color="transparent", 
                                                    image=self.img_normal,
                                                    hover_color= "#CECECE")
        self.button.grid(row=6, column=0, padx=10, pady=(20, 0))
        self.button.bind("<Enter>", lambda e: self.button.configure(image = self.img_hover))
        self.button.bind("<Leave>", lambda e: self.button.configure(image = self.img_normal))
        #Cria uma imagem simples 
        self.image_logo = customtkinter.CTkImage(Image.open(LOGO_PATH), size=(530, 530))
        #Exibe a imagem em um Label
        self.logo_label = customtkinter.CTkLabel(self, image=self.image_logo, text="")
        self.logo_label.place(x=400, y=-20) 

        
    #Função do botão entrar
    def button_callback(self):
        print("button pressed")
    #Função senha mostrar/ocultar 
    def alternar_password(self):
        if self.entry_senha.cget("show") == "":
            self.entry_senha.configure(show="*")
            self.btn_eye.configure(image=self.eye_closed_img)  # olho fechado
        else:
            self.entry_senha.configure(show="")
            self.btn_eye.configure(image=self.eye_open_img)  # olho aberto

app = LoginPage()
app.mainloop()