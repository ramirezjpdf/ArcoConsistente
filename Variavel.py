class Variavel(object):
	def __init__(self, ordem, **kwargs):
		self.ordem = ordem
		self.dominio = []
		self.__dict__.update(kwargs)


	def adicionaValor(self, valorDominio):
		self.dominio.append(valorDominio)

	def __eq__(self, other):
		selfAux = dict(self.__dict__)
		otherAux = dict(self.__dict__)
		del selfAux['dominio']
		del otherAux['dominio']
		return selfAux == otherAux

	def __hash__(self):
		selfAux = dict(self.__dict__)
		del selfAux['dominio']
		return hash(str(selfAux))