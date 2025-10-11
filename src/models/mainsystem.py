from ..database.conexao import criar_conexao

class MainSystem():

    def __init__(self):
        self.nome = None
        self.cat_custo = None
        self.carroceria = None
        self.carro = None
        self.valor = None
        self.conexao = None    

    def solicitar_nome(self):
        '''
        Solicita que o usuário insira seu nome, valida a entrada e retorna o nome em maiúscula.\n
        A função irá imprimir uma mensagem de orientação e ficara em looping em caso de entradas indesejadas.

        Parameters
        ----------
        Sem parâmetros

        Returns
        -------
        str
            Atribui a self.nome string com priemira letra em maiúscula
        ''' 
        while True:
            nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')  
            if nome.isalpha() and len(nome) >= 3:
                self.nome = nome.capitalize()
                return self.nome
            else:
                print('Entrada invalida. Por favor digite 3 letras ou mais e use apenas letras ')
 
    def solicitar_cat_custo(self):
        '''
        Solicita ao usuário o nome da categoria de custo ele deseja e guarda em maiúscula.

        Parameters
        ----------
        Sem parâmetros

        Returns
        -------
        str
            Atribui string em self.cat_custo com nome da coluna em letras maiúsculas.
        ''' 
        self.cat_custo = input("Digite a categoria (ex: Premium ou Custo beneficio): ").strip().upper()

    def conectar_dados(self):
        '''
        Faz a conexão com o banco de dados.

        Parameters
        ----------
        Sem parâmetros

        Returns
        -------
        Retona a conexão com o banco de dados e atribui em self.conexao
        ''' 
        self.conexao = criar_conexao()
        if not self.conexao:
            print('Erro na conexão com os dados')
    
    def filtrar_carroceria(self):
        '''
        Executa a função de conexão com o banco de dados e atribui a carroceria nos atributos da classe.

        Parameters
        ----------
        Sem parâmetros

        Returns
        -------
        str
            Atribui string com nome da carroceria em self.carroceria
        ''' 
        self.conectar_dados()
        cursor  = self.conexao.cursor()
        cursor.execute("SELECT DISTINCT Cat_Carro FROM CARROSS WHERE Cat_Custo = ?", (self.cat_custo,))
        tipos = cursor.fetchall()
        print(f"\nTipos disponíveis na categoria {self.cat_custo}:")
        for tipo in tipos:
            print(f"- {tipo['Cat_Carro']}")
        self.carroceria = input("\nDigite o tipo que deseja ver (ex: Esportivo): ").strip().upper()

    def filtrar_carros(self):
        '''
        Solicita ao usuário que escolha um carro específico da lista filtrada e atribui a self.carro
        Parameters
        ----------
        sem parâmetros
        
        Returns
        -------
        atribui resultado a self.carro
        '''
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM CARROSS WHERE Cat_Custo = ? AND Cat_Carro = ?", (self.cat_custo, self.carroceria))
        resultados = cursor.fetchall()
        print(f"\nModelos encontrados ({self.cat_custo} > {self.carroceria}):")
        for carro in resultados:
            print(f"- {carro['Nome']}")
        self.carro = input('\nDigite qual carro deseja: ').strip().upper()

    def carro_escolhido(self):
        '''
        Imprime mensagem personalizada com nome do usuário e mostra o veículo escolhido com seu valor.
        Parameters
        ----------
        sem parâmetros
        
        Returns
        -------
        None
        '''
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM CARROSS WHERE Cat_Custo = ? AND Cat_Carro = ? AND Nome = ?", (self.cat_custo, self.carroceria, self.carro))
        self.valor = cursor.fetchall()
        print(f'{self.nome} você escolheu o veículo {self.carro} da classe de custo {self.cat_custo} com o valor de R${self.valor[0][4]:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.'))

#main
if __name__ == '__run__':
    sistema = MainSystem()
    sistema.solicitar_nome()
    sistema.solicitar_cat_custo()
    print(sistema.nome)