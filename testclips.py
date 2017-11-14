import clips
import pyFormulas


clips.Clear()
clips.Reset()

clips.DebugConfig.ActivationsWatched = True


#Area de Funciones Py

def py_square(x,y):
    return  x*y

def py_string(x,y):
    return  str(x) +' - '+ str(y)

#Fin Area de Funciones Py

#Registracion Funct
clips.RegisterPythonFunction(py_square)

f0 = clips.Assert("(Juan H C)")
f0 = clips.Assert("(Luis H C)")
f0 = clips.Assert("(Maria M C)")
f0 = clips.Assert("(Lucia M S)")
f0 = clips.Assert("(German H S)")

#Lista los Hechos en formato clips
fl = clips.FactList()
print fl

#Impresion amigable de Facts
clips.PrintFacts()

# llama Funcion Pyton e imprime
print clips.Eval("(python-call py_square 4 3)")

clips.RegisterPythonFunction(py_string)
# llama Funcion Pyton e imprime
print clips.Eval("(python-call py_string ARGENTINA CHILE)")


clips.RegisterPythonFunction(pyFormulas.formuUbicacionEmpresaPais)
# llama Funcion Pyton e imprime
print clips.Eval("(python-call formuUbicacionEmpresaPais VENEZUELA ARGENTINA)")