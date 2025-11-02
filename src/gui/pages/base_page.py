from src.config import LOGO_PATH, FONT_POPINS, BTN_NORMAL
from PIL import Image, ImageEnhance
import customtkinter


class BasePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # Configura layout interno
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#CECECE")
        self.comboboxes = []  # LISTA PARA PODER LIMPAR OS COMBOBOX
    # ============================================
    # FUNÇÃO PARA TROCAR DE TELA 
    # ============================================
    def trocar_tela(self, nome_tela):
        """Pede ao controller para abrir uma nova janela e destruir a atual"""
        self.controller.mostrar_tela(nome_tela)

    # ============================================
    # CARREGAMENTO DE RECURSOS (FONTES / IMAGENS)
    # ============================================
    def carregar_recursos(self):
        """Carrega fontes e imagens usadas na interface"""
        # Fonte personalizada
        customtkinter.FontManager.load_font(FONT_POPINS)

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

    def criar_logo(self, x=400, y=-20):
        """Exibe o logo à direita"""
        label_logo = customtkinter.CTkLabel(self, image=self.img_logo, text="")
        label_logo.place(x=x, y=-y)

    # ============================================
    # CRIAR LABEL
    # ============================================ 
    def criar_label(self, texto, row=None, column=0, padx=75, pady=(0, 0), font_size=16, color="black", weight="normal", sticky='w', 
                    use_place=False, x=10, y=10, bg_color="transparent", fg_color="transparent", parent=None,):
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
    def criar_botao(self, texto, font_size=14, text_color="white", row=None, column=0, padx=0, pady=(0, 0), tamanho=(300, 40), 
                    sticky='w',  use_place=False, x=10, y=10, parent=None, command=None):
        """Cria um botão padrão do menu usando label com imagem"""

        parent= parent or self.frame_menu
        if command is None:
            command = self.btn_callback
        # CARREGAR IMAGEM    
        self.img_base = Image.open(BTN_NORMAL)
        self.img_button = customtkinter.CTkImage(
            light_image=self.img_base,
            dark_image=self.img_base,
            size=tamanho
        )

        botao = customtkinter.CTkLabel(
            parent, 
            text=texto, 
            font=("Poppins SemiBold", font_size), 
            text_color=text_color, 
            fg_color="transparent", 
            bg_color="transparent", 
            image=self.img_button,
            cursor="hand2"
        )

        if use_place:
            botao.place(x=x, y=y)
        else:
        # row precisa estar definido para usar grid
            if row is None:
                raise ValueError("O parâmetro 'row' é obrigatório quando não estiver usando place().")
            botao.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        botao.bind("<Button-1>", lambda e, f=command: f()) # item[1] é a função
            
        self.adicionar_hover_escurecer(botao, tamanho=tamanho)
        
        return botao

    # ============================================
    # FUNÇÃO PARA CRIAR OS ENTRY
    # ============================================
    def criar_entry(self, placeholder="", row=None, column=0, padx=75, pady=(0, 0), sticky='w', show="", width=300, height=40, use_place=False, x=10, y=10):
        entry = customtkinter.CTkEntry(
            self.frame_menu, 
            text_color= "gray", 
            placeholder_text=placeholder, 
            fg_color="#CECECE", 
            border_color="#A3A3A3", 
            width=width, 
            height=height, 
            font=("Poppins SemiBold", 14),
            show=show
            )
        
        if use_place:
            entry.place(x=x, y=y)
        else:
        # row precisa estar definido para usar grid
            if row is None:
                raise ValueError("O parâmetro 'row' é obrigatório quando não estiver usando place().")
            entry.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        
        return entry
    
    # ============================================
    # FUNÇÃO PARA CRIAR OS COMBOBOX
    # ============================================
    def criar_combobox(self, command=None, row=0, column=0, padx=20, pady=(0, 0), sticky='w', texto="Selecione uma opção"):
        frame_borda = customtkinter.CTkFrame(
            self.frame_menu,
            border_width=2,  # Define a largura da borda do frame
            corner_radius=25,
            bg_color="transparent",
            fg_color="#cecece",
            width=300,
            height=40,
            border_color="gray"
        ) 
        frame_borda.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        
        # Cria a variável do combobox
        combo_var = customtkinter.StringVar(value=texto)
        
        # Se nenhum comando for passado, usa o método padrão
        if command is None:
            command = self.combobox_callback

        opcoes = ["Opção 1", "Opção 2", "Opção 3"]
        
        # Cria o combobox
        combobox = customtkinter.CTkComboBox(
            master=frame_borda,
            width=280,
            height=20,
            variable=combo_var,
            corner_radius=15,
            text_color= "#808080",
            fg_color="#CECECE",
            border_color="#CECECE",
            bg_color="transparent",
            font=("Poppins SemiBold", 14),
            dropdown_font=("Poppins SemiBold", 14, "bold"),
            dropdown_fg_color="#CECECE",
            dropdown_text_color="black",
            dropdown_hover_color="gray",
            values=opcoes,
            command=lambda choice: self._on_combobox_select(choice, combobox, combo_var, texto, command),
            button_color="#CECECE",
            button_hover_color="#CECECE"
        )
        combobox.place(relx=0.5, rely=0.51, anchor=customtkinter.CENTER)
        # Coloca como "somente leitura"
        combobox._entry.configure(state="readonly")
        # Marca internamente o placeholder
        combobox._is_placeholder = True
        combobox._placeholder_text = texto
        combobox._entry.configure(fg="#808080")  # texto cinza inicial
        # adiciona o combobox à lista
        self.comboboxes.append({"combo": combobox, "var": combo_var, "placeholder": texto})

        return combobox
    
    # ============================================   
    # FUNÇÃO PARA GERENCIAR O PLACEHOLDER 
    # ============================================ 
    def _on_combobox_select(self, choice, combobox, combo_var, placeholder, command):
        """Gerencia a seleção e o placeholder do combobox."""
        # Atualiza cor e estado normal
        combo_var.set(choice)
        combobox._entry.configure(fg="#000000")
        combobox._is_placeholder = False
        # Chama o callback externo (se houver)
        if callable(command):
            command(choice)

    # ============================================   
    # FUNÇÃO PARA LIMPAR TODOS PLACEHOLDER
    # ============================================   
    def limpar_todos_combobox(self):
        for item in self.comboboxes:
            combo = item["combo"]
            var = item["var"]
            placeholder = item["placeholder"]
            var.set(placeholder)                # atualiza o StringVar
            combo._entry.configure(fg="#808080")  # coloca texto em cinza
            combo._is_placeholder = True
        

    # ============================================        
    # Função quando uma opção for selecionada no combobox
    # ============================================
    def combobox_callback(self,choice):
        print("Opção selecionada:", choice)

    # ============================================
    # Função que será chamada quando um botão for pressionado
    # ============================================
    def btn_callback(self):
        print("Botão pressionado")

    # ============================================
    # EFEITO HOVER ESCURECER
    # ============================================
    def adicionar_hover_escurecer(self, botao, tamanho=(300, 40)):
        """Aplica efeito suave de escurecimento no hover"""
        botao._hover_ativo = False
        botao._brilho_atual = 1.0  # brilho inicial (100%)

        def on_enter(_):
            botao._hover_ativo = True
            self._animar_escurecer(botao, 1.0, 0.55, tamanho=tamanho)  # 85% brilho no hover

        def on_leave(_):
            botao._hover_ativo = False
            self._animar_escurecer(botao, botao._brilho_atual, 1.0, tamanho=tamanho)

        botao.bind("<Enter>", on_enter)
        botao.bind("<Leave>", on_leave)

    def _animar_escurecer(self, botao, brilho_inicial, brilho_final, passos=8, tempo=20, tamanho=(300, 40)):
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
                    size=tamanho
                )
                botao.configure(image=nova_img)

                self.after(tempo, animar)

        animar()