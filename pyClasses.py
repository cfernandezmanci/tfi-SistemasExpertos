import clips
import csv
import sys

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


class Empresas():
    def __init__(self,archivoEmp):
       self.archivoEmpresas = archivoEmp

    def setArchivoEmpresas(self,archivo):
        self.archivoEmpresas= archivo

    def setEmpresa(self,empresa):
        empresaPuntaje = Entidad()
        empresaPuntaje.putArchivo(self.archivoEmpresas)
        empresaPuntaje.leerArchivo()
        emprePun = empresaPuntaje.getDatosArchivo()

        for row1 in iter(emprePun):
            if row1[0] == empresa:
                return row1[7]

        return 0

    def buscarTermino(self,termino):
        empresaDatos = Entidad()
        empresaDatos.putArchivo(self.archivoEmpresas)
        empresaDatos.leerArchivo()
        empresas = empresaDatos.getDatosArchivo()

        for row1 in iter(empresas):
            valor = str(row1[1]).lower()
            valorrta = valor.find(termino.lower())
            if valorrta > 0:
                return row1[0]
        return 0

    def comercioext(self,eid):
        empresaDatos = Entidad()
        empresaDatos.putArchivo(self.archivoEmpresas)
        empresaDatos.leerArchivo()
        empresas = empresaDatos.getDatosArchivo()

        for row2 in iter(empresas):
            if row2[0] == eid:
                return row2[6]


class Enlaces():
    def __init__(self,archivoEnl):
       self.archivoEnlaces = archivoEnl

    def setArchivoEnlaces(self,archivo):
        self.archivoEnlaces= archivo

    def setEnlaces(self,enlaces):
        enlaceValor = Entidad()
        enlaceValor.putArchivo(self.archivoEnlaces)
        enlaceValor.leerArchivo()
        enlaceVal = enlaceValor.getDatosArchivo()

        for row1 in iter(enlaceVal):
            if row1[0] == enlaces:

                if int(row1[3]) >= 90:
                    return "EXCELENTE"
                elif int(row1[3]) >= 80:
                    return "MUY BUENO"
                elif int(row1[3]) >= 70:
                    return "BUENO"
                elif int(row1[3]) >= 60:
                    return "REGULAR"
                elif int(row1[3]) < 60:
                    return "MALO"
                else:
                    return "MALO"


class Paises():
    def __init__(self,archivoCont,archivoRel):
        self.archivoPaisesCont = archivoCont
        self.archivoPaisesRel = archivoRel

    def setArchivoPaisesCont(self,archivo):
        self.archivoPaisesCont = archivo

    def setArchivoPaisesRel(self,archivo):
        self.archivoPaisesRel= archivo

    def setPaises(self,pais1,pais2):

        if pais1==pais2:
            return "LOCAL"
        else:
            paisListaCont = Entidad()
            paisListaCont.putArchivo(self.archivoPaisesCont)
            paisListaCont.leerArchivo()
            paisContinente = paisListaCont.getDatosArchivo()

            paisListaRel = Entidad()
            paisListaRel.putArchivo(self.archivoPaisesRel)
            paisListaRel.leerArchivo()
            paisRelacion = paisListaRel.getDatosArchivo()

            for row1 in iter(paisRelacion):
                if (row1[0] == pais1 and row1[1] == pais2) or (row1[0] == pais2 and row1[1] == pais1):
                    return "LIMITROFE"

            pais1Cont = ""
            pais2Cont = ""
            for row2 in iter(paisContinente):
                if row2[0] == pais1:
                    pais1Cont = row2[1]
                if row2[0] == pais2:
                    pais2Cont = row2[1]

            if pais1Cont.strip() == pais2Cont.strip():
                return "REGIONAL"

            return "MUNDIAL"


class Comentarios():
    def __init__(self, archivoCom):
        self.archivoComentarios = archivoCom

    def setArchivoComentarios(self, archivo):
            self.archivoComentarios = archivo

    def listarComentarios(self):
        comentarioDatos = Entidad()
        comentarioDatos.putArchivo(self.archivoComentarios)
        comentarioDatos.leerArchivo()
        comentarios = comentarioDatos.getDatosArchivo()

        return comentarios

    def buscarTermino(self,termino):
        comentarioDatos = Entidad()
        comentarioDatos.putArchivo(self.archivoComentarios)
        comentarioDatos.leerArchivo()
        comentarios = comentarioDatos.getDatosArchivo()

        for row1 in iter(comentarios):
            valor = str(row1[4]).lower()
            valorrta = valor.find(termino.lower())
            if valorrta > 0:
                return row1[2]
        return 0

class Ventas():
    def __init__(self, archivoVen):
        self.archivoVentas = archivoVen

    def setArchivoVentas(self, archivo):
            self.archivoVentas = archivo

    def listarVentas(self):
        VentaDatos = Entidad()
        VentaDatos.putArchivo(self.archivoVentas)
        VentaDatos.leerArchivo()
        ventas = VentaDatos.getDatosArchivo()
        return ventas

    def buscarTermino(self,termino):
        VentaDatos = Entidad()
        VentaDatos.putArchivo(self.archivoVentas)
        VentaDatos.leerArchivo()
        ventas = VentaDatos.getDatosArchivo()

        for row1 in iter(ventas):
            valor = str(row1[2]).lower()
            valorrta = valor.find(termino.lower())
            if valorrta > 0:
                return row1[0]
        return 0


class Compras():
    def __init__(self, archivoComp):
        self.archivoCompras = archivoComp

    def setArchivoCompras(self, archivo):
            self.archivoCompras = archivo

    def listarCompras(self):
        CompraDatos = Entidad()
        CompraDatos.putArchivo(self.archivoCompras)
        CompraDatos.leerArchivo()
        compras = CompraDatos.getDatosArchivo()
        return compras

    def buscarTermino(self,termino):
        CompraDatos = Entidad()
        CompraDatos.putArchivo(self.archivoCompras)
        CompraDatos.leerArchivo()
        compras = CompraDatos.getDatosArchivo()

        for row1 in iter(compras):
            valor = str(row1[2]).lower()
            valorrta = valor.find(termino.lower())
            if valorrta > 0:
                return row1[0]
        return 0


class Busquedas():
    def __init__(self, archivoBus):
        self.archivoBusquedas = archivoBus

    def setArchivoBusquedas(self, archivo):
            self.archivoBusquedas = archivo

    def listarBusquedas(self):
        BusquedaDatos = Entidad()
        BusquedaDatos.putArchivo(self.archivoBusquedas)
        BusquedaDatos.leerArchivo()
        busquedas = BusquedaDatos.getDatosArchivo()
        return busquedas

    def buscarTermino(self,termino):
        BusquedaDatos = Entidad()
        BusquedaDatos.putArchivo(self.archivoBusquedas)
        BusquedaDatos.leerArchivo()
        busquedas = BusquedaDatos.getDatosArchivo()

        for row1 in iter(busquedas):
            valor = str(row1[1]).lower()
            valorrta = valor.find(termino.lower())
            #print valorrta,termino, row1[1], row1[2]
            if valorrta >= 0:
                return row1[2]
        return 0


