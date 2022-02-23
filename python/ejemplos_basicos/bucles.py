def potencia(base, exponente):
    numero = base**exponente
    return numero

def run():
    base = int(input("ingrese la base a calcular: "))
    exponente = 0
    numero=potencia(base, exponente)
    if numero < 1000:
        print(str(base) + " elevado por " + str(exponente) + " = " + str(numero))
        exponente = exponente + 1
    else:
        print("numero es mayor a 1000")

if __name__=="__main__":
    run()