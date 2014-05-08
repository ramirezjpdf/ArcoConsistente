'''
Classe que representa uma restricao

propriedades: 
->escopo eh uma lista de strings com as variaveis
que fazem parte da restricao.
-> funcaorestricao eh uma funcao que recebe
como argumentos elementos do dominio das variaveis
do escopo da restricao e retorna True se a restricao eh
satisfeita ou False caso contrario 

'''

class Restricao:
	def __init__(self, escopo, funcaorestricao):
		self.escopo = escopo
		self.funcaorestricao = funcaorestricao

	def pertenceEscopo(self, variavel):
		return variavel in self.escopo