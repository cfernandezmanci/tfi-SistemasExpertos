import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos


posClientesLimitrofesLista = pyClasses.Entidad()

varClipTemplateNombre = """posclientes"""
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
varClipTemplateComentario = """Es Template Posibles Clientes"""

tempPosCliLoc = posClientesLimitrofesLista.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posClientesLimitrofesLista.leeAssertTemplate(tempPosCliLoc)


''' REGLAS '''
print "REGLAS"



clips.SendCommand("""
(defrule posclientesexteriores
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) (comercioext ?comercioext & "EXPORTA"|"EXPIMP") )         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2) (comercioext ?comercioext & "EXPORTA"|"EXPIMP"))
  (enlace (epid ?epid)(esid ?esid)(valor ?valor) (pid ?pid) (fuente ?fuente & "V")  (enlaceid ?enlaceid))
  (and(test(neq ?pais ?pais2)) (test(neq ?eid ?eid2)) (test(eq ?epid ?eid)) (test(eq ?esid ?eid2)))  
  =>
  (assert(posclientes (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (venta ?pid) (valor ?valor)  (enlaceid ?enlaceid) ))
 )
""")


clips.SendCommand("""
(defrule posclienteslocales
  (empresa (eid ?eid)(nombre ?nombre) (pais ?pais) )         
  (empresa (eid ?eid2)(nombre ?nombre2) (pais ?pais2))
  (enlace (epid ?epid)(esid ?esid)(valor ?valor) (pid ?pid) (fuente ?fuente & "V")  (enlaceid ?enlaceid))
   (and(test(eq ?pais ?pais2)) (test(neq ?eid ?eid2)) (test(eq ?epid ?eid)) (test(eq ?esid ?eid2)) )  
  =>
  (assert(posclientes (eid ?eid) (nombre ?nombre) (pais ?pais) (eid2 ?eid2) (nombre2 ?nombre2) (pais2 ?pais2) (venta ?pid) (valor ?valor)  (enlaceid ?enlaceid) ))
 )
""")


clips.PrintRules()
clips.Run()


#NPC MyHome  Local
import csv
DIRECTORIO = "/home/christian/tfiClips/"

with open(DIRECTORIO+"posiblesclientes.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    print "Resultado - Posibles Clientes Exteriores"
    lista = clips.FactList()
    for f in lista:
        if f.Relation == 'posclientes':
            valorEnl = pyFormulas.formuValorEnlace(f.Slots["enlaceid"])
            if valorEnl == "EXCELENTE" or valorEnl == "MUY BUENO":
                tipoPais = pyFormulas.formuUbicacionEmpresaPais(f.Slots["pais"], f.Slots["pais2"])
                valorComExtEmp1 = pyFormulas.formuComercioExtEmpresa(f.Slots["eid"])
                valorComExtEmp2 = pyFormulas.formuComercioExtEmpresa(f.Slots["eid2"])

                if tipoPais == "LOCAL":
                    print f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],tipoPais,f.Slots["venta"]
                    wr.writerow([f.Slots["eid"],f.Slots["eid2"],tipoPais,valorComExtEmp2,f.Slots["enlaceid"]])

                if tipoPais == "LIMITROFE":
                    if (valorComExtEmp1 in ("EXPORTA","IMPORTA","EXPIMP")) and (valorComExtEmp2 in ("EXPORTA","IMPORTA","EXPIMP")):
                        print f.Slots["eid"],f.Slots["nombre"],f.Slots["pais"],f.Slots["eid2"],f.Slots["nombre2"],f.Slots["pais2"],tipoPais,f.Slots["venta"]
                        wr.writerow([f.Slots["eid"], f.Slots["eid2"], tipoPais, valorComExtEmp2, f.Slots["enlaceid"]])

                if tipoPais == "REGIONAL":
                    if (valorComExtEmp1 in ("EXPORTA","IMPORTA","EXPIMP")) and (valorComExtEmp2 in ("EXPORTA","IMPORTA","EXPIMP")):
                        print f.Slots["eid"], f.Slots["nombre"], f.Slots["pais"], f.Slots["eid2"], f.Slots["nombre2"], f.Slots["pais2"], tipoPais, f.Slots["venta"]
                        wr.writerow([f.Slots["eid"], f.Slots["eid2"], tipoPais,valorComExtEmp2 , f.Slots["enlaceid"]])

                if tipoPais == "MUNDIAL":
                    if (valorComExtEmp1 in ("EXPORTA","IMPORTA","EXPIMP")) and (valorComExtEmp2 in ("EXPORTA","IMPORTA","EXPIMP")):
                        print f.Slots["eid"], f.Slots["nombre"], f.Slots["pais"], f.Slots["eid2"], f.Slots["nombre2"], f.Slots["pais2"], tipoPais, f.Slots["venta"]
                        wr.writerow([f.Slots["eid"], f.Slots["eid2"], tipoPais, valorComExtEmp2, f.Slots["enlaceid"]])



myfile.close()
