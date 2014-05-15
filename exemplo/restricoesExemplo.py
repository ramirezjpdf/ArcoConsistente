'''
	Exemplo de arquivo de funcao de Restricao
	IMPORTANTE!!
	 A ordem em que os argumentos devem ser declarados nas funcoes
	deve respeitar a ordem em que as variaveis sao declaradas no arquivo
	de entrada. 
	Assim, vemos que na funcao funcRestricaoEmenorC(elementoDominioC, elementoDominioE)
	o argumento que recebe um elemento de dominio da variavel C
	eh declarado antes do argumento que recebe um elemento de
	dominio da variavel E, porque a variavel C foi declarada antes 
	da variavel E no arquivo de entrada
'''

def funcRestricaoAdiferenteB(elementoDominioA, elementoDominioB):
	return elementoDominioA.valor != elementoDominioB.valor

def funcRestricaoAigualD(elementoDominioA, elementoDominioD):
	return elementoDominioA.valor == elementoDominioD.valor

def funcRestricaoEmenorA(elementoDominioA, elementoDominioE):
	return int(elementoDominioE.valor) < int(elementoDominioA.valor)

#Restricao B
def funcRestricaoBdiferenteD(elementoDominioB, elementoDominioD):
	return elementoDominioB.valor != elementoDominioD.valor

def funcRestricaoBdiferenteC(elementoDominioB, elementoDominioC):
	return elementoDominioB.valor != elementoDominioC.valor

def funcRestricaoEmenorB(elementoDominioB, elementoDominioE):
	return int(elementoDominioE.valor) < int(elementoDominioB.valor)

#Restricao C
def funcRestricaoCmenorD(elementoDominioC, elementoDominioD):
	return int(elementoDominioC.valor) < int(elementoDominioD.valor)

def funcRestricaoEmenorC(elementoDominioC, elementoDominioE):
	return int(elementoDominioE.valor) < int(elementoDominioC.valor)

#Restricao D
def funcRestricaoEmenorD(elementoDominioD, elementoDominioE):
	return int(elementoDominioE.valor) < int(elementoDominioD.valor)