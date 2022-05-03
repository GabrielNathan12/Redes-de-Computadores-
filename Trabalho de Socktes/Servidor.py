#Gabriel Nathan Almeida Silva , 22A
#Vitoria Alvim da Silva , 14A

import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
Servidor_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Criacao do Servidor
addr = (HOST, PORT) #Endereco
Servidor_UDP.bind((HOST, PORT))

print("Conectando ao Servidor")

while True:
    # recebe a mensagem do servidor, buffer de tamanho 1024
    data, addr = Servidor_UDP.recvfrom(1024)
    print(str(data))
    message = "Conectado"
    Servidor_UDP.sendto(message.encode("utf-8"),addr)
print("Terminou a Conexao")
Servidor_UDP.close();
