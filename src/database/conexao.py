import sqlite3

#Conexão com Banco de dados
def criar_conexao():
    try:
        conexao = sqlite3.connect(r'src/database/cars.db')
        conexao.row_factory = sqlite3.Row
        return conexao
    except:
        print("Erro ao conectar ao banco")
        return None