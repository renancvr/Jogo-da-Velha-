from socket import *

def checaVitoria(mensagem):
	if mensagem.count('vitoria') > 0:
		return True
def checaDerrota(mensagem):
	if mensagem.count('vitoria') > 0:
		return True
def checaEmpate(mensagem):
	if mensagem.count('-') == 0:
		return True

serverHost = 'localHost'
serverPort = 50007

sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.connect((serverHost,serverPort))
vitoria = False
derrota = False
empate = False
print('Digite "start" para jogar!')
while True:
	msg = input('Eu: ')
	sockobj.send(msg.encode())
	data = sockobj.recv(1024)
	print(data.decode())
	vitoria = checaVitoria(data.decode())
	if vitoria == True:
		print('VITORIA')
		break
	msg = 'sua vez'
	sockobj.send(msg.encode())
	data = sockobj.recv(1024)
	print(data.decode())
	derrota = checaDerrota(data.decode())
	if derrota == True:
		print('DERROTA')
		break
	if derrota == False and vitoria == False:
		empate = checaEmpate()
		if empate == True:
			print('VELHA')


sockobj.close()