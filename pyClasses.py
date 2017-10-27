import clips
import csv

class Entidad():
    def __init__(self):
        self.archivo = '/home/christian/tfiClips/empresas_1.csv'
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
        print "*** Vizualizacion Template Empresas"
        print defTemp.PPForm()


    def putAssertTemplate(self,defTemp,defCampos,defData):
        for row in defData:
            indice = 0
            f1 = clips.Fact(defTemp)
            for valor in defCampos:
                f1.Slots[valor] = row[indice]
                indice =  indice +1
            f1.Assert()


'''CARGA EMPRESAS '''

emplista = Entidad()
emplista.putArchivo('/home/christian/tfiClips/empresas_1.csv')
emplista.leerArchivo()
empre = emplista.getDatosArchivo()

varClipTemplateNombre = """empresa"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot tipo (type STRING))
    (slot categoria (type STRING))
    (slot ciudad (type STRING))
    (slot pais (type STRING))
    (slot comercioext (type STRING))
    (slot puntaje (type INTEGER))
 """
varClipTemplateComentario = """Es Template Empresa"""

varCamposTemp = ["eid","nombre","tipo","categoria","ciudad","pais","comercioext","puntaje"]

tempEmpresa = emplista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
emplista.leeAssertTemplate(tempEmpresa)
emplista.putAssertTemplate(tempEmpresa,varCamposTemp,empre)

#clips.PrintFacts()

'''CARGA COMPRAS '''

compralista = Entidad()
compralista.putArchivo('/home/christian/tfiClips/servicios_1.csv')
compralista.leerArchivo()
comp = compralista.getDatosArchivo()

varClipTemplateNombre = """compra"""
varClipTemplateDatos = """
    (slot sid (type INTEGER))
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
 """
varClipTemplateComentario = """Es Template Compras"""

varCamposTemp = ["sid","eid","nombre"]

tempCompra = compralista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
compralista.leeAssertTemplate(tempCompra)
compralista.putAssertTemplate(tempCompra,varCamposTemp,comp)




'''CARGA VENTAS '''


ventaLista = Entidad()
ventaLista.putArchivo('/home/christian/tfiClips/productos_1.csv')
ventaLista.leerArchivo()
venta = ventaLista.getDatosArchivo()

varClipTemplateNombre = """venta"""
varClipTemplateDatos = """
    (slot pid (type INTEGER))
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot precio (type STRING))
    (slot moneda (type STRING))
    (slot promocional (type STRING))
 """
varClipTemplateComentario = """Es Template Ventas"""

varCamposTemp = ["pid","eid","nombre","precio","moneda","promocional"]


tempVenta = ventaLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
ventaLista.leeAssertTemplate(tempVenta)
ventaLista.putAssertTemplate(tempVenta,varCamposTemp,venta)


#clips.PrintFacts()


clips.PrintFacts()
clips.Clear()


