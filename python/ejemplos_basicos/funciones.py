def conversacion(mensaje):
    print('Hola,como estas')
    print(mensaje)
    print('Adios')
opcion = int(input("Hola ingrese una opcion: "))
if opcion==1:
    conversacion("ingresó la opción numero 1")
elif opcion==2:
    conversacion("ingresó la opción numero 2")
elif opcion==3:
    conversacion("ingresó la opción numero 3")
else:
    print("ingresó una opcion no contemplada")
