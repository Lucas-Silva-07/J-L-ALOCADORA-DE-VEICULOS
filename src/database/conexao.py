from src.config import DB_PATH
import sqlite3

def executar_consulta(query, params=()):
    """
    Executa uma consulta SQL de forma segura usando 'with'.
    Fecha automaticamente a conexão, mesmo em caso de erro.

    Parameters
    ----------
    query : str
        Comando SQL (SELECT, INSERT, UPDATE, etc.)
    params : tuple
        Parâmetros a serem passados para o comando SQL

    Returns
    -------
    list[sqlite3.Row]
        Lista de linhas retornadas (no caso de SELECT),
        ou uma lista vazia em caso de erro.
    """
    try:
        with sqlite3.connect(DB_PATH) as conexao:
            conexao.row_factory = sqlite3.Row
            cursor = conexao.cursor()
            cursor.execute(query, params)
            # Retorna resultados apenas se for um SELECT
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            conexao.commit()
            return []
    except sqlite3.Error as erro:
        print(f"Erro ao executar consulta: {erro}")
        return []
