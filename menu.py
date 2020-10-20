# conding: utf-8
from telas import *
import os

opcao = -1
while True:
	#variável que será usada para controlar o loop interno dos menus
	op = -1
	tela_inicial()
	
	try:
		opcao = int(input("Escolha uma opção: "))
		os.system('clear') or None
	except ValueError:
		print("\nOpção inválida!\n")		
	
	if opcao == 0:
		break
	
	if opcao == 1:
		while True:
			os.system('clear') or None
			tela_cadastros()
			try:
				op = int(input("Escolha uma opção: "))
			except ValueError:
				print("\nOpção inválida!\n")
			if op == 0:
				os.system('clear') or None
				break
	
	if opcao == 2:
		while True:
			os.system('clear') or None
			tela_lancamentos()
			try:
				op = int(input("Escolha uma opção: "))
			except ValueError:
				print("\nOpção inválida!\n")
			if op == 0:
				os.system('clear') or None
				break
			

print("Você saiu da aplicação, até mais!")
