menu = """
Bienvenidos al conversor de monedas

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción:
"""
opcion = input(menu)
if opcion == '1':
    pesos=input("¿Cuantos Pesos Colombianos Tienes?: ")
    pesos=float(pesos)
    valor_dolar=3991
    dolares = str(round(pesos/valor_dolar,2))
    print("tienes $" + dolares + " Dolares")
elif opcion == '2':
    pesos=input("¿Cuantos Pesos Argentinos Tienes?: ")
    pesos=float(pesos)
    valor_dolar= 64
    dolares = str(round(pesos/valor_dolar,2))
    print("tienes $" + dolares + " Dolares")
elif opcion == '3':
    pesos=input("¿Cuantos Pesos Mexicanos Tienes?: ")
    pesos=float(pesos)
    valor_dolar=25
    dolares = str(round(pesos/valor_dolar,2))
    print("tienes $" + dolares + " Dolares")
else:
    print("ingresa una opción correcta ")


### Ejemplo 1: solo cambio de pesos a dolares - basico
#pesos=input("¿Cuantos Pesos Colombianos Tienes?: ")
#pesos=float(pesos)
#valor_dolar=3991
#dolares = str(round(pesos/valor_dolar,2))
#print("tienes $" + dolares + " Dolares")