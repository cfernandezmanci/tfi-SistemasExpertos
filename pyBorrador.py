import pyFormulas


valor = pyFormulas.formuUbicacionEmpresaPais("ARGENTINA","CHILE")
print valor

valor = pyFormulas.formuUbicacionEmpresaPais("ARGENTINA","ESPANA")
print valor

valor = pyFormulas.formuUbicacionEmpresaPais("VENEZUELA","ARGENTINA")
print valor



valor =pyFormulas.formuPuntajeEmpresa("273")
print valor


valor =pyFormulas.formuPuntajeEmpresa("11273")
print valor


valor =pyFormulas.formuValorEnlace("181082")
print valor

print "---------------BUSQUEDA ------------------"

valor = pyFormulas.formuTerminoBusqueda("COMENTARIOS","web")
print valor

valor = pyFormulas.formuTerminoBusqueda("COMENTARIOS","cord")
print valor


valor = pyFormulas.formuTerminoBusqueda("EMPRESAS","Tambo")
print valor

valor = pyFormulas.formuTerminoBusqueda("EMPRESAS","madera")
print valor

valor = pyFormulas.formuTerminoBusqueda("VENTAS","madera")
print valor

valor = pyFormulas.formuTerminoBusqueda("VENTAS","cabernet")
print valor


valor = pyFormulas.formuTerminoBusqueda("COMPRAS","papel")
print valor

valor = pyFormulas.formuTerminoBusqueda("COMPRAS","goma")
print valor

