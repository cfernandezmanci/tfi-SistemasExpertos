import clips
import pyClasses
import pyClassesAssertBasicos





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
(defrule empresacompra
  (compra (sid ?sid) (eid ?eid) (nombre ?nombre))
  (compra (sid ?sid2) (eid ?eid2) (nombre ?nombre2))
  (and(test(eq ?nombre ?nombre2)) (test(neq ?sid ?sid2)) (test(neq ?eid ?eid2)) )  
  =>
  (assert(empcomp (sid ?sid) (sid2 ?sid2) (eid ?eid) (eid2 ?eid2) (nombre ?nombre) ))
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

clips.PrintRules()
clips.Run()



print "Resultado - Pool De Compras"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'poolcompras':
        print f.Slots["eid"],f.Slots["nombre"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["categoria"],f.Slots["pais"],f.Slots["compra"]

