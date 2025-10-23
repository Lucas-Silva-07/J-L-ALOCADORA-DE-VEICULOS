from .conexao import executar_consulta

def listar_carroceria_por_categoria(cat_custo):
    """
    Executa consulta no banco de dados para listar tipos de carroceria
    com base na categoria de custo (self.cat_custo).
    """
    query = "SELECT DISTINCT Cat_Carro FROM CARROSS WHERE Cat_Custo = ?"
    tipos = executar_consulta(query, (cat_custo,))
    print(f"\nTipos disponíveis na categoria {cat_custo}:")
    for tipo in tipos:
        print(f"- {tipo['Cat_Carro']}")

def listar_carros_por_carroceria(cat_custo, carroceria):
    """
    Executa consulta no banco de dados para listar os carros com base na carroceria(self.carroceria) e categoria de custo(self.custo).
    """
    query = "SELECT * FROM CARROSS WHERE Cat_Custo = ? AND Cat_Carro = ?"
    carros = executar_consulta(query,(cat_custo, carroceria,))
    print(f"\nModelos encontrados ({cat_custo} > {carroceria}):")
    for carro in carros:
        print(f"- {carro['Nome']}")

def veiculo_valor_escolhido(cat_custo, carroceria, carro):
    """
    Executa consulta no banco de dados para pegar o valor do veículo com baser a categoria de custo(self.cat_custo), na carroceria(self.carroceria) e no veículo escolhido(self.carro).
    """
    query = "SELECT * FROM CARROSS WHERE Cat_Custo = ? AND Cat_Carro = ? AND Nome = ?"
    valor = executar_consulta(query,(cat_custo, carroceria, carro,))
    return valor[0][4]