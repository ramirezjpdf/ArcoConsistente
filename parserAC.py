import re
import sys
import copy
import os.path
from Variavel import *
from ElementoDominio import *
from Restricao import *

whitespacePattern        = re.compile(r'^[\s\n]+$')
commentPattern           = re.compile(r'^//')
variaveisPattern         = re.compile(r'^@VARIAVEIS')
atributosPattern         = re.compile(r'^%ATRIBUTOS')
linhaAtributoPattern     = re.compile(r'([^,]+,)+')
valoresAtributosPattern  = re.compile(r'^%%VALORES')
dominiosPattern          = re.compile(r'^@DOMINIOS')
atribuicaoPattern        = re.compile(r'^@ATRIBUICAO')
restricoesPattern        = re.compile(r'@RESTRICOES')
idPattern                = re.compile(r'^id=[\d\w_]+')
valoresSplitPattern      = re.compile(r',(?![^\[\]]*\])') #separa uma linha de valores pelas virgulas menos as linhas que estao dentro de listas

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

	atributosVariaveis = []
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

	atributosDominios = []
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
	while not atribuicaoPattern.match(linha):
		valores = valoresSplitPattern.split(linha[:-1])
		if not idPattern.match(valores[0]):
			raise ValueError('ERRO!! Para a linha: < ' + linha[:-1] + ' >. Nao foi encontrado atributo id')
		valores[0] = re.sub('^id=', '', valores[0])
		valoresAtributosDominios.append(valores)
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na subsecao %%VALORES da secao @DOMINIOS. Secao @ATRIBUICAO nao encontrada')
	if not valoresAtributosDominios:
		raise ValueError('ERRO!! Nenhum valor para os atributos dos dominios foi declarado')

	atribuicaoDict = {}

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado secao @ATRIBUICAO')
	while not restricoesPattern.match(linha):
		atribuicao = linha[:-1].split('=')
		atribuicaoDict[atribuicao[0]] = re.sub(r'[\{\}]', '', atribuicao[1]).split(',')
		linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na secao @ATRIBUICAO')
	if not atribuicaoDict:
		raise ValueError('ERRO!! Nenhuma atribuicao entre variaveis e dominios encontrada')

	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado na secao @RESTRICOES!! O nome do modulo das restricoes nao foi declarado')
	modulorestricoes = linha[:-1]
	linha = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado. Faltam restricoes na secao @RESTRICOES!!')
	restricoes = []
	while True:
		escopo = linha[:-1].split(',')
		funcrestricao = proximalinha(linhas, 'ERRO!! Fim de arquivo inesperado. Restricao com escopo = (' + escopo + ') nao possui funcao da restricao ')
		restricoes.append((escopo, funcrestricao[:-1]))
		try:
			linha = linhas.next()
		except StopIteration:
			break
	return atributosVariaveis, valoresAtributosVariaveis, atributosDominios, valoresAtributosDominios, atribuicaoDict, modulorestricoes, restricoes

def preparaAtribuicao(atributos, valores, nomeClasse):
	listPattern              = re.compile(r'^[.* ]$')
	stringToListSplitPattern = re.compile(r'[\[,\]]')
	lista = []
	initmethod = getattr(__import__(nomeClasse), nomeClasse)
	for i, valor in enumerate(valores):
		valor = [stringToListSplitPattern.split(v)[1:-1] if listPattern.match(v) else v for v in valor ] #transforma a string  '[a,b,c]' na lista ['a','b','c']
		objId = valor[0]
		atributosDict = dict(zip(atributos, valor[1:]))
		if nomeClasse == 'Variavel':
			obj = initmethod(objId, i, **atributosDict)
		elif nomeClasse == 'ElementoDominio':
			obj = initmethod(objId,**atributosDict)
		lista.append(variavel)
	return lista

def constroiDominios(variaveis, elementosDominios, atribuicaoDict):
	for variavel in variaveis:
		for elementoDominio in elementosDominios:
			if elementoDominio.elementoId in atribuicaoDict[variavel.variavelId]:
				copiaElementoDominio = copy.deepcopy(elementoDominio)
				copiaElementoDominio.variavel = variavel
				variavel.dominio.append(copiaElementoDominio)

def constroiRestricoes(variaveis, modulorestricoes, tuplasrestricoes):
	sys.path.append(os.path.dirname(modulorestricoes))
	mod = None
	try:
		mod = __import__(os.path.basename(modulorestricoes).replace('.py', ''))
	except:
		raise ValueError('ERRO!! Modulo com as funcoes de restricao nao encontrado')
