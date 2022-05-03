#Gabriel Nathan Almeida Silva , 22A
#Vitoria Alvim da Silva , 14A

import socket

socket.setdefaulttimeout(0.25) #timeout esteja ajustado para 250 ms
contTentativas = 0 # Contagem de Tentativas de Envio
ping = 0 #Contagem de Ping com sucesso
packetloss = 0 #Pacotes Perdidos
somaping = 0 #Soma dos Pacostes enviados
Host = '192.168.1.1' # Ip do Professor , caso queira testar no servidor local e apenas trocar para localhost
Port = 5002 # Posta a Ser utilisada
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ('192.168.1.1',5002) #Endereco
udp.sendto("Ping".encode(),address)
udp.connect((Host, Port)) #Fazendo a Conexao d

#Funcao para enviar a mensagem para o servidor
def enviar():
    while True:
        mensagem = "Ping"
        # da encode na mensagem do cliente e a envia ao servidor
        udp.sendto(mensagem.encode())
        if mensagem == "EXIT":
            print ("VocÃª desconectou!")
            break
    return

def PING(sock, umaMensagem):
    #Envia um Ping para o servidor , se o servidor nao responder um Pong quer dizer que o pacote foi perdido
    if 'PING :' in umaMensagem:
        codigo_ping = umaMensagem.split('PING :')[-1]
        resposta_pong = 'PONG :{}'.format(codigo_ping)
        envia_comando(sock, resposta_pong)

#Funcao para receber a resposta do Servidor
def receber():
    while True:
        #recebe a mensagem do servidor, buffer de tamanho 1024
        mensagem = udp.recvfrom(1024)
        #Se a mensagem do servidor for 'EXIT' significa que este mesmo cliente encerrou
        # este programa, entao encerramos essa thread e
        # finalizamos o socket
        if mensagem.decode() == "EXIT":
            udp.close()
            break
        #caso contrario continuaremos a execucao normal da funcao e imprimimos a mensagem
        elif mensagem:
            print('\n', mensagem.decode(), '\n')
    return

import time

#Funcao Principal
while(contTentativas  < 20):
    contTentativas += 1
    inicio = ((time.time()) / 1000)  # divisao para utilizacao do tempo em ms
    udp.sendto("Ping".encode(), address)
    #Tratamento de Execao se caso o tempo estorar ele sera perdido
    try:
        mensagem, adrs = udp.recvfrom(1024)
        print("Pacote Enviado ", inicio)
        fim = ((time.time()) / 1000)  # divisao para utilizacao do tempo em ms
        ping = ping + 1
    except Exception as e:
        fim = ((time.time()) / 1000) #divisao para utilizacao do tempo em ms
        packetloss = packetloss + 1
        print("Pacote Foi Perdido")
    somaping += (fim-inicio)
    print("O tempo de envio total do Pacote foi de : ",round(fim- inicio) ,"sec" )

udp.close()
print("o tempo total foi de : ",somaping)

if ping!=0:
 print("o tempo medio : ",(somaping/ping))
print("Pacotes Enviados : ",ping)
print("Pacotes Perdidos : ", packetloss)