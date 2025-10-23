from src.config import ICO_PATH, LOGO_PATH, FONT_POPINS, BTN_NOMRAL, BTN_HOVER
from PIL import Image
import customtkinter


class MenuPage(customtkinter.CTk):
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

        #Criando Frame 
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nw')        
        self.checkbox_frame.configure(fg_color="#CECECE")
        #Fonte personalizada
        customtkinter.FontManager.load_font(FONT_POPINS)
        #Cria uma imagem simples 
        self.image_logo = customtkinter.CTkImage(Image.open(LOGO_PATH), size=(530, 530))
        #Exibe a imagem em um Label
        self.logo_label = customtkinter.CTkLabel(self, image=self.image_logo, text="")
        self.logo_label.place(x=400, y=-20) 

        #Imagens dos botões
        #Imagem botão normal
        self.img_normal = customtkinter.CTkImage(
            light_image=Image.open(BTN_NOMRAL),
            dark_image=Image.open(BTN_NOMRAL),
            size=(300, 40)
        )
        #Imagem quando ficar com mouse em cima
        self.img_hover = customtkinter.CTkImage(
            light_image=Image.open(BTN_HOVER),
            dark_image=Image.open(BTN_HOVER),
            size=(300, 40)
        )
        #Botão nova consulta
        self.btn_nova_consulta = self.criar_btn(funcao=self.nova_consulta)
        self.btn_nova_consulta.grid(row=0, column=0, padx=75, pady=(140, 0))
        self.criar_hover(botao=self.btn_nova_consulta)
        #botao carros alugados
        self.btn_carros_algugados = self.criar_btn(funcao=self.carros_alugados)
        self.btn_carros_algugados.grid(row=1, column=0, padx=75, pady=(10, 0))
        self.criar_hover(botao=self.btn_carros_algugados)
        #Botão configuração de conta
        self.btn_congigurar_conta = self.criar_btn(funcao=self.configuracao_conta)
        self.btn_congigurar_conta.grid(row=2, column=0, padx=75, pady=(10, 0))
        self.criar_hover(botao=self.btn_congigurar_conta)       
        #Botão sair da conta
        self.btn_sair_conta = self.criar_btn(funcao=self.sair_conta)
        self.btn_sair_conta.grid(row=3, column=0, padx=75, pady=(10, 0))
        self.criar_hover(botao=self.btn_sair_conta)        

    #Função criar botão
    def criar_btn(self, funcao):
        btn = customtkinter.CTkButton(self.checkbox_frame, text="",
                                                    command=funcao,
                                                    width=300, 
                                                    height=40, 
                                                    fg_color="transparent", 
                                                    image=self.img_normal,
                                                    hover_color= "#CECECE")
        return btn

    #Funçao criar efeito hover
    def criar_hover(self, botao):
        botao.bind("<Enter>", lambda e: botao.configure(image = self.img_hover))
        botao.bind("<Leave>", lambda e: botao.configure(image = self.img_normal))

    #Função dos botões
    def nova_consulta(self):
        print("button pressed")

    def carros_alugados(self):
        print("button pressed")

    def configuracao_conta(self):
        print("button pressed")

    def sair_conta(self):
        print("button pressed")

app = MenuPage()
app.mainloop()