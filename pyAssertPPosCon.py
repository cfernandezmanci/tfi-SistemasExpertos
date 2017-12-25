import clips
import pyClasses
import pyFormulas
import pyClassesAssertBasicos

#Posible Interes Empresas Visitadas

posIntConEmp = pyClasses.Entidad()

varClipTemplateNombre = """posintcongral"""
varClipTemplateDatos = """
    (slot termino (type STRING))
    (slot tipocontacto (type STRING))    
    (slot eid (type INTEGER))
    (slot eid2 (type INTEGER))
 """
varClipTemplateComentario = """Es Template Posible Interes Empresas Contacto"""

tempposIntConEmp = posIntConEmp.addAssertTemplate(varClipTemplateNombre,varClipTemplateDatos,varClipTemplateComentario)
posIntConEmp.leeAssertTemplate(tempposIntConEmp)

clips.Run()


print "Resultado - Contactos CLIPs"

lista = clips.FactList()


#Cargo Ventas
DIRECTORIO = "/home/christian/tfiClips/"
ventaListaTemp = pyClasses.Entidad()
ventaListaTemp.putArchivo(DIRECTORIO + "productos_1.csv")
ventaListaTemp.leerArchivo()
ventaTemp = ventaListaTemp.getDatosArchivo()

#Cargo Compras
compraListaTemp = pyClasses.Entidad()
compraListaTemp.putArchivo(DIRECTORIO + "servicios_1.csv")
compraListaTemp.leerArchivo()
compraTemp = compraListaTemp.getDatosArchivo()


#NPC MyHome  Local
import csv
DIRECTORIO = "/home/christian/tfiClips/"

with open(DIRECTORIO+"posibleinterescontactos.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)



    for f in lista:
        if f.Relation == 'comentario':
            print "Contacto EMPRESA"
            #print f.Slots["comid"],f.Slots["tipo"],f.Slots["eid"],f.Slots["eid2"],f.Slots["mensaje"]
            print f.Slots["mensaje"], f.Slots["eid"], f.Slots["eid2"]
            wr.writerow([f.Slots["mensaje"], f.Slots["eid"], f.Slots["eid2"],"",""])

            #Split mensaje - Separo por termino para la busqueda
            splittermino = f.Slots["mensaje"]
            data = splittermino.split()
            for temp in data:
                if len(temp)>2:  # Excluyo terminos de 2 caracteres
                    valor = pyFormulas.formuTerminoBusqueda("VENTAS", temp)   # Busco en Ventas
                    if valor > 0:
                        # Busco idventa en Asserts Ventas
                        for dataVenta in ventaTemp:
                            if dataVenta[0] == valor:
                                print "Contacto VENTAS"
                                print f.Slots["mensaje"] + ' - (' + temp + ')', f.Slots["eid2"],dataVenta[1],valor
                                wr.writerow([f.Slots["mensaje"] + ' - (' + temp + ')', f.Slots["eid2"],dataVenta[1],valor])

                    valor = pyFormulas.formuTerminoBusqueda("COMPRAS", temp)   # Busco en Ventas
                    if valor > 0:
                        # Busco idventa en Asserts Ventas
                        for dataCompra in compraTemp:
                            if dataCompra[0] == valor:
                                print "Contacto COMPRAS"
                                print f.Slots["mensaje"]+ ' - (' + temp +')', f.Slots["eid2"],dataCompra[1],valor
                                wr.writerow([f.Slots["mensaje"]+ ' - (' + temp +')', f.Slots["eid2"],dataCompra[1],valor])

myfile.close()

