import os

def inicial():	
	tela = '''\
«««««|\033[1mSistema de Gestão Financeira\033[0m|»»»»»

 1 » Cadastros
 2 » Histórico
 3 » Relátorios
 0 « Sair
 '''
	print(tela)

def cadastros():	
	
	tela = '''\
«««««|\033[1mCadastros\033[0m|»»»»»

 1 » Categorias
 2 » Clientes
 3 » Despesas
 4 » Doações
 5 » Contas
 0 « Voltar
 '''
	print(tela)

def movimento():	
	
	tela = '''\
«««««|\033[1mHistórico\033[0m|»»»»»

 1 » Proventos
 2 » Pagamentos de Clientes
 3 » Doações a Entregar
 4 » Despesas
 5 » Transferência de Valores entre Contas
 0 « Voltar
 '''
	print(tela)
