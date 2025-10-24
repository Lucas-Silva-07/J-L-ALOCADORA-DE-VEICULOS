from src.config import ICO_PATH, LOGO_PATH, FONT_POPINS, BTN_NORMAL
from PIL import Image, ImageEnhance
import customtkinter


class BasePage(customtkinter.CTk):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

    def trocar_tela(self, nome_tela):
        """Função comum para todas as páginas."""
        self.controller.mostrar_tela(nome_tela)
    # ============================================
    # CONFIGURAÇÕES BÁSICAS
    # ============================================
    def configurar_janela(self):
        """Define aparência e posição da janela"""
        self.title("JL Alocadora de Veículos")

        largura_janela = 930
        altura_janela = 530
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        x = (largura_tela / 2) - (largura_janela / 2)
        y = (altura_tela / 2) - (altura_janela / 2)

        self.geometry(f"{largura_janela}x{altura_janela}+{int(x)}+{int(y)}")
        self.resizable(False, False)
        self.configure(fg_color="#CECECE")
        self.iconbitmap(ICO_PATH)

    # ============================================
    # CARREGAMENTO DE RECURSOS (FONTES / IMAGENS)
    # ============================================
    def carregar_recursos(self):
        """Carrega fontes e imagens usadas na interface"""
        # Fonte personalizada
        customtkinter.FontManager.load_font(FONT_POPINS)

        # Carrega imagem base uma única vez
        self.img_base = Image.open(BTN_NORMAL)

        # Cria CTkImage padrão
        self.img_normal = customtkinter.CTkImage(
            light_image=self.img_base,
            dark_image=self.img_base,
            size=(300, 40)
        )

        # Logo
        self.img_logo = customtkinter.CTkImage(
            Image.open(LOGO_PATH),
            size=(530, 530)
        )

    # ============================================
    # ESTRUTURA PRINCIPAL
    # ============================================
    def criar_frame_principal(self):
        """Cria o frame da lateral esquerda"""
        self.frame_menu = customtkinter.CTkFrame(self, fg_color="#CECECE")
        self.frame_menu.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nw")

        # Controla espaçamento interno dos botões
        self.frame_menu.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.frame_menu.grid_columnconfigure(0, weight=1)

    def criar_logo(self):
        """Exibe o logo à direita"""
        label_logo = customtkinter.CTkLabel(self, image=self.img_logo, text="")
        label_logo.place(x=400, y=-20)

    # ============================================
    # CRIAR LABEL
    # ============================================ 
    def criar_label(self, texto, row=None, column=0, padx=75, pady=(0, 0), font_size=16, color="black", weight="normal", sticky='w', use_place=False, x=10, y=10, bg_color="transparent", fg_color="transparent", parent=None,):
        """
        Cria uma label padronizada e posiciona com grid ou place.
        
        Parâmetros:
            texto (str): texto da label
            row (int): linha para usar com grid
            column (int): coluna para usar com grid
            padx, pady: espaçamento do grid
            font_size (int): tamanho da fonte
            color (str): cor do texto
            weight (str): estilo da fonte (normal/bold/etc)
            sticky (str): alinhamento no grid
            use_place (bool): se True, usa .place() em vez de .grid()
            x, y (int): posição absoluta se usar .place()
        """
        parent = parent or self.frame_menu  # padrão: frame_menu
        fonte = ("Poppins SemiBold", font_size, weight)
        label = customtkinter.CTkLabel(
            parent,
            text=texto,
            font=fonte,
            text_color=color,
            fg_color=fg_color,  # garante que o fundo não fique branco
            bg_color=bg_color
        )

        if use_place:
            label.place(x=x, y=y)
        else:
            # row precisa estar definido para usar grid
            if row is None:
                raise ValueError("O parâmetro 'row' é obrigatório quando não estiver usando place().")
            label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

        return label


    # ============================================
    # BOTÕES E FUNÇÕES
    # ============================================
    def criar_botoes(self,lista_tupla):
        """
        Recebe uma lista de Tupla com [(nome do botão, função do botão, linha, coluna, padx, pady)]
        Cria e posiciona todos os botões do menu"""
        botoes = lista_tupla

        for texto, funcao, linha, coluna, padx, pady in botoes:
            label = self.criar_botao(texto)
            label.grid(row=linha, column=coluna, padx=padx, pady=pady)
            label.bind("<Button-1>", lambda e, f=funcao: f())  # passa a função corretamente
            self.adicionar_hover_escurecer(label)

    def criar_botao(self, texto):
        """Cria um botão padrão do menu usando label com imagem"""
        return customtkinter.CTkLabel(
            self.frame_menu, 
            text=texto, 
            font=("Poppins SemiBold", 14), 
            text_color="white", 
            fg_color="transparent", 
            bg_color="transparent", 
            image=self.img_normal,
            cursor="hand2"
            )

    # ============================================
    # EFEITO HOVER ESCURECER
    # ============================================
    def adicionar_hover_escurecer(self, botao):
        """Aplica efeito suave de escurecimento no hover"""
        botao._hover_ativo = False
        botao._brilho_atual = 1.0  # brilho inicial (100%)

        def on_enter(_):
            botao._hover_ativo = True
            self._animar_escurecer(botao, 1.0, 0.55)  # 85% brilho no hover

        def on_leave(_):
            botao._hover_ativo = False
            self._animar_escurecer(botao, botao._brilho_atual, 1.0)

        botao.bind("<Enter>", on_enter)
        botao.bind("<Leave>", on_leave)

    def _animar_escurecer(self, botao, brilho_inicial, brilho_final, passos=8, tempo=20):
        """Anima suavemente a mudança de brilho"""
        diferenca = (brilho_final - brilho_inicial) / passos
        brilho = brilho_inicial

        def animar():
            nonlocal brilho
            if ((brilho_final > brilho_inicial and brilho < brilho_final) or
                (brilho_final < brilho_inicial and brilho > brilho_final)):

                brilho += diferenca
                botao._brilho_atual = brilho

                # Ajusta brilho da imagem base
                enhancer = ImageEnhance.Brightness(self.img_base)
                img_editada = enhancer.enhance(brilho)

                # Atualiza a imagem no botão
                nova_img = customtkinter.CTkImage(
                    light_image=img_editada,
                    dark_image=img_editada,
                    size=(300, 40)
                )
                botao.configure(image=nova_img)

                self.after(tempo, animar)

        animar()