import Rainha

listarainhas = [] # lista com todos os laboratorios
loop = True

f = open('entrada.txt', 'r')

#ler as entradas

loop = True
while loop == True:
    linha = f.readline()
    if linha == '\n':
        loop = False
    else:
        linha = linha.replace('{', '')
        linha = linha.replace('}', '')
        linha = linha.replace('=', ',')
        linha = linha.replace('\n', '')
        linha = linha.split(',')
        rainha = Rainha.Rainha(linha[0])
        for j in range(1,len(linha)):
            rainha.dominio.append(linha[j])
        listarainhas.append(rainha)
                
for i in range(0,len(listarainhas)):
    print(listarainhas[i].numero)
    print(listarainhas[i].dominio[0:8])
                        


