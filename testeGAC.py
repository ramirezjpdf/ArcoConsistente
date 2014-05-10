from Restricao import *
from ValorDominio import *
from Variavel import *
from GACDebug import *

A = Variavel(1, **dict(nome='A'))
A1 = ValorDominio(A, **dict(valor=1))
A2 = ValorDominio(A, **dict(valor=2))
A3 = ValorDominio(A, **dict(valor=3))
A4 = ValorDominio(A, **dict(valor=4))

A.adicionaValor(A1)
A.adicionaValor(A2)
A.adicionaValor(A3)
A.adicionaValor(A4)

B = Variavel(2, **dict(nome='B'))
B1 = ValorDominio(B, **dict(valor=1))
B2 = ValorDominio(B, **dict(valor=2))
B3 = ValorDominio(B, **dict(valor=3))
B4 = ValorDominio(B, **dict(valor=4))

B.adicionaValor(B1)
B.adicionaValor(B2)
B.adicionaValor(B3)
B.adicionaValor(B4)

def funcRestricaoAmenorB(valorDominioA, valorDominioB):
	return valorDominioA < valorDominioB

restricaoAmenorB = Restricao([A, B], funcRestricaoAmenorB)

print 'Teste do escopo e restricoes'
print '' 
print 'A pertenceEscopo de funcRestricaoAmenorB ? ' + str(restricaoAmenorB.pertenceEscopo(A))
print 'B pertenceEscopo de funcRestricaoAmenorB ? ' + str(restricaoAmenorB.pertenceEscopo(B))

TDA = geraTDA([A, B], [restricaoAmenorB])

#def funcRestricaoAigual3(valorDominioA):
#	return valorDominioA.valor == 3
#
#def funcRestricaoBigual2(valorDominioB):
#	return valorDominioB.valor == 2
#
#restricaoAigual3 = Restricao([A], funcRestricaoAigual3)
#restricaoBigual2 = Restricao([B], funcRestricaoBigual2)
#
#print 'Teste do escopo e restricoes'
#print '' 
#print 'A pertenceEscopo de funcRestricaoAigual3 ? ' + str(restricaoAigual3.pertenceEscopo(A))
#print 'A pertenceEscopo de funcRestricaoBigual2 ? ' + str(restricaoBigual2.pertenceEscopo(A))
#print 'B pertenceEscopo de funcRestricaoBigual2 ? ' + str(restricaoBigual2.pertenceEscopo(B))
#print 'B pertenceEscopo de funcRestricaoAigual3 ? ' + str(restricaoAigual3.pertenceEscopo(B))
#
#TDA = geraTDA([A, B], [restricaoAigual3, restricaoBigual2])

print ''
print 'TDA:'
print ''
for arco in TDA:
	print 'Arco=' + str(arco)

print ''
print 'GAC'
print ''
variaveisNovosDominios = GAC(TDA)

print 'Dominios Finais'
for var in variaveisNovosDominios:
	print 'Dominio de ' + str(var)
	print var.dominio