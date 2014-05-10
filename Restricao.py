from ElementoDominio import *
'''
Classe que representa uma restricao

propriedades: 
->escopo eh um set de variaveis(objetos da classe variavel)
que fazem parte da restricao.
-> funcaorestricao eh uma funcao que recebe
como argumentos elementos do dominio das variaveis
do escopo da restricao e retorna True se a restricao eh
satisfeita ou False caso contrario 

'''

class Restricao:
	def __init__(self, escopo, funcaorestricao):
		if type(escopo) is not set: raise ValueError('argumento escopo deve ser set')
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
		return sorted(args, key=ElementoDominio.getOrdem)

	def chamafuncaorestricao(self, args):
		args = self._ordenaArgumentos(args)
		return self.funcaorestricao(*args)

	def __eq__(self, other):
		return self.funcaorestricao == other.funcaorestricao and self.escopo == other.escopo

	def __hash__(self):
		return hash(str(self))

	def __str__(self):
		return self.funcaorestricao.__name__

	def __repr__(self):
		return self.__str__()