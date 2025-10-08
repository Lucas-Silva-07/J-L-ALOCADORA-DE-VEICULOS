import sqlite3

#Conexão com Banco de dados
def criar_conexao():
    conexao = sqlite3.connect('cars.db')
    conexao.row_factory = sqlite3.Row
    return conexao