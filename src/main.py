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
        try:
            classificacao_custo = int(input('Digite o número referente a qual categoria de custo você prefere:\n'
                                             '0 - Categoria Premium\n1 - Categoria Custo Beneficio\n'))
            if classificacao_custo in [0,1]:
                return classificacao_custo
            else:
                print('Numero invalido, digite apenas números da lista.\n')
        except ValueError:
            print('Por favor, digite apenas números.\n')


def solicitar_categorias():
    while True:   
        try:
            categorias = int(input(f'Perfeito, {nome}. Digite o número referente à categoria de carro desejada:\n'
                                    '0 - Hatchs\n1 - Sedans\n2 - Picapes\n3 - SUVs\n4 - Vans\n5 - Esportivos\n6 - Caminhões\n'))
            if categorias in range(7):
                return categorias
            else:
                print('Digite apenas números da lista.\n')
        except ValueError:
            print('Por favor, digite apenas números.\n')
    
    
def escolher_carro():
    while True:
        try:        
            if classificacao_custo == 0:
                carros_disponiveis = premium[categorias]
            else:
                carros_disponiveis = custo_beneficio[categorias]
            print('Carros disponiveis: ')
            for i, carro in enumerate(carros_disponiveis):
                print(f'{i} - {carro}')
            escolha = int(input('Escolha o número do carro desejado: '))
            if escolha in range(i+1):
                return carros_disponiveis[escolha]
            else:
                print('Escolha apenas números da lista.\n ')
        except ValueError:
            print('Digite apenas números\n')
    
    
#main
nome = solicitar_nome()
classificacao_custo = solicitar_classe_custo()
categorias = solicitar_categorias()
carro = escolher_carro()
print(f'Você escolheu o carro {carro}')