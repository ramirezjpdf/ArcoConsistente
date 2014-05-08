class ValorDominio(object):
	def __init__(self,variavel,**kwargs):
		self.variavel = variavel
		self.__dict__.update(kwargs)

	def getOrdem(self):
		return self.variavel.ordem