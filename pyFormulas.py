import clips
import csv
import pyClasses


'''DEFINICIONES'''


#NPC MyHome  Local
DIRECTORIO = "/home/christian/tfiClips/"


#Notebook Dell Local
#DIRECTORIO = "/home/christian/Documents/TFI/clips/"

#Notebook HP BBT Local
#DIRECTORIO = "/home/fernandezc/PycharmProjects/TFIClips/"


def formuPuntajeEmpresa(eid):
    empresaAnalisis = pyClasses.Empresas(DIRECTORIO+"empresas_1.csv")
    valor = empresaAnalisis.setEmpresa(eid)
    return valor

def formuComercioExtEmpresa(eid):
    empresaAnalisis = pyClasses.Empresas(DIRECTORIO+"empresas_1.csv")
    valor = empresaAnalisis.comercioext(eid)
    return valor


def formuValorEnlace(enid):
    enlaceAnalisis = pyClasses.Enlaces(DIRECTORIO+"enlaces_1.csv")
    valor = enlaceAnalisis.setEnlaces(enid)
    return valor

def formuUbicacionEmpresaPais(pais1,pais2):
    '''FORMULA: PAISES'''
    paisAnalisis = pyClasses.Paises(DIRECTORIO+"paises.csv",DIRECTORIO+"paisesrelacion.csv")
    valor = paisAnalisis.setPaises(pais1,pais2)
    return valor

def formuTerminoBusqueda(entidad,termino):
    '''FORMULA BUSQUEDA'''
    if entidad == "COMENTARIOS":
        comentarioAnalisis = pyClasses.Comentarios(DIRECTORIO+"comentarios_1.csv")
        valor = comentarioAnalisis.buscarTermino(termino)
        return valor

    if entidad == "EMPRESAS":
        empresaAnalisis = pyClasses.Empresas(DIRECTORIO + "empresas_1.csv")
        valor = empresaAnalisis.buscarTermino(termino)
        return valor

    if entidad == "VENTAS":
        ventaAnalisis = pyClasses.Ventas(DIRECTORIO + "productos_1.csv")
        valor = ventaAnalisis.buscarTermino(termino)
        return valor

    if entidad == "COMPRAS":
        compraAnalisis = pyClasses.Compras(DIRECTORIO + "servicios_1.csv")
        valor = compraAnalisis.buscarTermino(termino)
        return valor

    if entidad == "BUSQUEDAS":
        busquedaAnalisis = pyClasses.Busquedas(DIRECTORIO + "busquedas_1.csv")
        valor = busquedaAnalisis.buscarTermino(termino)
        return valor