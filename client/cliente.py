import socket

def cliente(op, email, senha, nome, ano):
    ip = 'localhost'
    port = 8000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    client_socket.send(op.encode())
    print('EnviouOp: ',  op, 'de cliente...Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(email.encode())
    print('EnviouEmail: ', email, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(senha.encode())
    print('EnviouSenha: ', senha, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(nome.encode())
    print('EnviouNome: ', nome, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(ano.encode())
    print('EnviouAno: ', ano, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    result = client_socket.recv(1024).decode()
    client_socket.close()
    return result
        