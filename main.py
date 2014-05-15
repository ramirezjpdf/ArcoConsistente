import sys
from parserAC import parseArcoConsistencia
from parserAC import preparaAtribuicao
from parserAC import constroiDominios
from parserAC import constroiRestricoes
from GAC      import geraTDA
from GAC      import GAC

if __name__ == '__main__':
	pathEntrada = sys.argv[1]
	with open(pathEntrada) as fo:
		av, vav, ad, vad, atribuicaoDict, mr, tuplasrestricoes = parseArcoConsistencia(fo)
		variaveis = preparaAtribuicao(av, vav, 'Variavel')
		elementosDominios = preparaAtribuicao(ad, vad, 'ElementoDominio')
		constroiDominios(variaveis, elementosDominios, atribuicaoDict)
		restricoes = constroiRestricoes(variaveis, mr, tuplasrestricoes)

		for var in variaveis:
			print 'Dominio de ' + str(var)
			print var.dominio

		print ''
		print 'Elementos Dominios'
		print elementosDominios

		print ''
		print 'Restricoes'
		print restricoes

		TDA = geraTDA(variaveis, restricoes)

		print ''
		print 'TDA:'
		print ''
		for arco in sorted(list(TDA), key=lambda a: a[0].nome):
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