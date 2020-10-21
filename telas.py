import os

def tela_inicial():	
	tela = '''\
«««««|\033[1mSistema de Gestão Financeira\033[0m|»»»»»

 1 » Cadastros
 2 » Lançamentos
 3 » Relátorios
 0 « Sair
 '''
	print(tela)

def tela_cadastros():	
	
	tela = '''\
«««««|\033[1mCadastros\033[0m|»»»»»

 1 » Proventos e/ou Serviços Prestados
 2 » Clientes
 3 » Despesas
 4 » Doações
 5 » Contas
 0 « Voltar
 '''
	print(tela)

def tela_lancamentos():	
	
	tela = '''\
«««««|\033[1mLançamentos\033[0m|»»»»»

 1 » Proventos
 2 » Pagamentos de Clientes
 3 » Doações a Entregar
 4 » Despesas
 5 » Transferência de Valores entre Contas
 0 « Voltar
 '''
	print(tela)
