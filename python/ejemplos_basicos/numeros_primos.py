# indica si un numero es primo
def es_primo(numero):
    contador=0
    for i in range(1, numero + 1):
        if i==1 or i==numero:
            continue
        if numero % i == 0:
            contador +=1 ## es igual a tener contador = contador + 1
    if contador == 0:
        return True
    else:
        return False
    #if numero % 1 and numero % numero == 0:
    #    return True
    
def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero): # si no se le pone un condicional es_primo(numero)==True pyehon va interpretarlo automaticamente
        print("es primo")
    else:
        print("no es primo")
    

if __name__=='__main__':
    run()