import clips
import csv

class Entidad():
    def __init__(self):
        self.archivo = ""
        self.data =""
        #"/home/christian/PycharmProjects/TFIClips/empresas_1.csv"

    def leerArchivo(self):
        with  open(self.archivo, 'rb') as file_data:
            self.data = [row for row in csv.reader(file_data)]

    def getDatosArchivo(self):
        return self.data

    def getColumnasArchivoCantidad(self):
        return len(self.data[0])

    def getRegistrosCantidad(self):
        return len(self.data)

    def getArchivo(self):
        return self.archivo

    def putArchivo(self,arch):
        self.archivo = arch

    def addAssertTemplate(self,defNombre,defTemplate,defComentario):
        temp = clips.BuildTemplate(defNombre,defTemplate,defComentario)
        return temp

    def leeAssertTemplate(self,defTemp):
        print "*** Vizualizacion Template"
        print defTemp.PPForm()


    def putAssertTemplate(self,defTemp,defCampos,defData):
        for row in defData:
            indice = 0
            f1 = clips.Fact(defTemp)
            for valor in defCampos:
                f1.Slots[valor] = row[indice]
                indice =  indice +1
            f1.Assert()

