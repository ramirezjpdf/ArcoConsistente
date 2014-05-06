from Laboratorio import *
from Monitores import *
import copy

listalaboratorios = [] # lista com todos os laboratorios
listamonitores = [] # lista com todos os monitores
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
