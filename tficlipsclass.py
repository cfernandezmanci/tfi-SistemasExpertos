import clips
import csv



class Empresas():
    def __init__(self):
        self.eid = 0
        self.nombre = ''
        self.categoria = ''
        self.ciudad = 'BS AS'
        self.pais = 'ARGENTINA'
        self.comercioext = 'NADA'
        self.puntaje  = 0


    def mostrar(self):
        print 'eid: ' + str(self.eid)
        print 'nombre: ' + self.nombre
        print 'categoria:' + self.categoria
        print 'ciudad: ' + self.ciudad
        print 'pais: ' + self.pais
        print 'comercioext: ' + self.comercioext
        print 'puntaje: ' + str(self.puntaje)

class EmpresasLista():
    def __init__(self):
        self.archivo = "/home/fernandezc/PycharmProjects/TFIClips/empresas.csv"

    def leerArchivo(self):
        with  open(self.archivo, 'rb') as file_data:
            self.data = [row for row in csv.reader(file_data)]

    def getDatosArchivo(self):
        return self.data

    def getColumnasArchivoCantidad(self):
        return len(self.data[0])

    def getColumnasCantidad(self):
        return len(self.data)


#Instancia Empresas
emp = Empresas()
emp.eid = 1
emp.nombre = 'La Ponderosa S.A.'
emp.mostrar()

#Instancia EmpresasLista

emplista = EmpresasLista()
emplista.leerArchivo()
empre = emplista.getDatosArchivo()
print emplista.getColumnasArchivoCantidad()
print emplista.getColumnasCantidad()

for registros in empre:
    print registros[5]