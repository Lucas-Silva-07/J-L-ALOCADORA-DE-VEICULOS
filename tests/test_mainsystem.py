from src.database import repository
from src.models import input_handler

class MainSystem():

    def __init__(self):
        self.nome = input_handler.pedir_nome()
        self.cat_custo = input_handler.pedir_categoria_custo()
        self.carroceria = None
        self.carro = None
        self.valor = None
        self.conexao = None    
  
    def filtrar_carroceria(self):
        """
        Mostra uma lista de carrocerias com base a escolha da categoria de custo (self.cat_custo).
        """
        repository.listar_carroceria_por_categoria(self.cat_custo)
        self.carroceria = input(
            "\nDigite o tipo que deseja ver (ex: Esportivo): "
            ).strip().upper()
        
    def filtrar_carros(self):
        """
        Mostra uma lista de carros com base na escolha da  carroceria(self.carroceria) e categoria de custo (self.cat_custo).
        """
        repository.listar_carros_por_carroceria(self.cat_custo, self.carroceria)
        self.carro = input('\nDigite qual carro deseja: ').strip().upper()

    def carro_escolhido(self):
        '''
        Imprime mensagem personalizada com nome do usuário e mostra o veículo(self.carro) escolhido com seu valor(self.valor).
        '''
        self.valor = repository.veiculo_valor_escolhido(self.cat_custo, self.carroceria, self.carro)
        print(f'\n{self.nome} você escolheu o veículo {self.carro} da classe de custo {self.cat_custo} com o valor de R${self.valor:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.'))

#main
if __name__ == '__run__':
    sistema = MainSystem()
    sistema.solicitar_nome()
    sistema.solicitar_cat_custo()
    print(sistema.nome)