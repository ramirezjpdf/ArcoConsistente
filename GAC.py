from Restricao import *

'''
param:
->variaveis: lista de  variaveis(string)
->restricoes: lista com as restricoes(objetos da classe Restricao)
param 

return TDA: lista de tuplas com variavel(string) e restricao(objeto da classe
Restricao)
'''
def geraTDA(variaveis, restricoes):
	return [(variavel, restricao) for variavel in variaveis for restricao in restricoes if restricao.pertenceEscopo(variavel)]


'''
param:
->TDA: TDA obtido por geraTDA
->variavelDominioDict: dicionario com a variavel(string) como chave e com
o dominio(lista) como valor, e.g. {X : ['1', '2', '3'], Y:['1', '2', '3']}
->restricoes: lista com as restricoes(objetos da classe Restricao)
param 
'''
def GAC(TDA, variavelDominioDict, restricoes):
	while len(TDA) != 0:
		arco = TDA.pop()
		TDA.remove(arco)
		variavel = arco[0]
		dominio = variavelDominioDict[variavel]
		novoDominio = [for valor in dominio]