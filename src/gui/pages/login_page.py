from src.config import ICO_PATH, LOGO_PATH, FONT_POPINS
import customtkinter
import tkinter as tk
from PIL import Image


class App(customtkinter.CTk):
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
        self.checkbox_frame.configure(fg_color="transparent")

        #Criando Frame Logo
        #self.checkbox_frame2 = customtkinter.CTkFrame(self)
        #self.checkbox_frame2.grid(row=0, column=1, padx=10, pady=(10, 0))        
        #self.checkbox_frame2.configure(fg_color="blue")

        #Label Bem Vindo
        self.texto1 = tk.Label(self.checkbox_frame, text="Bem Vindo", font=("Poppins", 34, "bold"), background="#CECECE")
        self.texto1.grid(row=0, column=0, padx=75, pady=(75, 0), sticky='w')
        #Label pedindo email 
        self.texto2 = tk.Label(self.checkbox_frame, text=" Por favor, insira seus dados.", font=("Poppins", 10), fg="#525151", background="#CECECE")
        self.texto2.grid(row=1, column=0, padx=75, pady=(0, 0), sticky='w')
        #Label email
        self.texto3 = tk.Label(self.checkbox_frame, text="Email", font=("Poppins", 12), background="#CECECE")
        self.texto3.grid(row=2, column=0, padx=75, pady=(20, 0), sticky='w')
        #Caixa entrada email
        self.entry_email = customtkinter.CTkEntry(self.checkbox_frame, placeholder_text="Digite seu email")
        self.entry_email.grid(row=3, column=0, padx=75, pady=(0, 0), sticky='w')
        #Label Senha
        self.texto4 = tk.Label(self.checkbox_frame, text="Senha", font=("Poppins", 12), background="#CECECE")
        self.texto4.grid(row=4, column=0, padx=75, pady=(20, 0), sticky='w')       
        #Caixa entrada senha
        self.entry_senha = customtkinter.CTkEntry(self.checkbox_frame, placeholder_text="Digite a senha")
        self.entry_senha.grid(row=5, column=0, padx=75, pady=(0, 0), sticky='w')

        #Botão entrar
        self.button = customtkinter.CTkButton(self.checkbox_frame, text="Entrar", command=self.button_callback)
        self.button.grid(row=6, column=0, padx=10, pady=(20, 0))
        #Cria uma imagem simples (sem tema)
        self.logo = customtkinter.CTkImage(Image.open(LOGO_PATH), size=(530, 530))
        # Exibe a imagem em um Label
        logo_label = customtkinter.CTkLabel(self, image=self.logo, text="")
        logo_label.grid(row=0, column=2, padx=10, pady=10) 




    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()