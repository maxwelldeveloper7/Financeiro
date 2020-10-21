# conding: utf-8
from telas import *
import os

opcoes = [0, 1, 2, 3]

msg_entrada = "\nEscolha uma opção: "
msg_erro = "\033[1m\033[31mOpção inválida!\033[0m" + msg_entrada
mensagem = msg_entrada

while True:
	os.system('clear') or None
	tela_inicial()
	try:
		opcao = int(input(mensagem))
	except ValueError:
		opcao = -1
	
	if opcao in opcoes:
		mensagem = msg_entrada
		
		if opcao == 0:
			break
		
		if opcao == 1:
			opcoes_1 = [0, 1, 2, 3, 4, 5]
			while True:
				os.system('clear') or None
				tela_cadastros()
				try:
					op1 = int(input(mensagem))
				except ValueError:
					op1 = -1
		
				if op1 in opcoes_1:
					mensagem = msg_entrada
					if op1 == 0:
						break
				else:
					mensagem = msg_erro
		
		if opcao == 2:
			opcoes_2 = [0, 1, 2, 3, 4, 5]
			while True:
				os.system('clear') or None
				tela_lancamentos()
				try:
					op2 = int(input(mensagem))
				except ValueError:
					op2 = -1
		
				if op2 in opcoes_2:
					mensagem = msg_entrada
					if op2 == 0:
						break
				else:
					mensagem = msg_erro
	else:
		mensagem = msg_erro
	
			
os.system('clear') or None
print("\nVocê saiu da aplicação, até mais!\n")
