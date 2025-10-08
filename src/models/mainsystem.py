class MainSystem():

    def __init__(self):
        self.nome = None
        self.cat_custo = None
        self.carroceria = None
        self.carro = None
        self.valor = None     

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
            texto com priemira letra em maiúscula
        ''' 
        while True:
            self.nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')  
            if self.nome.isalpha() and len(self.nome) >= 3:
                return self.nome.capitalize()
            else:
                print('Entrada invalida. Por favor digite 3 letras ou mais e use apenas letras ')

    def solicitar_cat_custo(self):
        self.cat_custo = input("Digite a categoria (ex: Premium ou Custo beneficio): ").strip().upper()

    def filtar_cat_custo(self):
        




#main
if __name__ == '__main__':
    sistema = MainSystem()
    sistema.solicitar_nome()
    print(sistema.nome)