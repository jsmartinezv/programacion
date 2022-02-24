import random # un modulo de python

def run():
    numero_aleatorio=random.randint(1,100) # genera un numero entero aleatorio entre 1 y 100
    numero_elegido=int(input("Elija un numero entre 1 y 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Es un numero mas grande ")
        else:
            print("Es un numero mas pequeño ")
        numero_elegido=int(input("Ingresa otro numero: "))
    print("ganaste!!")


if __name__ == '__main__':
    run()