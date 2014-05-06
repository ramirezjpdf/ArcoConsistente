class Laboratorio:
        def __init__(self, numero, horario, dia, nmonitores):
            self.numero = numero
            self.monitores = [numero]
            self.horario = horario
            self.dia = dia
            self.nmonitores = nmonitores
				
        def adicionamonitor(self,monitor):
            self.monitores.append(monitor)



