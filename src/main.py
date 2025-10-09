carros = [  ('PREMIUM','HATCHS','HONDA CITY', 55000),
            ('PREMIUM','HATCHS','AUDI A3', 60000),
            ('PREMIUM','HATCHS','BMW 118i', 65000),
            ('PREMIUM','HATCHS','FORD FOCUS ST', 58000),
            ('PREMIUM','SEDANS','HONDA CIVIC TOURING', 60000),
            ('PREMIUM','SEDANS','TOYOTA COROLLA ALTIS', 58000),
            ('PREMIUM','SEDANS','AUDI A5', 65000),
            ('PREMIUM','SEDANS','BMW 320i', 62000),
            ('PREMIUM','PICAPES','TOYOTA HILUX', 65000),
            ('PREMIUM','PICAPES','MITSUBISHI L200', 62000),
            ('PREMIUM','PICAPES','FIAT TORO', 57000),
            ('PREMIUM','PICAPES','CHEVROLET S10', 59000),
            ('PREMIUM','SUVS','BMW X1', 68000),
            ('PREMIUM','SUVS','VOLVO XC40', 70000),
            ('PREMIUM','SUVS','AUDI Q3', 66000),
            ('PREMIUM','SUVS','VOLKSWAGEN TIGUAN', 64000),
            ('PREMIUM','VANS','MERCEDES VITO', 75000),
            ('PREMIUM','VANS','HYUNDAI STARIA', 72000),
            ('PREMIUM','ESPORTIVOS','BMW M5', 90000),
            ('PREMIUM','ESPORTIVOS','PORSHE CAYMAN', 85000),
            ('PREMIUM','ESPORTIVOS','AUDI RS6', 95000),
            ('PREMIUM','ESPORTIVOS','MERCEDES CLA AMG 45', 88000),
            ('PREMIUM','CAMINHOES','VOLVO VM 270', 110000),
            ('PREMIUM','CAMINHOES','MERCEDES MB 4144', 120000),
            ('CUSTO BENEFICIO','HATCHS','VOLKSWAGEN POLO', 35000),
            ('CUSTO BENEFICIO','HATCHS','HYUNDAI HB20', 33000),
            ('CUSTO BENEFICIO','HATCHS','FORD KA', 32000),
            ('CUSTO BENEFICIO','SEDANS','HONDA CITY SEDAN', 40000),
            ('CUSTO BENEFICIO','SEDANS','VOLKSWAGEN VOYAGE', 36000),
            ('CUSTO BENEFICIO','SEDANS','FORD FIESTA', 34000),
            ('CUSTO BENEFICIO','SEDANS','HYUNDAI HB20S', 37000),
            ('CUSTO BENEFICIO','PICAPES','VOLKSWAGEN SAVEIRO', 38000),
            ('CUSTO BENEFICIO','PICAPES','FIAT STRADA', 36000),
            ('CUSTO BENEFICIO','PICAPES','CHEVROLET MONTANA', 37000),
            ('CUSTO BENEFICIO','PICAPES','FORD COURIER', 35000),
            ('CUSTO BENEFICIO','SUVS','HONDA HR-V', 42000),
            ('CUSTO BENEFICIO','SUVS','HYUNDAI IX35', 40000),
            ('CUSTO BENEFICIO','SUVS','CHEVROLET CAPTIVA', 42000),
            ('CUSTO BENEFICIO','SUVS','TOYOTA COROLLA CROSS XR', 41000),
            ('CUSTO BENEFICIO','VANS','VOLKSWAGEN CADDY', 45000),
            ('CUSTO BENEFICIO','VANS','MERCEDES SPRINTER', 48000),
            ('CUSTO BENEFICIO','VANS','RENAUT MASTER', 46000),
            ('CUSTO BENEFICIO','ESPORTIVOS','MITSUBISHI LANCER EVO X', 55000),
            ('CUSTO BENEFICIO','ESPORTIVOS','SUBARU IMPREZA WRX STI', 54000),
            ('CUSTO BENEFICIO','ESPORTIVOS','AUDI RS4', 58000),
            ('CUSTO BENEFICIO','ESPORTIVOS','BMW M135i', 56000),
            ('CUSTO BENEFICIO','CAMINHOES','HYUNDAI HR', 58000),
            ('CUSTO BENEFICIO','CAMINHOES','MERCEDES SPRINTER TRUCK', 62000)    ]


def sair_programa():
    '''
    Encerra o programa.

    Parameters
    ----------
    Sem parâmetros

    Returns
    -------
    print
        'Saindo do programa...'
    exit()
    '''
    print('Saindo do programa...')
    exit()


def solicitar_nome():
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
        nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')  
        if nome.isalpha() and len(nome) >= 3:
            return nome.capitalize()
        else:
            print('Entrada invalida. Por favor digite 3 letras ou mais e use apenas letras ')
            

def validar_entradas(indice_escolhido, tamanho_lista):
    '''
    Valida a entrada do usuário para índices e verifica se a entrada está dentro de um intervalo válido.
    Em caso de entrada inválida a função retornará como None.

    Parameters
    ----------
    int
       indice escolhido pelo usuário  
    int
        tamanho da lista
    Returns
    -------
    int
        indice escolhido pelo usuario

    None 
        (em caso de entrada inválida retornará None)
    ''' 
    
    try:
        indice_escolhido = int(indice_escolhido)
        if indice_escolhido in range(tamanho_lista):
            return indice_escolhido
        else:
            print('Digite apenas números da lista.\n')
            return None
    except ValueError:
        print('Por favor, digite apenas números.\n')
        return None


def solicitar_categorias():
    '''
    Solicita ao usuário que escolha uma categoria de carro em uma lista, valida a entrada e retorna a categoria selecionada.\n
    A função irá imprimir uma mensagem de orientação e ficara em looping em caso de entradas indesejadas.

    Parameters
    ----------
    Sem parâmetros

    Returns
    -------
    str
        categoria selecionada
    ''' 
    lista_categorias = ['HATCHS', 'SEDANS', 'PICAPES', 'SUVS', 'VANS', 'ESPORTIVOS', 'CAMINHOES']
    while True:   
        categorias = (input(f'Perfeito, {nome}. Digite o número referente à categoria de carro desejada:\n'
                                    '0 - Hatchs\n1 - Sedans\n2 - Picapes\n3 - SUVs\n4 - Vans\n5 - Esportivos\n6 - Caminhões\n7 - Sair\n'))
        categorias_validada = validar_entradas(categorias, 8)
        if categorias_validada is not None:
            if categorias_validada == 7:
                sair_programa()
            else:
                return lista_categorias[categorias_validada]


def solicitar_categoria_custo():
    '''
    Solicita que o usuário escolha uma categoria de custo, valida a entrada e retorna a categoria de custo selecionada.\n
    A função irá imprimir uma mensagem de orientação e ficara em looping em caso de entradas indesejadas.

    Parameters
    ----------
    Sem parâmetros

    Returns
    -------
    str
        categoria de custo selecionada
    ''' 
    while True:
        classificacao_custo = (input('Digite o número referente a qual categoria de custo você prefere:\n'
                                        '0 - Categoria Premium\n1 - Categoria Custo Beneficio\n2 - Sair\n'))
        classificacao_validada = validar_entradas(classificacao_custo, 3)
        if classificacao_validada is not None:
            if classificacao_validada == 2:
                sair_programa()
            elif classificacao_validada == 1:
                return 'CUSTO BENEFICIO'
            elif classificacao_validada == 0:
                return 'PREMIUM'


def filtrar_classe(carros, indice_classe, categorias):
    '''
    Filtra a lista de carros disponíveis com base na classe e categoria de carro selecionada.\
    Retorna uma lista com os carros e valores filtrados.

    Parameters
    ----------
    list
        tuple
            Categoria de custo, categoria do carro, carros, valor do carro
    
    str
        'CUSTO BENEFICIO', 'PREMIUM'

    str
        'HATCHS', 'SEDANS', 'PICAPES', 'SUVS', 'VANS', 'ESPORTIVOS', 'CAMINHOES'

    Returns
    -------
    list
        carros, valores
    ''' 
    lista_filtrada = [[carro, valor] for classe, categoria, carro, valor in carros if classe == indice_classe and categoria == categorias]
    return lista_filtrada


def escolher_carro():
    '''
    Solicita ao usuário que escolha um carro específico da lista filtrada e retorna o carro selecionado.

    Parameters
    ----------
    sem parâmetros
    
    Returns
    -------
    lista
        carro, valor
    '''
    while True:
        print('Carros disponiveis: ')
        indice_carros = []
        for i, carro in enumerate(carros_disponiveis):
            print(f'{i} - {carro[0]}')
            indice_carros.append(i)
        tamanho = len(indice_carros)
        indice_carros.append(tamanho)
        escolha = (input(f'{i+1} - SAIR\nEscolha o número do carro desejado: '))
        carro_escolhido = validar_entradas(escolha, i+2)
        if carro_escolhido is not None:
            if carro_escolhido == indice_carros[-1]:
                sair_programa()
            else:
                return carros_disponiveis[carro_escolhido]
   

#main
nome = solicitar_nome()
classe = solicitar_categoria_custo()
categorias = solicitar_categorias()
carros_disponiveis = filtrar_classe(carros, classe, categorias)
carro_escolhido = escolher_carro()
print(f'Você escolheu o carro {carro_escolhido[0]}\n'
      f'Valor do carro é de {carro_escolhido[1]}')
