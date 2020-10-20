# conding: utf-8
from telas import *
import os

opcoes = [0, 1, 2, 3]

mensagem = "\nEscolha uma opção: "

while True:
	os.system('clear') or None
	tela_inicial()
	try:
		opcao = int(input(mensagem))
	except ValueError:
		opcao = -1
	
	if opcao in opcoes:
		mensagem = "\nEscolha uma opção: "
		
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
					mensagem = "\nEscolha uma opção: "
					if op1 == 0:
						break
				else:
					mensagem = "Opção inválida!\nEscolha uma opção: "
		
		if opcao == 2:
			opcoes_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
			while True:
				os.system('clear') or None
				tela_lancamentos()
				try:
					op2 = int(input(mensagem))
				except ValueError:
					op2 = -1
		
				if op2 in opcoes_2:
					mensagem = "\nEscolha uma opção: "
					if op2 == 0:
						break
				else:
					mensagem = "Opção inválida!\nEscolha uma opção: "
	else:
		mensagem = "Opção inválida!\nEscolha uma opção: "
	
			
os.system('clear') or None
print("\nVocê saiu da aplicação, até mais!")
