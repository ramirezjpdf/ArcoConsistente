import re

whitespacePattern        = re.compile(r'^[\s\n]+$')
commentPattern           = re.compile(r'^//')
variaveisPattern         = re.compile(r'^@VARIAVEIS')
atributosPattern         = re.compile(r'^%ATRIBUTOS')
linhaAtributoPattern     = re.compile(r'([^,]+,)+')
valoresAtributosPattern  = re.compile(r'^%%VALORES')
dominiosPattern          = re.compile(r'^@DOMINIOS')
restricoesPattern        = re.compile(r'@RESTRICOES')
idPattern                = re.compile(r'^id=[\d\w_]+')
valoresSplitPattern      = re.compile(r',(?![^\[\]]*\])')

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
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada na secao @VARIAVEIS')

	atributosVariaveis = ['id']
	valoresAtributosVariaveis = []

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @VARIAVEIS')
	atributosVariaveis.extend(linha[:-1].split(','))
	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao $ATRIBUTOS. %%VALORES: subsecao nao encontrada na secao @VARIAVEIS')
	if not valoresAtributosPattern.match(linha):
		raise ValueError('ERRO!! %%VALORES: subsecao nao encontrada na secao @VARIAVEIS ou os atributos da subsecao #ATRIBUTOS nao foram declarados')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @VARIAVEIS')
	while not dominiosPattern.match(linha):
		valores = valoresSplitPattern.split(linha[:-1])
		if not idPattern.match(valores[0]):
			raise ValueError('ERRO!! Para a linha: < ' + linha[:-1] + ' >. Nao foi encontrado atributo id')
		valores[0] = re.sub('^id=', '', valores[0])
		valoresAtributosVariaveis.append(valores)
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @VARIAVEIS. Secao @DOMINIOS nao encontrada')
	if not valoresAtributosVariaveis:
		raise ValueError('ERRO!! Nenhum valor para os atributos das variaveis foi declarado')

	atributosDominios = ['id']
	valoresAtributosDominios = []

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado %ATRIBUTOS: subsecao nao encontrada na secao @DOMINIOS')
	if not atributosPattern.match(linha):
		raise ValueError('ERRO!! %ATRIBUTOS: subsecao nao encontrada na secao @DOMINIOS')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @DOMINIOS')
	atributosDominios.extend(linha[:-1].split(','))
	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %ATRIBUTOS da secao @DOMINIOS. Subsecao ##VALORES nao encontrada')
	if not valoresAtributosPattern.match(linha):
		raise ValueError('ERRO!! %%VALORES: subsecao nao encontrada na secao @DOMINIOSou os atributos da subsecao #ATRIBUTOS nao foram declarados')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @DOMINIOS')
	while not restricoesPattern.match(linha):
		valores = valoresSplitPattern.split(linha[:-1])
		if not idPattern.match(valores[0]):
			raise ValueError('ERRO!! Para a linha: < ' + linha[:-1] + ' >. Nao foi encontrado atributo id')
		valores[0] = re.sub('^id=', '', valores[0])
		valoresAtributosDominios.append(valores)
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