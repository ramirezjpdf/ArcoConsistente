from Restricao import *
from ElementoDominio import *
from Variavel import *
from GAC import *

'''
exemplo da aula 12 slide 3
'''

A = Variavel(1, **dict(nome='A'))
A1 = ElementoDominio(A, **dict(valor=1))
A2 = ElementoDominio(A, **dict(valor=2))
A3 = ElementoDominio(A, **dict(valor=3))
A4 = ElementoDominio(A, **dict(valor=4))
A.adicionaElemento(A1)
A.adicionaElemento(A2)
A.adicionaElemento(A3)
A.adicionaElemento(A4)

B = Variavel(2, **dict(nome='B'))
B1 = ElementoDominio(B, **dict(valor=1))
B2 = ElementoDominio(B, **dict(valor=2))
B4 = ElementoDominio(B, **dict(valor=4))
B.adicionaElemento(B1)
B.adicionaElemento(B2)
B.adicionaElemento(B4)

C = Variavel(3, **dict(nome='C'))
C1 = ElementoDominio(C, **dict(valor=1))
C3 = ElementoDominio(C, **dict(valor=3))
C4 = ElementoDominio(C, **dict(valor=4))
C.adicionaElemento(C1)
C.adicionaElemento(C3)
C.adicionaElemento(C4)

D = Variavel(4, **dict(nome='D'))
D1 = ElementoDominio(D, **dict(valor=1))
D2 = ElementoDominio(D, **dict(valor=2))
D3 = ElementoDominio(D, **dict(valor=3))
D4 = ElementoDominio(D, **dict(valor=4))
D.adicionaElemento(D1)
D.adicionaElemento(D2)
D.adicionaElemento(D3)
D.adicionaElemento(D4)

E = Variavel(5, **dict(nome='E'))
E1 = ElementoDominio(E, **dict(valor=1))
E2 = ElementoDominio(E, **dict(valor=2))
E3 = ElementoDominio(E, **dict(valor=3))
E4 = ElementoDominio(E, **dict(valor=4))
E.adicionaElemento(E1)
E.adicionaElemento(E2)
E.adicionaElemento(E3)
E.adicionaElemento(E4)

#Restricoes

#Restricao A
def funcRestricaoAdiferenteB(elementoDominioA, elementoDominioB):
	#print 'Funcao de Restricao'
	#print ''
	#print 'Variavel de elementoDominioA: ' + str(elementoDominioA.variavel)
	#print 'Variavel de elementoDominioB: ' + str(elementoDominioB.variavel)
	#print 'elementoDominioA.valor != elementoDominioB.valor ? ' + str(elementoDominioA.valor < elementoDominioB.valor)
	#print 'para elementoDominioA.valor = ' + str(elementoDominioA.valor) + ' e elementoDominioB.valor = ' +  str(elementoDominioB.valor)
	return elementoDominioA.valor != elementoDominioB.valor
restricaoAdiferenteB = Restricao(set([A, B]), funcRestricaoAdiferenteB)

def funcRestricaoAigualD(elementoDominioA, elementoDominioD):
	return elementoDominioA.valor == elementoDominioD.valor
restricaoAigualD = Restricao(set([A, D]), funcRestricaoAigualD)

def funcRestricaoEmenorA(elementoDominioA, elementoDominioE):
	return elementoDominioE.valor < elementoDominioA.valor
restricaoEmenorA = Restricao(set([A, E]), funcRestricaoEmenorA)

#Restricao B
def funcRestricaoBdiferenteD(elementoDominioB, elementoDominioD):
	return elementoDominioB.valor != elementoDominioD.valor
restricaoBdiferenteD = Restricao(set([B, D]), funcRestricaoBdiferenteD)

def funcRestricaoBdiferenteC(elementoDominioB, elementoDominioC):
	return elementoDominioB.valor != elementoDominioC.valor
restricaoBdiferenteC = Restricao(set([B, C]), funcRestricaoBdiferenteC)

def funcRestricaoEmenorB(elementoDominioB, elementoDominioE):
	return elementoDominioE.valor < elementoDominioB.valor
restricaoEmenorB = Restricao(set([B, E]), funcRestricaoEmenorB)

#Restricao C
def funcRestricaoCmenorD(elementoDominioC, elementoDominioD):
	return elementoDominioC.valor < elementoDominioD.valor
restricaoCmenorD = Restricao(set([C, D]), funcRestricaoCmenorD)

def funcRestricaoEmenorC(elementoDominioC, elementoDominioE):
	return elementoDominioE.valor < elementoDominioC.valor
restricaoEmenorC = Restricao(set([C, E]), funcRestricaoEmenorC)

#Restricao D
def funcRestricaoEmenorD(elementoDominioD, elementoDominioE):
	return elementoDominioE.valor < elementoDominioD.valor
restricaoEmenorD = Restricao(set([D, E]), funcRestricaoEmenorD)

#Restricao E
#todas as restricoes de E ja foram feitas

#print 'Teste do escopo e restricoes'
#print '' 
#print 'A pertenceEscopo de funcRestricaoAmenorB ? ' + str(restricaoAmenorB.pertenceEscopo(A))
#print 'B pertenceEscopo de funcRestricaoAmenorB ? ' + str(restricaoAmenorB.pertenceEscopo(B))

TDA = geraTDA([A, B, C, D, E], [restricaoAdiferenteB, restricaoAigualD, restricaoEmenorA, restricaoBdiferenteD, restricaoBdiferenteC, restricaoEmenorB, restricaoCmenorD, restricaoEmenorC, restricaoEmenorD])

print ''
print 'TDA:'
print ''
for arco in TDA:
	print 'Arco=' + str(arco)

print ''
print 'GAC'
print ''
variaveisNovosDominios = GAC(TDA)

print ''
print 'Dominios Finais'
for var in variaveisNovosDominios:
	print 'Dominio de ' + str(var)
	print var.dominio