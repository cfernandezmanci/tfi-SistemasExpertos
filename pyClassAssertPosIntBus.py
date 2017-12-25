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





#Posible Interes Busqueda Temp

posIntBus = pyClasses.Entidad()

varClipTemplateNombre = """posintbus"""
varClipTemplateDatos = """
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot pais (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))
    (slot pais2 (type STRING))
    (slot comercioext (type STRING))
 """
varClipTemplateComentario = """Es Template Posible Interes Busqueda Temp"""

tempPosIntBus = posIntBus.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntBus.leeAssertTemplate(tempPosIntBus)



''' REGLAS '''
print "REGLAS"


clips.SendCommand("""
(defrule posclientesexteriores
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) (comercioext ?comercioext & "EXPORTA"|"EXPIMP") )         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2) (comercioext ?comercioext2 & "EXPORTA"|"EXPIMP"))
  (and(test(neq ?eid ?eid2)) (test(eq ?comercioext ?comercioext2)) )  
  =>
  (assert(posintbus (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (comercioext ?comercioext) ))
 )
""")


clips.PrintRules()
clips.Run()

print "Resultado - Posibles Clientes Exteriores CLIPs"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'posintbus':
        print f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],f.Slots["comercioext"]


print "Resultado - Posibles Clientes Exteriores en Empresas"
lista = clips.FactList()
for f in lista:
    if f.Relation == 'posintbus':
        valorempresa = f.Slots["nombre"].split()
        for buscaterm in valorempresa:
            valor = pyFormulas.formuTerminoBusqueda("BUSQUEDAS",buscaterm)
            if valor > 0 and valor <> f.Slots["eid"] and f.Slots["eid2"] == valor:
            #Encontro valores coincidentes en la busqueda
                tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])
                print  tipoPais,f.Slots["comercioext"],f.Slots["eid"],valor




print "Resultado - Posibles Clientes Exteriores en Ventas"
lista = clips.FactList()
lista2 = clips.FactList()


for f in lista:
    if f.Relation == 'posintbus':
        #print f.Slots["eid"] , f.Slots["eid2"]
        for g in lista2:
            if g.Relation == 'venta':
                if f.Slots["eid"] == g.Slots["eid"]:
                    #print f.Slots["eid"],g.Slots["eid"],g.Slots["nombre"]
                    valor = pyFormulas.formuTerminoBusqueda("BUSQUEDAS", g.Slots["nombre"])

                    if valor > 0 and valor <> f.Slots["eid"]  and valor == f.Slots["eid2"]:
                        # Encontro valores coincidentes en la busqueda
                        tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])
                        print  tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],g.Slots["pid"]



print "Resultado - Posibles Clientes Exteriores en Compras"
lista = clips.FactList()
lista2 = clips.FactList()

for f in lista:
    if f.Relation == 'posintbus':
        #print f.Slots["eid"] , f.Slots["eid2"]
        for g in lista2:
            if g.Relation == 'compra':
                if f.Slots["eid"] == g.Slots["eid"]:
                    #print f.Slots["eid"],g.Slots["eid"],g.Slots["nombre"]
                    valor = pyFormulas.formuTerminoBusqueda("BUSQUEDAS", g.Slots["nombre"])

                    if valor > 0 and valor <> f.Slots["eid"]  and valor == f.Slots["eid2"]:
                        # Encontro valores coincidentes en la busqueda
                        tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])
                        print  tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],g.Slots["sid"]