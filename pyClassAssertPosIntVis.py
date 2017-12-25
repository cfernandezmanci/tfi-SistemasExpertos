import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos




#Posible Interes  Visitadas Gral

posIntVisGral = pyClasses.Entidad()

varClipTemplateNombre = """posintvisgral"""
varClipTemplateDatos = """
    (slot tipovisita (type STRING))    
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot pais (type STRING))
    (slot comercioext (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais2 (type STRING))
    (slot comercioext2 (type STRING))
        
 """
varClipTemplateComentario = """Es Template Posible Interes Visitas Gral"""

tempposIntVisGral = posIntVisGral.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntVisGral.leeAssertTemplate(tempposIntVisGral)


''' REGLAS '''
print "REGLAS"


clips.SendCommand("""
(defrule posclientesvisitas
  (visitas (eid ?eid0) (veid ?veid) (tipo ?tipovisita) )
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) (comercioext ?comercioext ))         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2) (comercioext ?comercioext2 ))
  (and (test(eq ?eid0 ?eid)) (test(eq ?veid ?eid2)) (test(neq ?eid ?eid2))  )  
  =>
  (assert(posintvisgral (tipovisita ?tipovisita) (eid ?eid) (nombre ?nombre) (pais ?pais) (comercioext ?comercioext)
  (eid2 ?eid2) (nombre2 ?nombre2)  (pais2 ?pais2) (comercioext2 ?comercioext2) ))
  
 )
""")


clips.PrintRules()

clips.Run()


print "Resultado - Visitas CLIPs"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'visitas':
        print f.Slots["vid"],f.Slots["eid"],f.Slots["veid"],f.Slots["tipo"],f.Slots["fecha"]

print "--------------------------------------------"

print "Resultado - interes Visitas Gral CLIPs"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'posintvisgral':
        #print f.Slots["tipovisita"],f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["comercioext"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],f.Slots["comercioext2"]
        tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])

        if tipoPais == "LOCAL":
            print "LOCAL",f.Slots["tipovisita"], f.Slots["eid"],f.Slots["eid2"]

        if tipoPais == "LIMITROFE":
            if (f.Slots["comercioext"] in ("EXPORTA","IMPORTA","EXPIMP"))  and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):
                print "LIMITROFE", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"]

        if tipoPais == "REGIONAL":
            if (f.Slots["comercioext"] in ("EXPORTA", "IMPORTA", "EXPIMP")) and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):
                print "REGIONAL", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"]

        if tipoPais == "MUNDIAL":
            if (f.Slots["comercioext"] in ("EXPORTA", "IMPORTA", "EXPIMP"))  and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):
                print "MUNDIAL", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"]



