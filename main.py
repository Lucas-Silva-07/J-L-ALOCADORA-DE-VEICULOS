def solicitar_nome():
    nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')
    return nome

def solicitar_classe_custo():
    classificacao_custo = int(input('Digite o numero referente a qual categoria de custo você prefere:\n'
                                    '0 - Categoria Premium\n1 - Categoria Custo Beneficio\n'))
    return classificacao_custo

def solicitar_categorias():
    categorias = int(input(f'Perfeito, {nome}. Digite o número referente à categoria de carro desejada:\n'
                            '0 - Hatchs\n1 - Sedans\n2 - Picapes\n3 - SUVs\n4 - Vans\n5 - Esportivos\n6 - Caminhões\n'))
    return categorias
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
def escolher_carro():
    if classificacao_custo == 0:
        carros_disponiveis = premium[categorias]
    else:
        carros_disponiveis = custo_beneficio[categorias]
    print('Carros disponiveis: ')
    for i, carro in enumerate(carros_disponiveis):
        print(f'{i} - {carro}')
    escolha = int(input('Escolha o número do carro desejado: '))
    return carros_disponiveis[escolha]
#main
nome = solicitar_nome()
classificacao_custo = solicitar_classe_custo()
categorias = solicitar_categorias()
carro = escolher_carro()
print(f'Você escolheu o carro {carro}')