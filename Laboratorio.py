class Laboratorio:
        numero = None
        horario = None
        dia = None
        nmonitores = None
        monitor = []

        def __init__(self, numero, horario, dia, nmonitores):
                self.numero = numero
                self.horario = horario
                self.dia = dia
                self.nmonitores = nmonitores
                self.monitor.append(numero)
        def adicionamonitor(self,monitor):
                self.monitor.append(monitor)



