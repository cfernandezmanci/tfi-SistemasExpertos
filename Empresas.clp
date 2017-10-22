; Datos de Empresas

(deftemplate Empresas
(field Nombre)
(field Tipo)
(field Pais)
(field Ciudad)
(field ComercioExterior)
(field Puntaje)
)

(deffacts VariasEmpresasHechos
(Empresas
	(Nombre "Empresa 1")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "Buenos Aires")
	(ComercioExterior "Nada")
	(Puntaje 40))
(Empresas
	(Nombre "Empresa 2")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "Buenos Aires")
	(ComercioExterior "Importa")
	(Puntaje 60))
(Empresas
	(Nombre "Empresa 3")
	(Tipo "MicroPymes")
	(Pais Argentina)
	(Ciudad "Cordoba")
	(ComercioExterior "Importa-Exporta")
	(Puntaje 74))
(Empresas
	(Nombre "Empresa 4")
	(Tipo "Profesional")
	(Pais Argentina)
	(Ciudad "Concordia")
	(ComercioExterior "Exporta")
	(Puntaje 90))
(Empresas
	(Nombre "Empresa 5")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "Concordia")
	(ComercioExterior "Exporta")
	(Puntaje 93))
(Empresas
	(Nombre "Empresa 6")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "Concordia")
	(ComercioExterior "Exporta")
	(Puntaje 60))
(Empresas
	(Nombre "Empresa 7")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "Buenos Aires")
	(ComercioExterior "Exporta")
	(Puntaje 80))			

(Empresas
	(Nombre "Empresa 8")
	(Tipo "Pymes")
	(Pais Argentina)
	(Ciudad "La Plata")
	(ComercioExterior "Exporta")
	(Puntaje 30))

(Empresas
	(Nombre "Empresa 9")
	(Tipo "Pymes")
	(Pais Mexico)
	(Ciudad "Guadalajara")
	(ComercioExterior "Importa-Exporta")
	(Puntaje 30))	

(Empresas
	(Nombre "Empresa 10")
	(Tipo "MicroPymes")
	(Pais Peru)
	(Ciudad "Lima")
	(ComercioExterior "Nada")
	(Puntaje 30))

(Empresas
	(Nombre "Empresa 11")
	(Tipo "Pymes")
	(Pais Peru)
	(Ciudad "Trujillo")
	(ComercioExterior "Importa-Exporta")
	(Puntaje 30))		
)

(defrule ImprimeExporta 
	(Empresas (ComercioExterior ?ComercioExterior & "Exporta"|"Importa-Exporta") 
	(Nombre ?Nombre)	   	
	)
	=> 
	(printout 
	t crlf "****************************"
	t crlf ?Nombre " - " ?ComercioExterior " sus productos."
	t crlf "****************************")
)

(defrule ImprimePymes 
	(Empresas (Tipo ?Tipo & "Pymes") 
	(Nombre ?Nombre)
	(ComercioExterior ?ComercioExterior)	   	
	)
	=> 
	(printout 
	t crlf "****************************"
	t crlf ?Nombre " Es una Pyme. "
	t crlf "Comercio Exterior: " ?ComercioExterior)
	t crlf "****************************"
)

(defrule ImprimeMayorPtos60 
	(Empresas 
	 	(Puntaje ?Puntaje & :(> ?Puntaje 60)) 
		(Nombre ?Nombre)	   	
	)
	=> 
	(printout 
	t crlf "****************************"
	t crlf ?Nombre " ha completado sus datos. "
	t crlf "Puntaje : " ?Puntaje)
	t crlf "****************************"
)


