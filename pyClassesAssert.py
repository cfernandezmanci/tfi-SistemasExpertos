import clips
import pyClasses

#Clips Clear
clips.Clear()

#Clips Reset
clips.Reset()


'''DEFINICIONES'''
#????
#DIRECTORIO = "/home/christian/tfiClips/"

#Notebook HP BBT
DIRECTORIO = "/home/fernandezc/PycharmProjects/TFIClips/"

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

varCamposTemp = ["enlaceid","fuente","metodo","valor","sid","pid","esid","epid"]


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
    (slot eid2 (type INTEGER))
 """
varClipTemplateComentario = """Es Template busqueda"""

varCamposTemp = ["busid","termino","eid","eid2"]

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




'''HECHOS (FACTS) GENERADOS MEDIANTE REGLAS'''


empcompLista = pyClasses.Entidad()

varClipTemplateNombre = """empcomp"""
varClipTemplateDatos = """
    (slot sid (type INTEGER))
    (slot sid2 (type INTEGER))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))        
    (slot nombre (type STRING))
 """
varClipTemplateComentario = """Es Template EmpresaCompras"""


tempEmpComp = empcompLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empcompLista.leeAssertTemplate(tempEmpComp)


empexpLista = pyClasses.Entidad()

varClipTemplateNombre = """empexp"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot comercioext (type STRING))
 """
varClipTemplateComentario = """Es Template EmpresaExporta"""


tempEmpExp = empexpLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empexpLista.leeAssertTemplate(tempEmpExp)


empventLista = pyClasses.Entidad()

varClipTemplateNombre = """empvent"""
varClipTemplateDatos = """
    (slot pid (type INTEGER))
    (slot eid (type INTEGER))
    (slot pid2 (type INTEGER))
    (slot eid2 (type INTEGER))        
    (slot nombre (type STRING))
 """
varClipTemplateComentario = """Es Template EmpresaVentas"""

tempEmpVent = empventLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empventLista.leeAssertTemplate(tempEmpVent)


empcatpaisLista = pyClasses.Entidad()

varClipTemplateNombre = """empresacatpais"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot categoria (type STRING))
    (slot pais (type STRING))
 """
varClipTemplateComentario = """Template para EmpresasCatPais"""

tempEmpCatPais = empcatpaisLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empcatpaisLista.leeAssertTemplate(tempEmpCatPais)


empcatLista = pyClasses.Entidad()

varClipTemplateNombre = """empresacat"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot categoria (type STRING))
 """
varClipTemplateComentario = """Template para EmpresasCategoria"""

tempempcate = empcatLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empcatLista.leeAssertTemplate(tempempcate)



'''CARGA POOLCOMPRAS '''

poolComprasLista = pyClasses.Entidad()

varClipTemplateNombre = """poolcompras"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot categoria (type STRING))
    (slot pais (type STRING))    
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
    (slot categoria (type STRING))
    (slot pais (type STRING))
    (slot comercioext (type STRING))        
    (slot venta (type STRING))
 """
varClipTemplateComentario = """Es Template Grupo de Exportacion"""

tempGrupoExp = poolComprasLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
grupoExportacionLista.leeAssertTemplate(tempGrupoExp)


''' REGLAS '''

print "REGLAS"


clips.SendCommand("""
(defrule empcatpais
  (empresa (eid ?eid)(nombre ?nombre) (categoria ?categoria) (pais ?pais))         
  (empresa (eid ?eid2)(nombre ?nombre2) (categoria ?categoria2) (pais ?pais2))
   (and(test(eq ?categoria ?categoria2)) (test(neq ?eid ?eid2)) (test(eq ?pais ?pais2)) )  
  =>
  (assert(empresacatpais (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) (pais ?pais) ))
 )
""")


clips.SendCommand("""
(defrule empcat
  (empresa (eid ?eid)(nombre ?nombre) (categoria ?categoria))         
  (empresa (eid ?eid2)(nombre ?nombre2) (categoria ?categoria2))
   (and(test(eq ?categoria ?categoria2)) (test(neq ?eid ?eid2)))  
  =>
  (assert(empresacat (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) ))
 )
""")


clips.SendCommand("""
(defrule empresaventa
  (venta (pid ?pid) (eid ?eid) (nombre ?nombre))
  (venta (pid ?pid2) (eid ?eid2) (nombre ?nombre2))
  (and(test(eq ?nombre ?nombre2)) (test(neq ?pid ?pid2)) (test(neq ?eid ?eid2)) )  
  =>
  (assert(empvent (pid ?pid) (eid ?eid) (pid2 ?pid2) (eid2 ?eid2) (nombre ?nombre) ))
 )
""")

clips.SendCommand("""
(defrule empresacompra
  (compra (sid ?sid) (eid ?eid) (nombre ?nombre))
  (compra (sid ?sid2) (eid ?eid2) (nombre ?nombre2))
  (and(test(eq ?nombre ?nombre2)) (test(neq ?sid ?sid2)) (test(neq ?eid ?eid2)) )  
  =>
  (assert(empcomp (sid ?sid) (sid2 ?sid2) (eid ?eid) (eid2 ?eid2) (nombre ?nombre) ))
 )
""")

clips.SendCommand("""
(defrule empresaexporta
  (empresa (eid ?eid) (comercioext ?comercioext & "EXPORTA"|"EXPIMP")) 
  =>
  (assert(empexp (eid ?eid) (comercioext ?comercioext) ))
 )
""")


clips.SendCommand("""
(defrule poolcompras
  (empresacatpais (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) (pais ?pais) )
  (empcomp (sid ?ecsid) (sid2 ?ecsid2) (eid ?eceid) (eid2 ?eceid2) (nombre ?compra))
  (and(test(eq ?eceid ?eid)) (test(eq ?eceid2 ?eid2))  )  
  =>
  (assert(poolcompras (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) (pais ?pais) (compra ?compra)))
 )
""")



clips.SendCommand("""
(defrule grupoexportacion
  (empresacatpais (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) (pais ?pais) )
  (empvent (pid ?evpid) (eid ?eveid) (pid2 ?evpid2) (eid2 ?eveid2) (nombre ?venta))
  (empexp (eid ?expeid) (comercioext ?comercioext))
  (and(test(eq ?eveid ?eid)) (test(eq ?eveid2 ?eid2)) )
  =>
  (assert(grupoexportacion (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (categoria ?categoria) (pais ?pais) (comercioext ?comercioext) (venta ?venta)))
 )
""")

clips.PrintRules()

clips.Run()


clips.PrintFacts()




'''
print "Lista ! "
lista = clips.FactList()
for f in lista:
    # skip initial fact
    if f.Relation == 'empresacatpais':
        emp_eid = f.Slots['eid']
        emp_nombre = f.Slots['nombre']
        emp_eid2 = f.Slots['eid2']
        emp_nombre2 = f.Slots['nombre']
        print "Emp Cat %s %s %s %s  " % (emp_eid,emp_nombre,emp_eid2,emp_nombre2)


print "Lista ! "
lista = clips.FactList()
for f in lista:
    # skip initial fact
    if f.Relation == 'empvent':
        emp_eid = f.Slots['eid']
        emp_nombre = f.Slots['pid']
        emp_eid2 = f.Slots['eid2']
        emp_nombre2 = f.Slots['pid2']
        print "Venta %s %s %s %s  " % (emp_eid,emp_nombre,emp_eid2,emp_nombre2)

print "Lista ! "
lista = clips.FactList()
for f in lista:
    # skip initial fact
    if f.Relation == 'empexp':
        emp_eid = f.Slots['eid']
        emp_nombre = f.Slots['comercioext']
        print "EmpExport %s %s  " % (emp_eid,emp_nombre)


print "Lista ! "
lista = clips.FactList()
for f in lista:
    # skip initial fact
    if f.Relation == 'grupoexportacion':
        emp_eid = f.Slots['eid']
        emp_nombre = f.Slots['comercioext']
        print "Grupo Exp %s %s  " % (emp_eid,emp_nombre)


'''

