import clips
import csv
import sys

#Clips Clear
clips.Clear()

#Clips Reset
clips.Reset()

temp = clips.BuildTemplate("empresa","""
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot tipo (type STRING))
    (slot categoria (type STRING))
    (slot ciudad (type STRING))
    (slot pais (type STRING))
    (slot comercioext (type STRING))
    (slot puntaje (type INTEGER))
 """, "Template para empresas")


tcomp = clips.BuildTemplate("compra","""
    (slot sid (type INTEGER))
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
 """, "Template para compras")


tempcomp = clips.BuildTemplate("empcomp","""
    (slot sid (type INTEGER))
    (slot sid2 (type INTEGER))
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))        
    (slot nombre (type STRING))
 """, "Template para empresas y compras")

tempcatp = clips.BuildTemplate("empresacatpais","""
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot categoria (type STRING))
    (slot pais (type STRING))
 """, "Template para empresas y cat")


tpoolcomp = clips.BuildTemplate("poolcompras","""
    (slot eid (type INTEGER))
    (slot nombre (type STRING))
    (slot eid2 (type INTEGER))
    (slot nombre2 (type STRING))        
    (slot compra (type STRING))
 """, "Template para pool de compras")


#Visualizacion Facts Empresas
print temp.PPForm()
print "*** Vizualizacion Template Empresas"

#Visualizacion Facts Compras
print tcomp.PPForm()
print "*** Vizualizacion Template Compras"


f = open('/home/christian/tfiClips/empresas_1.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        f1=clips.Fact(temp)
        f1.Slots['eid'] = row[0]
        f1.Slots['nombre'] = row[1]
        f1.Slots['tipo'] = row[2]
        f1.Slots['categoria'] = row[3]
        f1.Slots['ciudad'] = row[4]
        f1.Slots['pais'] = row[5]
        f1.Slots['comercioext'] = row[6]
        f1.Slots['puntaje'] = row[7]
        f1.Assert()
finally:
    f.close()

print "*** Fin Bucle Carga FACTs Empresas"



fileComp = open('/home/christian/tfiClips/servicios_1.csv', 'rt')
try:
    reader = csv.reader(fileComp)
    for row in reader:
        fc=clips.Fact(tcomp)
        fc.Slots['sid'] = row[0]
        fc.Slots['eid'] = row[1]
        fc.Slots['nombre'] = row[2]
        fc.Assert()
finally:
    fileComp.close()

print "*** Fin Bucle Carga FACTs Compras"


clips.SendCommand("""
(defrule empcatpais
  (empresa  (eid ?eid)(nombre ?nombre) (categoria ?categoria) (pais ?pais))         
  (empresa  (eid ?eid2)(nombre ?nombre2) (categoria ?categoria2) (pais ?pais2))
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
  (assert(poolcompras (eid ?eid) (nombre ?nombre) (eid2 ?eid2) (nombre2 ?nombre2) (compra ?compra)))
 )
""")

#Visualizacion Reglas
#clips.PrintRules()
#Visualiza Facts
#clips.PrintFacts()

clips.Run()

listaempresas = clips.FactList()
for f in listaempresas:
    # skip initial fact
    if f.Relation == 'empresacatpais':
        emp_eid = f.Slots['eid']
        emp_nombre = f.Slots['nombre']
        emp_eid2 = f.Slots['eid2']
        emp_nombre2 = f.Slots['nombre2']
        print "Empresa %s %s - %s %s " % (emp_eid,emp_nombre,emp_eid2,emp_nombre2)


li = clips.FactList()
for f in li:
    # skip initial fact
    if f.Relation == 'poolcompras':
        pool_eid = f.Slots['eid']
        pool_nombre = f.Slots['nombre']
        pool_eid2 = f.Slots['eid2']
        pool_nombre2 = f.Slots['nombre2']
        pool_compra = f.Slots['compra']
        print "Pool. %s - %s %s " % (pool_nombre,pool_nombre2, pool_compra)



print "*** Fin de Programa"



