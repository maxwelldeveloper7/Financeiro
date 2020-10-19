# conding: utf-8
from telas import *
import os

opcao = -1
while opcao != 0:
	tela_inicial()
	try:
		opcao = int(input("Escolha uma opção: "))
		os.system('clear') or None
	except ValueError:
		
		print("Opção inválida!")
