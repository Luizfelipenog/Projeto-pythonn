import socket

def cliente(op, email, senha, nome, ano):
    ip = '10.180.42.15'
    port = 8000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    client_socket.send(op.encode())
    print('enviou',  op, 'de cliente...')
    print(client_socket.recv(1024).decode())

    client_socket.send(email.encode())
    print('enviou ', email, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(senha.encode())
    print('enviou', senha, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(nome.encode())
    print('enviou', nome, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    client_socket.send(ano.encode())
    print('enviou', ano, 'Recebeu: ', end='')
    print(client_socket.recv(1024).decode())

    result = client_socket.recv(1024).decode()
    client_socket.close()
    return result
        