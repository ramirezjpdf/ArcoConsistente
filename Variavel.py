class Variavel(object):
	def __init__(self, variavelId, ordem, **kwargs):
		self.variavelId = variavelId
		self.ordem = ordem
		self.dominio = []
		self.__dict__.update(kwargs)


	def adicionaElemento(self, elementoDominio):
		self.dominio.append(elementoDominio)

	def __eq__(self, other):
		selfAux = dict(self.__dict__)
		otherAux = dict(other.__dict__)
		del selfAux['dominio']
		del otherAux['dominio']
		return selfAux == otherAux

	def __hash__(self):
		selfAux = dict(self.__dict__)
		del selfAux['dominio']
		return hash(str(selfAux))

	def __str__(self):
		aux = dict(self.__dict__)
		del aux['dominio']
		del aux['ordem']
		ret = '< '
		for key, value in aux.iteritems():
			ret += key + ' = ' + str(value) + ', '
		return ret[:-2] + ' >'

	def __repr__(self):
		return self.__str__()