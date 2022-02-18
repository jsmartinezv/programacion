pesos=input("¿Cuantos Pesos Colombianos Tienes?: ")
pesos=float(pesos)
valor_dolar=3991
dolares = str(round(pesos/valor_dolar,2))
print("tienes $" + dolares + " Dolares")