class ValorDominio(object):
	def __init__(self,variavel,**kwargs):
		self.variavel = variavel
		self.__dict__.update(kwargs)

	def getOrdem(self):
		return self.variavel.ordem

	def __str__(self):
		ret = ''
		aux = dict(self.__dict__)
		del aux['variavel']
		for key, value in aux.iteritems():
			ret += key + ' = ' + str(value) + ', '
		return ret[:-2]

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		selfAux = dict(self.__dict__)
		otherAux = dict(self.__dict__)
		del selfAux['variavel']
		del otherAux['variavel']
		return selfAux == otherAux

	def __hash__(self):
		selfAux = dict(self.__dict__)
		del selfAux['variavel']
		return hash(str(selfAux))