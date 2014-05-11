from Restricao import *
from ElementoDominio import *
from Variavel import *

'''
param:
->variaveis: lista de  variaveis(objetos da classe Variavel)
->restricoes: lista com as restricoes(objetos da classe Restricao)
param 

return TDA: conjunto de tuplas com variavel(objeto da classe Variavel) e restricao(objeto da classe
Restricao)
'''
def geraTDA(variaveis, restricoes):
	return {(variavel, restricao) for variavel in variaveis for restricao in restricoes if restricao.pertenceEscopo(variavel)}


'''
param:
->TDA: TDA obtido por geraTDA

return: conjunto de variaveis com novos dominios 
'''
def GAC(TDA):
	arcosUsados = set()
	while len(TDA) != 0:
		arco = TDA.pop()
		print 'Vez do arco:'
		print str(arco)
		print ''
		variavel = arco[0]
		dominio = variavel.dominio
		restricao = arco[1]
		print 'Dominio de ' + str(variavel) + ':'
		print str(dominio)
		print ''
		novoDominio = []
		if len(restricao.escopo) == 1: #restricao unaria
			novoDominio = [ elementoDominio for elementoDominio in dominio if restricao.funcaorestricao(elementoDominio)]
		elif len(restricao.escopo) == 2: #restricao binaria
			outraVariavel = [ variavelEscopo for variavelEscopo in restricao.escopo if variavelEscopo != variavel ][0] #pega a outra variavel do escopo
			print 'outraVariavel = ' + str(outraVariavel)
			outroDominio = outraVariavel.dominio
			#novoDominio = [ elementoDominio for elementoDominio in dominio for elementoOutroDominio in itertools.takewhile(outroDominio) if restricao.chamafuncaorestricao([elementoDominio, elementoOutroDominio]) ]

			for elementoDominio in dominio:
				for elementoOutroDominio in outroDominio:
					if restricao.chamafuncaorestricao([elementoDominio, elementoOutroDominio]):
						novoDominio.append(elementoDominio)
						break

		print 'Novo Dominio de ' + str(variavel) + ':'
		print str(novoDominio)
		print ''
		if novoDominio != dominio:
			arcosVoltantes = { arcoUsado for arcoUsado in arcosUsados if arcoUsado[1].pertenceEscopo(variavel) and arcoUsado[1] != restricao and arcoUsado[0] != variavel }
			TDA |= arcosVoltantes
			arcosUsados -= arcosVoltantes#remove os arcos voltantes dos arcosUsados

		variavel.dominio = novoDominio
		arcosUsados.add(arco)
		print 'Arcos Usados: \n'
		print sorted(list(arcosUsados), key=lambda a: a[0].nome)
		print ''

	return { variavelArco for variavelArco, restricaoArco in arcosUsados}