import os

def tela_inicial():	
	
	tela = '''\
«««««|Sistema de Gestão Financeira|»»»»»

 1 » Cadastros
 2 » Lançamentos
 3 » Relátorios
 0 « Sair
 '''
	print(tela)

def tela_cadastros():	
	
	tela = '''\
«««««|Cadastros|»»»»»

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
«««««|Gegistro de Lançamentos|»»»»»

 1 » Proventos a Receber
 2 » Proventos Recebidos
 3 » Pagamentos de Clientes a Receber
 4 » Pagamentos de Clientes Recebidos
 5 » Dízimos e Ofertas a Devolver
 6 » Despesas a Pagar
 7 » Despesas pagas
 8 » Transferência de Valores entre Contas
 0 « Voltar
 '''
	print(tela)
