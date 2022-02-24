# El teorema de wilson indica que sea un numero entero p>0, si el factorial de (p-1) es divisible 
# en (p-1) entonces p es un numero primo
def factorial(numero):
    producto=1
    for i in range(1, numero+1):
        producto *= i
    return producto


def es_primo(numero):
    if factorial(numero - 1) % (numero - 1) == 0:
        return True
    else:
        return False


def run():
    numero=int(input("ingrese un numero: "))
    print("el factorial de " + str(numero) + " es " + str(factorial(numero)))
    if es_primo(numero):
        print(str(numero) + "es primo")
    else:
        print(str(numero) + "no es primo")


if __name__ =='__main__':
    run()