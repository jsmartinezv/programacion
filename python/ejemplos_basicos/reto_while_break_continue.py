# se ingresa un numero y desde ese numero hasta 99 se van a imprimir todos los numeros que no sean
# enteramente divisibles entre 2 y 3
def run():
    numero = int(input("ingrese un numero: "))
    while numero < 100:
        numero = numero + 1
        if numero % 2 == 0 or numero % 3 == 0:
            continue
        print(numero)         
    print("se acabo")

if __name__ == '__main__':
    run()