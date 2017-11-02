import clips
import csv
import pyClasses




'''DEFINICIONES'''

DIRECTORIO = "/home/christian/tfiClips/"

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

#clips.PrintFacts()

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

varCamposTemp = ["enlaceid","fuente","metodo","valor","sid","pid","esid","epid"]


tempEnlace = enlaceLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
enlaceLista.leeAssertTemplate(tempEnlace)
enlaceLista.putAssertTemplate(tempEnlace,varCamposTemp,enlace)


'''HECHOS (FACTS) GENERADOS MEDIANTE REGLAS'''

'''CARGA POOLCOMPRAS '''


poolComprasLista = pyClasses.Entidad()

varClipTemplateNombre = """poolcompras"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot compra (type STRING))
 """
varClipTemplateComentario = """Es Template poolCompras"""

tempPoolCompras = poolComprasLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
poolComprasLista.leeAssertTemplate(tempPoolCompras)

'''CARGA GRUPOEXPORTACION '''

grupoExportacionLista = pyClasses.Entidad()

varClipTemplateNombre = """grupoexportacion"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais (type STRING))
    (slot categoria (type STRING))
    (slot comercioext (type STRING))        
    (slot venta (type STRING))
 """
varClipTemplateComentario = """Es Template Grupo de Exportacion"""

tempGrupoExp = poolComprasLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
grupoExportacionLista.leeAssertTemplate(tempGrupoExp)


#clips.PrintFacts()
clips.Clear()