import mysql.connector as mysql
from mysql.connector import Error

def criar_conexao(host_name, user_name, db_name, user_senha):
    conexao = None
    try:
        conexao = mysql.connect( 
            host = host_name, 
            db = db_name,
            user = user_name,
            passwd = user_senha
    )
    except Error as err:
        print(f"Error:'{err}'")
    
    return conexao

def execute_query(conexao, query, var=None):
    cursor = conexao.cursor()
    try:
        cursor.execute(query, var)
        conexao.commit()
        conexao.close()
    except Error as err:
        print(f"Error:'{err}'")

def read_query(conexao, query, var=None):
    cursor = conexao.cursor()
    result = None
    try:
        cursor.execute(query, var)
        result = cursor.fetchall()
        conexao.close()
        return result
    except Error as err:
        print(f"Error:'{err}'")
