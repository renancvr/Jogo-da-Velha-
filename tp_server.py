from socket import *
from random import randint
from velha import *


meuHost = ''
minhaPort = 50007
sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((meuHost,minhaPort))
sockobj.listen(1)

while True:
	print('Servidor online')
	conexao, endereco = sockobj.accept()
	print('Server conectado por: ',endereco)
	while True:
		data = conexao.recv(1024)
		msg = data.decode()
		print('Msg: ', data.decode())
		if data.decode() == 'start':
			limpaTabuleiro()
			flagInicio = True
			resposta = inicia()
		elif msg == '1-1' or msg == '1-2' or msg == '1-3' or msg == '2-1' or msg == '2-2' or msg == '2-3' or msg == '3-1' or msg == '3-2' or msg == '3-3':
			jogadasInvalidas(msg)
			resposta = atualizaTabuleiro(msg)
		elif msg == 'sua vez':
			if flagInicio == True:
				resposta = 'Comece o jogo!\n'
				flagInicio = False
			else:
				jogada = jogadaServer()
				inv = open('invalidas.txt','r')
				invalidas = inv.readlines()
				l = []
				for i in invalidas:
					l.append(i)
				inv.close()
				while l.count(jogada)>0 or l.count(jogada+'\n')>0:
					jogada = jogadaServer()
				jogadasInvalidas(jogada)
				resposta = atualizaTabuleiroServer(jogada)
		elif msg == 'close':
			limpaTabuleiro()
			break
		elif not msg: break
		else: 
			resposta = 'comando invalido'

		conexao.send(resposta.encode())
	print('Finalizando conexao do cliente',endereco)
	conexao.close()