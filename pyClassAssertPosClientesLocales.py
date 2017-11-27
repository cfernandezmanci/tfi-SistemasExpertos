import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos


posClientesLocalesLista = pyClasses.Entidad()

varClipTemplateNombre = """posclienteslocales"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot pais (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais2 (type STRING))
    (slot tipopais (type STRING))    
    (slot venta (type STRING))
    (slot valor (type STRING))
    (slot enlaceid (type STRING))
 """
varClipTemplateComentario = """Es Template Posibles Clientes Locales"""

tempPosCliLoc = posClientesLocalesLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posClientesLocalesLista.leeAssertTemplate(tempPosCliLoc)




''' REGLAS '''
print "REGLAS"


clips.SendCommand("""
(defrule posclienteslocales
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) )         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2))
  (enlace (epid ?epid)(esid ?esid)(valor ?valor) (pid ?pid) (fuente ?fuente & "V")  (enlaceid ?enlaceid))
   (and(test(eq ?pais ?pais2)) (test(neq ?eid ?eid2)) (test(eq ?epid ?eid)) (test(eq ?esid ?eid2)) )  
  =>
  (assert(posclienteslocales (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (venta ?pid) (valor ?valor)  (enlaceid ?enlaceid) ))
 )
""")

clips.PrintRules()
clips.Run()



print "Resultado - Posibles Clientes Locales"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'posclienteslocales':
        valorEnl = pyFormulas.formuValorEnlace(f.Slots["enlaceid"])
        if valorEnl == "EXCELENTE" or valorEnl == "MUY BUENO":
            print f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],"LOCAL",f.Slots["venta"]

