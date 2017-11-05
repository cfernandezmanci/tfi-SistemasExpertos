import clips
import csv
import pyClasses




'''DEFINICIONES'''

DIRECTORIO = "/home/christian/tfiClips/"


def formuPuntajeEmpresa(eid):
    empresaAnalisis = pyClasses.Empresas(DIRECTORIO+"empresas_1.csv")
    valor = empresaAnalisis.setEmpresa(eid)
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

def formuTerminoBusqueda(tipo,termino):
    '''FORMULA BUSQUEDA'''



