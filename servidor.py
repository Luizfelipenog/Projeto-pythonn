import threading
import socket 
from cadastro import Cadastro

class UsuarioThread(threading.Thread):
    def __init__(self, userAddress, userSocket, sinc):
        threading.Thread.__init__(self)
        self.user_socket = userSocket
        print('Nova conexao: ', userAddress)
        self.cad = Cadastro()
        self.sinc = sinc
    
    def run(self):
        result = ''
        op, email, senha, nome, ano = self.user_socket.recv(1024).decode()
        print('op:', op)
        if op == '2':#cadastro
            self.sinc.acquire()
            cadastrou = self.cad.cadastra(email, nome, senha, int(ano))
            print('cadastro em andamento...')
            self.sinc.release()
            if cadastrou:
                result = 'True'
                print('valores inseridos!', result)
            else:
                result = 'False'
                print('nao cadastrou')
            
        if op == '1':#login
            achou = self.cad.login(email, senha)
            if achou:
                result = 'True'
            else:
                result = 'False'
            print('login feito!', result)
        print('fim do run!')
        self.user_socket.send(result.encode())

if __name__=='__main__':
    localhost = 'localhost'
    port = 8000
    sinc = threading.Lock()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((localhost, port))
    print('Servidor Iniciado')
    print('Aguardando conexao...')
    while True:
        try:
            server_socket.listen(1)
            userSocket, userAddress = server_socket.accept()
            Newthread = UsuarioThread(userAddress, userSocket, sinc)
            Newthread.start()
        except:
            print('Erro')
            break
        

