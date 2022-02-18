def suma(a,b):
    print("se suman dos numeros: " + str(a) + " y " + str(b))
    resultado=a+b
    return resultado # Está función devuelve un resultado, es decir tiene un retorno
sumatoria = suma(int(input("ingrese un numero A: ")),int(input("ingrese un numero B: ")))
print(sumatoria)