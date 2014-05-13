import re

whitespacePattern        = re.compile(r'^[\s\n]+$')
commentPattern           = re.compile(r'^//')
variaveisPattern         = re.compile(r'^@VARIAVEIS')
atributosPattern         = re.compile(r'^%ATRIBUTOS')
linhaAtributoPattern     = re.compile(r'([^,]+,)+')
valoresAtributosPattern  = re.compile(r'^%%VALORES')
dominiosPattern          = re.compile(r'^@DOMINIOS')
restricoesPattern        = re.compile(r'@RESTRICOES')

def parseArcoConsistencia(fo):
	atributosVariaveis = []
	valoresAtributosVariaveis = []

	#remove as linhas em branco e comentarios
	linhas = (l for l in fo if not commentPattern.match(l) and not whitespacePattern.match(l))
	linha = linhas.next()
	if not variaveisPattern.match(linha):
		raise ValueError('ERRO!! @VARIAVEIS: secao nao encontrada ')
	linha = linhas.next()
	if not atributosPattern.match(linha):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada')

	linha = linhas.next()
	while not valoresAtributosPattern.match(linha):
		atributosVariaveis.append(linha[:-1])
		linha = linhas.next()

	linha = linhas.next()
	while not dominiosPattern.match(linha):
		valoresAtributosVariaveis.append(linha[:-1])
		linha = linhas.next()

	atributosDominios = []
	valoresAtributosDominios = []
	linha = linhas.next()
	if not atributosPattern.match(linha):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada')

	linha = linhas.next()
	while not valoresAtributosPattern.match(linha):
		atributosDominios.append(linha[:-1])
		linha = linhas.next()

	linha = linhas.next()
	while not restricoesPattern.match(linha):
		valoresAtributosDominios.append(linha[:-1])
		linha = linhas.next()
	return atributosVariaveis, valoresAtributosVariaveis, atributosDominios, valoresAtributosDominios