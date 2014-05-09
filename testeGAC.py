from Restricao import *
from ValorDominio import *
from Variavel import *
from GAC import *

A = Variavel(1, **dict(nome='A'))
A1 = ValorDominio(A, **dict(valor=1))
A2 = ValorDominio(A, **dict(valor=2))
A3 = ValorDominio(A, **dict(valor=3))
A4 = ValorDominio(A, **dict(valor=4))

A.adicionaValor(A1)
A.adicionaValor(A2)
A.adicionaValor(A3)
A.adicionaValor(A4)

B = Variavel(1, **dict(nome='B'))
B1 = ValorDominio(B, **dict(vBlor=1))
B2 = ValorDominio(B, **dict(vBlor=2))
B3 = ValorDominio(B, **dict(vBlor=3))
B4 = ValorDominio(B, **dict(vBlor=4))

B.adicionaValor(B1)
B.adicionaValor(B2)
B.adicionaValor(B3)
B.adicionaValor(B4)

def funcRestricaoAmenorB(valorDominioA, valorDominioB):
	return valorDominioA < valorDominioB

restricaoAmenorB = Restricao([A, B], funcRestricaoAmenorB)

TDA = geraTDA([A, B], [restricaoAmenorB])
variaveisNovosDominios = GAC(TDA)