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


#NPC MyHome  Local
import csv
DIRECTORIO = "/home/christian/tfiClips/"

#Cargo Enlaces (Vtas Cpras)

enlaceLista = pyClasses.Entidad()
enlaceLista.putArchivo(DIRECTORIO + "enlaces_1.csv")
enlaceLista.leerArchivo()
enlace = enlaceLista.getDatosArchivo()



with open(DIRECTORIO+"posibleinteresvisitas.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)



    print "Resultado - interes Visitas Gral CLIPs"
    lista = clips.FactList()
    for f in lista:
        if f.Relation == 'posintvisgral':
            #print f.Slots["tipovisita"],f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["comercioext"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],f.Slots["comercioext2"]
            tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])

            if tipoPais == "LOCAL":
                print "LOCAL",f.Slots["tipovisita"], f.Slots["eid"],f.Slots["eid2"]
                if f.Slots["tipovisita"] =="EMPRESA":
                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],""])

                if f.Slots["tipovisita"] == "VENTA":
                    for data in enlace:
                        if data[1] == "V" and data[6] == f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                            wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[4]])

                if f.Slots["tipovisita"] == "COMPRA":
                    for enlace in data:
                        if data[1] == "C" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                            wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[5]])

            if tipoPais == "LIMITROFE":
                if (f.Slots["comercioext"] in ("EXPORTA","IMPORTA","EXPIMP"))  and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):

                    if f.Slots["tipovisita"] == "EMPRESA":
                        print "LIMITROFE", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"],""
                        wr.writerow([f.Slots["tipovisita"],tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],""])

                        if f.Slots["tipovisita"] == "VENTA":
                            for data in enlace:
                                if data[1] == "V" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[4]])

                        if f.Slots["tipovisita"] == "COMPRA":
                            for enlace in data:
                                if data[1] == "C" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[5]])



            if tipoPais == "REGIONAL":
                if (f.Slots["comercioext"] in ("EXPORTA", "IMPORTA", "EXPIMP")) and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):

                    if f.Slots["tipovisita"] == "EMPRESA":
                        print "REGIONAL", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"],""
                        wr.writerow([f.Slots["tipovisita"],tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],""])

                        if f.Slots["tipovisita"] == "VENTA":
                            for data in enlace:
                                if data[1] == "V" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[4]])

                        if f.Slots["tipovisita"] == "COMPRA":
                            for enlace in data:
                                if data[1] == "C" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[5]])


            if tipoPais == "MUNDIAL":
                if (f.Slots["comercioext"] in ("EXPORTA", "IMPORTA", "EXPIMP"))  and (f.Slots["comercioext2"] in ("EXPORTA", "IMPORTA", "EXPIMP")):
                    if f.Slots["tipovisita"] == "EMPRESA":
                        print "MUNDIAL", f.Slots["tipovisita"], f.Slots["eid"], f.Slots["eid2"],""
                        wr.writerow([f.Slots["tipovisita"],tipoPais,f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],""])

                        if f.Slots["tipovisita"] == "VENTA":
                            for data in enlace:
                                if data[1] == "V" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[4]])

                        if f.Slots["tipovisita"] == "COMPRA":
                            for enlace in data:
                                if data[1] == "C" and data[6] ==  f.Slots["eid"] and data[7] == f.Slots["eid2"]:
                                    wr.writerow([f.Slots["tipovisita"], tipoPais, f.Slots["comercioext"], f.Slots["eid"], f.Slots["eid2"],data[5]])


myfile.close()
