import re

whitespacePattern        = re.compile(r'^[\s\n]+$')
commentPattern           = re.compile(r'^//')
variaveisPattern         = re.compile(r'^@VARIAVEIS')
atributosPattern         = re.compile(r'^%ATRIBUTOS')
linhaAtributoPattern     = re.compile(r'([^,]+,)+')
valoresAtributosPattern  = re.compile(r'^%%VALORES')
dominiosPattern          = re.compile(r'^@DOMINIOS')
restricoesPattern        = re.compile(r'@RESTRICOES')

def proximalinha(g, errormsg):
	try:
		return g.next()
	except StopIteration:
		raise EOFError(errormsg)

def parseArcoConsistencia(fo):
	#remove as linhas em branco e comentarios
	linhas = (l for l in fo if not commentPattern.match(l) and not whitespacePattern.match(l))
	linha = proximalinha(linhas, 'ERRO!! @VARIAVEIS: secao nao encontrada')
	if not variaveisPattern.match(linha):
		raise ValueError('ERRO!! @VARIAVEIS: secao nao encontrada ')
	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado. %ATRIBUTOS: subsecao nao encontrada na secao @VARIAVEIS')
	if not atributosPattern.match(linha):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada')

	atributosVariaveis = []
	valoresAtributosVariaveis = []

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @VARIAVEIS')
	while not valoresAtributosPattern.match(linha):
		atributosVariaveis.append(linha[:-1])
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @VARIAVEIS. Subsecao %%VALORES nao encontrada')
	if not atributosVariaveis:
		raise ValueError('ERRO!! Nenhum atributo para as variaveis foi declarado')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @VARIAVEIS')
	while not dominiosPattern.match(linha):
		valoresAtributosVariaveis.append(linha[:-1])
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @VARIAVEIS. Secao @DOMINIOS nao encontrada')
	if not valoresAtributosVariaveis:
		raise ValueError('ERRO!! Nenhum valor para os atributos das variaveis foi declarado')

	atributosDominios = []
	valoresAtributosDominios = []

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado %ATRIBUTOS: subsecao nao encontrada')
	if not atributosPattern.match(linha):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @DOMINIOS')
	while not valoresAtributosPattern.match(linha):
		atributosDominios.append(linha[:-1])
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @DOMINIOS. Subsecao ##VALORES nao encontrada')
	if not atributosDominios:
		raise ValueError('ERRO!! Nenhum valor para os atributos dos dominios foi declarado')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @DOMINIOS')
	while not restricoesPattern.match(linha):
		valoresAtributosDominios.append(linha[:-1])
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @DOMINIOS. Secao @RESTRICOES nao encontrada')
	if not valoresAtributosDominios:
		raise ValueError('ERRO!! Nenhum valor para os atributos dos dominios foi declarado')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na secao @RESTRICOES!! O nome do modulo das restricoes nao foi declarado')
	modulorestricoes = linha[:-1]
	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado. Faltam restricoes na secao @RESTRICOES!!')
	restricoes = []
	while True:
		escopo = linha[:-1]
		funcrestricao = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado. Restricao com escopo = (' + escopo + ') nao possui funcao da restricao ')
		restricoes.append((escopo, funcrestricao[:-1]))
		try:
			linha = linhas.next()
		except StopIteration:
			break
	return atributosVariaveis, valoresAtributosVariaveis, atributosDominios, valoresAtributosDominios, modulorestricoes, restricoes