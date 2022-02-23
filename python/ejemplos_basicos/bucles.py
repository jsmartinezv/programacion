def run():
    contador = 0
    base = int(input("ingrese la base a calcular: "))
    LIMITE = 1000 # las constantes se nombran con mayusculas
    potencia = base**contador
    while potencia < LIMITE:
        print(str(base) + " elevado por " + str(contador) + " es igual a: " + str(potencia))
        contador = contador + 1
        potencia = base**contador
    
if __name__=="__main__":
    run()