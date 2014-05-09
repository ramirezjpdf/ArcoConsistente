from Restricao import *
from ValorDominio import *
from Variavel import *

'''
param:
->variaveis: lista de  variaveis(string)
->restricoes: lista com as restricoes(objetos da classe Restricao)
param 

return TDA: lista de tuplas com variavel(objeto da classe Variavel) e restricao(objeto da classe
Restricao)
'''
def geraTDA(variaveis, restricoes):
	return [(variavel, restricao) for variavel in variaveis for restricao in restricoes if restricao.pertenceEscopo(variavel)]


'''
param:
->TDA: TDA obtido por geraTDA
->variavelDominioDict: dicionario com a variavel(objeto da classe Variavel) como chave e com
o dominio(lista de objetos da classe ValorDominio) como valor, e.g. {Var1 : [ValorDom1, ValorDom2, ValorDom3], Var2:[ValorDom4, ValorDom5, ValorDom6]}
->restricoes: lista com as restricoes(objetos da classe Restricao)
param 
'''
def GAC(TDA, variavelDominioDict, restricoes):
	while len(TDA) != 0:
		arco = TDA.pop()
		TDA.remove(arco)
		variavel = arco[0]
		dominio = variavelDominioDict[variavel]
		restricao = arco[1]
		novoDominio = []
		if len(restricao.escopo) == 1: #restricao unaria
			novoDominio = [ valorDominio for valorDominio in dominio if restricao.funcaorestricao(valorDominio)]
		elif len(restricao.escopo) == 2: #restricao binaria
			outraVariavel = [ variavel for variavel in restricao.escopo if variavel != variavel ][0] #pega a outra variavel do escopo
			outroDominio = variavelDominioDict[outraVariavel]
			novoDominio = [ valorDominio for valorDominio in dominio for valorOutroDominio in outroDominio if restricao.chamafuncaorestricao([valorDominio, valorOutroDominio]) ]
		