from categoria import Categoria
from conta import Conta
from operacao import Operacao
from doacao import Doacao

class Registro():
    def __init__(self, data, historico,Categoria, Operacao, valor, Conta, 
        Docacao, id = 0):
        self.data = data
        self.historico = historico
        self.Categoria = Categoria
        self.Operacao = Operacao
        self.valor = valor
        self.Conta = Conta
        self.Doacao = Doacao
        self.id = id

categoria = Categoria("Salário", 1)
conta = Conta("Conta Corrente/Caixa", 1)
tipo_operacao = Operacao("Entrada", 1)
doacao = Doacao("Dízimo", 0.1, 1)

def teste():
    registro = Registro('02/02/2020', "Pagamento de Novembro",categoria,
        tipo_operacao, 1122.38, conta, doacao, 1)
    print("Id: " + str(registro.id))
    print("Data: " + registro.data)
    print("Histórico: " + registro.historico)
    print("Categoria: " + registro.Categoria.descricao)
    print("Operação: " + registro.Operacao.descricao)
    print("Valor: " + str(registro.valor))
    print("Conta: " + registro.Conta.descricao)
    percentual = doacao.percentual
    print("Doação: " + doacao.descricao +" "+ str(registro.valor * 
        percentual))

teste()