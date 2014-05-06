<<<<<<< HEAD
import Laboratorio
import Monitores
import Restricoes
=======
from Laboratorio import *
from Monitores import *
import copy
>>>>>>> 7abcb2abfe1e1a392ff6164cdda51e19320e0e4d

listalaboratorios = [] # lista com todos os laboratorios
listamonitores = [] # lista com todos os monitores
listarestricoes = [] # lista com todas as restriçoes
loop = True

with open('entrada2.txt', 'r') as f:
    while loop == True:
    #entrada do tipo "Monitor,Carlos,10-12,segunda"
            linha = f.readline()
            lista = linha.split(',')
    # lista[0] = primeira palavra da linha
    
            if lista[0] == '\n':
                    loop = False
            if lista[0] == 'Laboratorio': # se a primeira palavra for laboratorio, cria um objeto da classe laboratorio
                    numero = int(lista[1])
                    horario = lista[2]
                    dia = lista[3]
                    nmonitores = int(lista[4])
                    lab = Laboratorio(numero,horario,dia,nmonitores)
                    print 'lista monitor: ' + str(lab.monitores)
                    listalaboratorios.append(lab)
    
                    for i in range(nmonitores - 1): # se um laboratorio precisar de mais de um monitor, duplica esse laboratorio e coloca na lista de laboratorios
                        novo = copy.deepcopy(lab) #novo apontava para o msm objeto. Nao estava duplicando o laboratorio. precisa dar um deepcopy
                        listalaboratorios.append(novo)
            if lista[0] == 'Monitor': # se a primeira palavra for monitor, cria um objeto da classe monitor
                    nome = lista[1]
                    horario = lista[2]
                    dia = lista[3]
                    monitor = Monitores(nome,horario,dia) 
                    listamonitores.append(monitor)
    
    for lab in listalaboratorios:
        print lab.numero

<<<<<<< HEAD
        if lista[0] == '\n':
                loop = False
        if lista[0] == 'Laboratorio': # se a primeira palavra for laboratorio, cria um objeto da classe laboratorio
                numero = int(lista[1])
                horario = lista[2]
                dia = lista[3]
                nmonitores = int(lista[4])
                lab = Laboratorio.Laboratorio(numero,horario,dia,nmonitores)
                print(lab.monitor,'lista monitor')
                listalaboratorios.append(lab)
        if lista[0] == 'Monitor': # se a primeira palavra for monitor, cria um objeto da classe monitor
                nome = lista[1]
                horario = lista[2]
                dia = lista[3]
                monitor = Monitores.Monitores(nome,horario,dia) 
                listamonitores.append(monitor)

# se um laboratorio precisar de mais de um monitor, duplica esse laboratorio e coloca na lista de laboratorios
for i in range(0,len(listalaboratorios)):
        while listalaboratorios[i].nmonitores > 1:
                novo = listalaboratorios[i]
                listalaboratorios.append(novo)
                listalaboratorios[i].nmonitores = listalaboratorios[i].nmonitores - 1
                

#ler as entradas

loop = True
while loop == True:
        linha = f.readline()
        if linha == '\n':
                loop = False
        else:
#transforma "1={Marcos,Pedro}" em (1,Marcos,Pedro)
                lista = linha.replace('{', '')
                lista = lista.replace('}', '')
                lista = lista.replace('=', ',')
                lista = lista.replace('\n', '')
                lista = lista.split(',')
#enquanto a variavel(1) existir na listalaboratorios, acrescenta os monitores (Marcos,Pedro) ao dominio
        for i in range(0,len(listalaboratorios)):
                if listalaboratorios[i].numero == int(lista[0]):
                        for j in range(1,len(lista)):
                                listalaboratorios[i].adicionamonitor(lista[j])

# le as restricoes
loop = True
while loop == True:
        linha = f.readline()
        if linha == '':
                loop = False
        else:
#transforma "1={Marcos,Pedro}" em (1,Marcos,Pedro)
                print(linha + 'l')
                lista = linha.replace('.', ' ')
                #lista = lista.replace('}', '')
                #lista = lista.replace('=', ',')
                #lista = lista.replace('\n', '')
                lista = lista.split(' ')
#enquanto a variavel(1) existir na listalaboratorios, acrescenta os monitores (Marcos,Pedro) ao dominio
        if len(lista) == 3:
                print('restricoes')
                res = Restricoes.Restricoes(lista[0],lista[2],lista[1])
                listarestricoes.append(res)
        if len(lista) == 5:
                res = Restricoes.Restricoes(lista[0],None,lista[2]) #nao precisa do ladodir, pois como o tipo é "p" já sabemos que devemos usar o dominio do ladoesq
                listarestricoes.append(res)
                
for i in range(0,len(listarestricoes)):
        print(listarestricoes[i].ladoesq)
        print(listarestricoes[i].tipo)
        print(listarestricoes[i].ladodir)
        print(listarestricoes[i].estado)
=======
    #ler as entradas
    
    loop = True
    while loop == True:
            linha = f.readline()
            if linha == '\n':
                    loop = False
            else:
    #transforma "1={Marcos,Pedro}" em (1,Marcos,Pedro)
                    lista = linha.replace('{', '')
                    lista = lista.replace('}', '')
                    lista = lista.replace('=', ',')
                    lista = lista.replace('\n', '')
                    lista = lista.split(',')
                    print lista
    #enquanto a variavel(1) existir na listalaboratorios, acrescenta os monitores (Marcos,Pedro) ao dominio
            print len(listalaboratorios)
            i = 0
            for lab in listalaboratorios:
                    print lab.numero
                    i += 1
                    if lab.numero == int(lista[0]):
                        print lab.numero
                        print lista[1:]
                        lab.monitores.extend(lista[1:])
                    print "i = " + str(i)
                        
for lab in listalaboratorios:
        print(lab.numero)
        print(lab.dia)
        print(lab.horario)
        print(lab.monitores)
>>>>>>> 7abcb2abfe1e1a392ff6164cdda51e19320e0e4d
