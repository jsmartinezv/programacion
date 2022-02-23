def run():
    nombre = input("Escribe tu nombre: ")
    for letra in nombre:
        #print(letra)
        print(letra.upper())#imprime los caracteres en mayuscula

if __name__=="__main__":
    run()