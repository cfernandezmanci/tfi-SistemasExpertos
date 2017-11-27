import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos



alianzaEstrategicaLista = pyClasses.Entidad()

varClipTemplateNombre = """alianzaestrategica"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot pais (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais2 (type STRING))
    (slot categoria (type STRING)) 
    (slot tipopais (type STRING))   
    (slot venta (type STRING))
    (slot compra (type STRING))
 """
varClipTemplateComentario = """Es Template Alianza Estrategica"""

tempAliEst = alianzaEstrategicaLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
alianzaEstrategicaLista.leeAssertTemplate(tempAliEst)

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

empcatLista = pyClasses.Entidad()

varClipTemplateNombre = """empresacat"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot pais (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais2 (type STRING))        
    (slot categoria (type STRING))
 """
varClipTemplateComentario = """Template para EmpresasCategoria"""

tempempcate = empcatLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
empcatLista.leeAssertTemplate(tempempcate)




''' REGLAS '''
print "REGLAS"


clips.SendCommand("""
(defrule empcat
  (empresa (eid ?eid)(nombre ?nombre) (categoria ?categoria) (pais ?pais) )         
  (empresa (eid ?eid2)(nombre ?nombre2) (categoria ?categoria2) (pais ?pais2) )
   (and(test(eq ?categoria ?categoria2)) (test(neq ?eid ?eid2)) )  
  =>
  (assert(empresacat (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (categoria ?categoria) ))
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
(defrule alienzaestrategica
  (empresacat (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (categoria ?categoria))
  (empvent (pid ?evpid) (eid ?eveid) (pid2 ?evpid2) (eid2 ?eveid2) (nombre ?venta))
  (empcomp (sid ?ecsid) (sid2 ?ecsid2) (eid ?eceid) (eid2 ?eceid2) (nombre ?compra))  
  (test(eq ?eveid ?eid)) (test(eq ?eveid2 ?eid2)) (test(eq ?eceid ?eid)) (test(eq ?eceid2 ?eid2))
  =>
  (assert(alianzaestrategica (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (categoria ?categoria) (venta ?venta) (compra ?compra)  )) 
 )
""")


clips.PrintRules()
clips.Run()



print "Resultado - Alianz Estraategica"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'alianzaestrategica':
        tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"],f.Slots["pais2"])
        if tipoPais == "LOCAL" or tipoPais == "LIMITROFE":
            print f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],f.Slots["categoria"],tipoPais,f.Slots["venta"],f.Slots["compra"]


