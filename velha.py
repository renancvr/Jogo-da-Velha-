from socket import *
from random import randint

def atualizaTabuleiro(jogada):
	arq = open('jogo.txt','r')
	l = []
	word = ''
	tabueiro = arq.read()
	for i in tabueiro:
		l.append(i)
	arq.close()
	if jogada == '1-1' and l[0] == '-':
		l[0] = 'X'
	elif jogada == '1-2' and l[1] == '-':
		l[1] = 'X'
	elif jogada == '1-3' and l[2] == '-':
		l[2] = 'X'
	elif jogada == '2-1' and l[4] == '-':
		l[4] = 'X'
	elif jogada == '2-2' and l[5] == '-':
		l[5] = 'X'
	elif jogada == '2-3' and l[6] == '-':
		l[6] = 'X'
	elif jogada == '3-1' and l[8] == '-':
		l[8] = 'X'
	elif jogada == '3-2' and l[9] == '-':
		l[9] = 'X'
	elif jogada == '3-3' and l[10] == '-':
		l[10] = 'X'
	else:
		return 'jogada invalida'
	word = word.join(l)
	arq = open('jogo.txt','w')
	arq.write(word)
	arq.close()
	aux = checaVitoria()
	return 'Jogador: \n' + word + '\n\n' + aux + '\n\n'
def checaVitoria():
	arq = open('jogo.txt','r')
	l = []
	tabuleiro = arq.read()
	for i in tabuleiro:
		l.append(i)
	arq.close()
	if (l[0] == l[1] == l[2] and l[0] !='-') or (l[4] == l[5] == l[6] and l[4] != '-') or (l[8] == l[9] == l[10] and l[8] != '-') or (l[0] == l[4] == l[8] and l[0] != '-') or (l[1] == l[5] == l[9] and l[1] != '-') or (l[2] == l[6] == l[10] and l[2] != '-') or (l[0] == l[5] == l[10] and l[0] != '-') or (l[2] == l[5] == l[8] and l[2] != '-') :
		print('teste')
		return 'vitoria'
	else:
		return ''
def limpaTabuleiro():
	arq = open('jogo.txt','w')
	arq.write('---\n---\n---\n')
	arq.close()
	arq2 = open('invalidas.txt','w')
	arq2.write('')
	arq2.close()
def inicia():
	arq = open('jogo.txt','r')
	tabuleiro = arq.read()
	word = ''
	l = []
	for i in tabuleiro:
		l.append(i)
	return word.join(l)
def jogadaServer():
	possibilidades = ['1-1','1-2','1-3','2-1','2-2','2-3','3-1','3-2','3-3']
	aux = randint(0,len(possibilidades)-1)
	jogada_server = possibilidades[aux]
	return jogada_server
def jogadasInvalidas(jogada):
	inv = open('invalidas.txt','r')
	conteudo = inv.readlines()
	conteudo.append(jogada + '\n')
	inv = open('invalidas.txt','w')
	inv.writelines(conteudo)
	inv.close()

def atualizaTabuleiroServer(jogada):
	arq = open('jogo.txt','r')
	l = []
	word = ''
	tabueiro = arq.read()
	for i in tabueiro:
		l.append(i)
	arq.close()
	if jogada == '1-1' and l[0] == '-':
		l[0] = 'O'
	elif jogada == '1-2' and l[1] == '-':
		l[1] = 'O'
	elif jogada == '1-3' and l[2] == '-':
		l[2] = 'O'
	elif jogada == '2-1' and l[4] == '-':
		l[4] = 'O'
	elif jogada == '2-2' and l[5] == '-':
		l[5] = 'O'
	elif jogada == '2-3' and l[6] == '-':
		l[6] = 'O'
	elif jogada == '3-1' and l[8] == '-':
		l[8] = 'O'
	elif jogada == '3-2' and l[9] == '-':
		l[9] = 'O'
	elif jogada == '3-3' and l[10] == '-':
		l[10] = 'O'
	else:
		return 'jogada invalida'
	word = word.join(l)
	arq = open('jogo.txt','w')
	arq.write(word)
	arq.close()
	aux = checaVitoria()
	return 'Server: \n' + word + '\n\n' + aux + '\n\n'