import clips
import pyClasses
import pyFormulas
import os

'''DEFINICIONES'''

#NPC MyHome  Local
DIRECTORIO = "/home/christian/tfiClips/"

## Text menu in Python

def print_menu():  ## Your menu design here
    print 30 * "-", "MENU", 30 * "-"
    print "1. Ver Empresas"
    print "2. Ver Ventas"
    print "3. Ver Compras"
    print "4. Ver Enlaces"
    print "5. Exit"
    print 67 * "-"


loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice == 1:
        print "1. Empresas Cargadas"
        ## Listado de empresas
        empresalista = pyClasses.Empresas(DIRECTORIO + "empresas_1.csv")
        empresalista.listar()

        raw_input("Presione una tecla para volver al Menu ...")
        os.system('clear')
    elif choice == 2:
        ## Listado de Ventas por Empresa
        ventalista = pyClasses.Ventas(DIRECTORIO + "productos_1.csv")
        ventalista.listar()

        raw_input("Presione una tecla para volver al Menu ...")
        os.system('clear')

    elif choice == 3:
        print "Menu 3 has been selected"
        ## You can add your code or functions here
    elif choice == 4:
        print "Menu 4 has been selected"
        ## You can add your code or functions here
    elif choice == 5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
