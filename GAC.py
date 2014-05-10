from Restricao import *
from ElementoDominio import *
from Variavel import *

'''
param:
->variaveis: lista de  variaveis(objetos da classe Variavel)
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
o dominio(lista de objetos da classe ElementoDominio) como valor, e.g. {Var1 : [ValorDom1, ValorDom2, ValorDom3], Var2:[ValorDom4, ValorDom5, ValorDom6]}
->restricoes: lista com as restricoes(objetos da classe Restricao)

return: lista de variaveis com novos dominios 
'''
def GAC(TDA):
	arcosUsados = []
	while len(TDA) != 0:
		arco = TDA.pop()
		variavel = arco[0]
		dominio = variavel.dominio
		restricao = arco[1]
		novoDominio = []
		if len(restricao.escopo) == 1: #restricao unaria
			novoDominio = [ elementoDominio for elementoDominio in dominio if restricao.funcaorestricao(elementoDominio)]
		elif len(restricao.escopo) == 2: #restricao binaria
			outraVariavel = [ variavelEscopo for variavelEscopo in restricao.escopo if variavelEscopo != variavel ][0] #pega a outra variavel do escopo
			outroDominio = outraVariavel.dominio
			for elementoDominio in dominio:
				for elementoOutroDominio in outroDominio:
					if restricao.chamafuncaorestricao([elementoDominio, elementoOutroDominio]):
						novoDominio.append(elementoDominio)
						break

		if novoDominio != dominio:
			arcosVoltantes = [ arcoUsado for arcoUsado in arcosUsados if arcoUsado[1].pertenceEscopo(variavel) and arcoUsado[1] != restricao and arcoUsado[0] != variavel ]
			TDA.extend(arcosVoltantes)
			arcosUsados = [ arcoUsado for arcoUsado in arcosUsados if arcoUsado not in arcosVoltantes ]#remove os arcos voltantes dos arcosUsados

		variavel.dominio = novoDominio
		arcosUsados.append(arco)
	return [ variavelArco for variavelArco, restricaoArco in arcosUsados ]