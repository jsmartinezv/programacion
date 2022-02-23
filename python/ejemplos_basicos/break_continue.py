def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue         # si es un impar vuelve al for y suma el siguiente
    #     print(contador)     # si es par imprime el numero almacenado en contador
    
    # for i in range(100):
    #     print(i)
    #     if i == 56:
    #         break

    texto = input("ingrese un texto: ")
    for letra in texto:
        if letra =='o':
            break
        print (letra)
    print(texto)


if __name__ =='__main__':
    run()