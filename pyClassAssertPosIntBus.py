import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos


#Posible Interes Busqueda Empresas

posIntBusEmp = pyClasses.Entidad()

varClipTemplateNombre = """posintbusemp"""
varClipTemplateDatos = """
    (slot tipopais (type STRING))
    (slot comercioext (type STRING))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))
 """
varClipTemplateComentario = """Es Template Posible Interes Busqueda Empresas"""

tempPosIntBusEmp = posIntBusEmp.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntBusEmp.leeAssertTemplate(tempPosIntBusEmp)


#Posible Interes Busqueda Compras

posIntBusComp = pyClasses.Entidad()

varClipTemplateNombre = """posintbuscomp"""
varClipTemplateDatos = """
    (slot tipopais (type STRING))
    (slot comercioext (type STRING))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))
    (slot sid (type INTEGER))
 """
varClipTemplateComentario = """Es Template Posible Interes Busqueda Compras"""

tempPosIntBusComp = posIntBusComp.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntBusComp.leeAssertTemplate(tempPosIntBusComp)


#Posible Interes Busqueda Ventas

posIntBusVent = pyClasses.Entidad()

varClipTemplateNombre = """posintbusvent"""
varClipTemplateDatos = """
    (slot tipopais (type STRING))
    (slot comercioext (type STRING))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))
    (slot pid (type INTEGER))
 """
varClipTemplateComentario = """Es Template Posible Interes Busqueda Ventas"""

tempPosIntBusVent = posIntBusVent.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntBusVent.leeAssertTemplate(tempPosIntBusVent)


''' REGLAS '''
print "REGLAS"


clips.SendCommand("""
(defrule posclientesexteriores
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) (comercioext ?comercioext & "EXPORTA"|"EXPIMP") )         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2) (comercioext ?comercioext2 & "EXPORTA"|"EXPIMP"))
  (and(test(neq ?eid ?eid2)) (test(eq ?comercioext ?comercioext2)) )  
  =>
  (assert(posintbus (eid ?eid) (eid2 ?eid2) (comercioext ?comercioext) ))
 )
""")
