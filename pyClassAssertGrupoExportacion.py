import clips
import pyClasses
import pyClassesAssertBasicos



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

tempGrupoExp = grupoExportacionLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
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
(defrule empresaventa
  (venta (pid ?pid) (eid ?eid) (nombre ?nombre))
  (venta (pid ?pid2) (eid ?eid2) (nombre ?nombre2))
  (and(test(eq ?nombre ?nombre2)) (test(neq ?pid ?pid2)) (test(neq ?eid ?eid2)) )  
  =>
  (assert(empvent (pid ?pid) (eid ?eid) (pid2 ?pid2) (eid2 ?eid2) (nombre ?nombre) ))
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



print "Resultado - Grupo de Exportacion"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'grupoexportacion':
        print f.Slots["eid"],f.Slots["nombre"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["categoria"],f.Slots["pais"],f.Slots["comercioext"],f.Slots["venta"]

