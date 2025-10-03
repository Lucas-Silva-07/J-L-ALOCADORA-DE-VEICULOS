premium = [['HONDA CITY', 'AUDI A3', 'BMW 118i', 'FORD FOCUS ST'], 
           ['HONDA CIVIC TOURING', 'TOYOTA COROLLA ALTIS', 'AUDI A5', 'BMW 320i'],
           ['TOYOTA HILUX', 'MITSUBISHI L200', 'FIAT TORO', 'CHEVROLET S10'],
           ['BMW X1', 'VOLVO XC40', 'AUDI Q3', 'VOLKSWAGEN TIGUAN'],
           ['MERCEDES VITO', 'HYUNDAI STARIA'],
           ['BMW M5', 'PORSHE CAYMAN', 'AUDI RS6', 'MERCEDES CLA AMG 45'],
           ['VOLVO VM 270', 'MERCEDES MB 4144']]

custo_beneficio = [['VOLKSWAGEN POLO', 'HYUNDAI HB20', 'FORD KA'],
                   ['HONDA CITY', 'VOLKSWAGEN VOYAGE', 'FORD FIESTA', 'HYUNDAI HB20S'],
                   ['VOLKSWAGEN SAVEIRO', 'FIAT STRADA', 'CHEVROLET MONTANA', 'FORD COURIER'],
                   ['HONDA HR-V', 'HYUNDAI IX35', 'CHEVROLET CAPTIVA', 'TOYOTA COROLLA CROSS XR'],
                   ['VOLKSWAGEN CADDY', 'MERCEDES SPRINTER', 'RENAUT MASTER'],
                   ['MITSUBISHI LANCER EVO X', 'SUBARU IMPREZA WRX STI', 'AUDI RS4', 'BMW M135i'],
                   ['HYUNDAI HR', 'MERCEDES SPRINTER TRUCK']]

def sair_programa(sair):
    print('Saindo do programa...')
    exit()
    
def validar_entradas(x, y):
    try:
        x = int(x)
        if x in range(y):
            return x
        else:
            print('Digite apenas números da lista.\n')
            return None
    except ValueError:
        print('Por favor, digite apenas números.\n')
        return None

def solicitar_nome():
    nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')    
    while True:
        if nome:
            if nome.isalpha():
                nome = nome.capitalize()
                if len(nome) < 3:
                    nome = input('Entrada Invalida. Digite 3 letras ou mais. ')
                else:
                    return nome
            else:
                nome = input('Entrada Invalida. Digite apenas letras. ')  
        else:
            nome = input('Por favor, preencha o campo vazio ')


def solicitar_classe_custo():
    while True:
        classificacao_custo = (input('Digite o número referente a qual categoria de custo você prefere:\n'
                                        '0 - Categoria Premium\n1 - Categoria Custo Beneficio\n2 - Sair\n'))
        classificacao_validada = validar_entradas(classificacao_custo, 3)
        if classificacao_validada is not None:
            if classificacao_validada == 2:
                sair_programa(2)
            else:
                return classificacao_validada
        

def solicitar_categorias():
    while True:   
        categorias = (input('Perfeito, {nome}. Digite o número referente à categoria de carro desejada:\n'
                                    '0 - Hatchs\n1 - Sedans\n2 - Picapes\n3 - SUVs\n4 - Vans\n5 - Esportivos\n6 - Caminhões\n7 - Sair\n'))
        categorias_validada = validar_entradas(categorias, 8)
        if categorias_validada is not None:
            if categorias_validada == 7:
                sair_programa(7)
            else:
                return categorias_validada
    
    
def escolher_carro():
    while True:
        if classificacao_custo == 0:
            carros_disponiveis = premium[categorias]
        else:
            carros_disponiveis = custo_beneficio[categorias]
        print('Carros disponiveis: ')
        indice_carros = []
        for i, carro in enumerate(carros_disponiveis):
            print(f'{i} - {carro}')
            indice_carros.append(i)
        tamanho = len(indice_carros)
        indice_carros.append(tamanho)
        escolha = (input(f'{i+1} - SAIR\nEscolha o número do carro desejado: '))
        carro_escolhido = validar_entradas(escolha, i+2)
        if carro_escolhido is not None:
            if carro_escolhido == indice_carros[-1]:
                sair_programa(indice_carros[-1])
            else:
                return carros_disponiveis[carro_escolhido]
    
    
#main
nome = solicitar_nome()
classificacao_custo = solicitar_classe_custo()
categorias = solicitar_categorias()
carro = escolher_carro()
print(f'Você escolheu o carro {carro}')