import re

whitespacePattern        = re.compile(r'^[\s\n]+$')
commentPattern           = re.compile(r'^//')
variaveisPattern         = re.compile(r'^@VARIAVES')
atributosPattern         = re.compile(r'^%ATRIBUTOS')
linhaAtributoPattern     = re.compile(r'([^,]+,)+')
dominiosPattern         = re.compile(r'^@DOMINIOS')

def parserArcoConsistencia(fo):
	atributosVariaveis = []
	linhas = (l for l in fo if not commentPattern.match(l) and not whitespacePattern.match(l)): #remove as linhas em branco e comentarios
	if not variaveisPattern.match(linhas.next()):
		raise ValueError('ERRO!! @VARIAVEIS: secao nao encontrada ')
	if not atributosPattern.match(linhas.next()):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada')
	valoresAtributosVariaveis = []
	linha = ''
	while not dominiosPattern.match((linha = linhas.next())):
		atributosVariaveis.append(linha)