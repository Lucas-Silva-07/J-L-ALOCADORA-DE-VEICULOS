#input handler
def pedir_nome():
    """
        Solicita que o usuário insira seu nome, valida a entrada e retorna o nome em maiúscula.\n
        A função irá imprimir uma mensagem de orientação e ficara em looping em caso de entradas indesejadas.
    """
    while True:
        nome = input('Olá, seja bem vindo a J & L ALOCADORA DE VEICULOS. Por favor insira seu nome para continuarmos com o atendimento. ')  
        if nome.isalpha() and len(nome) >= 3:
            nome = nome.capitalize()
            return nome
        else:
            print('Entrada invalida. Por favor digite 3 letras ou mais e use apenas letras.')
 
def pedir_categoria_custo():
    """
    Solicita ao usuário o nome da categoria de custo ele deseja e guarda em maiúscula..
    """ 
    cat_custo = input("Digite a categoria (ex: Premium ou Custo beneficio): ").strip().upper()
    return cat_custo