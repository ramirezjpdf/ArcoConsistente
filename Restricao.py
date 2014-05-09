from ValorDominio import *
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

	'''
	params: args lista de argumentos para serem passados
	para a funcaorestricao depois de serem ordenados

	return: lista de argumentos devidamente ordenados
	'''
	def _ordenaArgumentos(self, args):
		return sorted(args, key=ValorDominio.getOrdem)

	def chamafuncaorestricao(self, args):
		self._ordenaArgumentos(args)
		return self.funcaorestricao(*args)

	def __eq__(self, other):
		return self.funcaorestricao == other.funcaorestricao

	def __hash__(self):
		return hash(str(self))