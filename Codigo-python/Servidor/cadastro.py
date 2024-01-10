from conexao import criar_conexao, execute_query, read_query

class Cadastro:
    __slots__ = ['_cursor', '_sql', '_pw']

    def __init__(self):
        self._pw = '23ropo2New'
        self._cursor = criar_conexao('localhost', 'root', 'suasaude', self._pw)
        self._sql = """CREATE TABLE IF NOT EXISTS usuarios(email VARCHAR(64) PRIMARY KEY, username VARCHAR(40) NOT NULL,
        senha VARCHAR(32) NOT NULL, ano integer NOT NULL, UNIQUE (username));"""
        execute_query(self._cursor, self._sql)
    

    def cadastra(self, email, username, senha, ano):
        existe = self.busca(email)
        existe = self.busca(username)
        if (existe == None):
            print('cadastra: email, ', email)
            self._cursor = criar_conexao('localhost', 'root', 'suasaude', self._pw)
            execute_query(self._cursor, 'INSERT INTO usuarios(email, username, senha, ano) VALUES (%s,%s,MD5(%s),%s)', (email, username, senha, ano))
            return True
        else:
            print('cadastra: email, ', email)
            return False

    def busca(self, username):
        self._cursor = criar_conexao('localhost', 'root', 'suasaude', self._pw)
        user = read_query(self._cursor, 'SELECT * FROM usuarios WHERE email = %s OR username = %s', (username, username))
        return user
    
    def login(self, email, senha):
        self._cursor = criar_conexao('localhost', 'root', 'suasaude', self._pw)
        user = read_query(self._cursor, 'SELECT * FROM usuarios WHERE email = %s AND senha = MD5 (%s)', (email, senha))
        if(user):
            return True
        else:
            return False
         