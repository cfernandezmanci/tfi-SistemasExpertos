import clips
import pyClasses
import pyFormulas

#Clips Clear
clips.Clear()

#Clips Reset
clips.Reset()

'''DEFINICION FUNCIONES'''

clips.RegisterPythonFunction(pyFormulas.formuUbicacionEmpresaPais)


'''DEFINICIONES'''

#NPC MyHome  Local
DIRECTORIO = "/home/christian/tfiClips/"


#Notebook Dell Local
#DIRECTORIO = "/home/christian/Documents/TFI/clips/"

#Notebook HP BBT Local
#DIRECTORIO = "/home/fernandezc/PycharmProjects/TFIClips/"



'''CARGA EMPRESAS '''

emplista = pyClasses.Entidad()
emplista.putArchivo(DIRECTORIO + "empresas_1.csv")
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


'''CARGA COMPRAS '''

compralista = pyClasses.Entidad()
compralista.putArchivo(DIRECTORIO + "servicios_1.csv")
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


ventaLista = pyClasses.Entidad()
ventaLista.putArchivo(DIRECTORIO + "productos_1.csv")
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


'''CARGA ENLACES '''


enlaceLista = pyClasses.Entidad()
enlaceLista.putArchivo(DIRECTORIO + "enlaces_1.csv")
enlaceLista.leerArchivo()
enlace = enlaceLista.getDatosArchivo()

varClipTemplateNombre = """enlace"""
varClipTemplateDatos = """
    (slot enlaceid (type INTEGER))
    (slot fuente (type STRING))
    (slot metodo (type STRING))
    (slot valor (type STRING))
    (slot sid (type INTEGER))
    (slot pid (type INTEGER))
    (slot epid (type INTEGER))
    (slot esid (type INTEGER))
 """
varClipTemplateComentario = """Es Template Enlace"""

varCamposTemp = ["enlaceid","fuente","metodo","valor","sid","pid","epid","esid"]


tempEnlace = enlaceLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
enlaceLista.leeAssertTemplate(tempEnlace)
enlaceLista.putAssertTemplate(tempEnlace,varCamposTemp,enlace)


'''CARGA COMENTARIOS '''

comentariolista = pyClasses.Entidad()
comentariolista.putArchivo(DIRECTORIO + "comentarios_1.csv")
comentariolista.leerArchivo()
coment = comentariolista.getDatosArchivo()

varClipTemplateNombre = """comentario"""
varClipTemplateDatos = """
    (slot comid (type INTEGER))
    (slot tipo (type STRING))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))
    (slot mensaje (type STRING))
 """
varClipTemplateComentario = """Es Template Comentarios"""

varCamposTemp = ["comid","tipo","eid","eid2","mensaje"]

tempComentario = comentariolista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
comentariolista.leeAssertTemplate(tempComentario)
comentariolista.putAssertTemplate(tempComentario,varCamposTemp,coment)

'''CARGA BUSQUEDAS'''

busquedalista = pyClasses.Entidad()
busquedalista.putArchivo(DIRECTORIO + "busquedas_1.csv")
busquedalista.leerArchivo()
busq = busquedalista.getDatosArchivo()

varClipTemplateNombre = """busqueda"""
varClipTemplateDatos = """
    (slot busid (type INTEGER))
    (slot termino (type STRING))
    (slot eid (type INTEGER))
 """
varClipTemplateComentario = """Es Template busqueda"""

varCamposTemp = ["busid","termino","eid"]

tempBusqueda = busquedalista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
busquedalista.leeAssertTemplate(tempBusqueda)
busquedalista.putAssertTemplate(tempBusqueda,varCamposTemp,busq)


'''CARGA ACCESOS'''

accesolista = pyClasses.Entidad()
accesolista.putArchivo(DIRECTORIO + "accesos_1.csv")
accesolista.leerArchivo()
acces = accesolista.getDatosArchivo()


varClipTemplateNombre = """accesos"""
varClipTemplateDatos = """
    (slot accid (type INTEGER))
    (slot fecha (type STRING))
    (slot eid (type INTEGER))
 """
varClipTemplateComentario = """Es Template acceso"""

varCamposTemp = ["accid","fecha","eid"]

tempAcceso = accesolista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
accesolista.leeAssertTemplate(tempAcceso)
accesolista.putAssertTemplate(tempAcceso,varCamposTemp,acces)


'''CARGA VISITAS'''

visitalista = pyClasses.Entidad()
visitalista.putArchivo(DIRECTORIO + "reg_empresavisitada_1.csv")
visitalista.leerArchivo()
visita = visitalista.getDatosArchivo()


varClipTemplateNombre = """visitas"""
varClipTemplateDatos = """
    (slot vid (type INTEGER))
    (slot eid (type INTEGER))
    (slot veid (type INTEGER))
    (slot tipo (type STRING))
    (slot fecha (type STRING))
 """
varClipTemplateComentario = """Es Template visitas"""

varCamposTemp = ["vid","eid","veid","tipo","fecha"]

tempvisita = visitalista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
visitalista.leeAssertTemplate(tempvisita)
visitalista.putAssertTemplate(tempvisita,varCamposTemp,visita)




