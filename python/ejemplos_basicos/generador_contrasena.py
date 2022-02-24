import random


def generar_password():
    mayusculas=['A','B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas=['a','b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    simbolos=['#','!','$','%','/','&', '*','(',')']
    numeros=['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []
    for i in range(15):
        caracter_random = random.choice(caracteres) # choice elige un caracter al azar
        password.append(caracter_random) # append va a agregar el parametro al final de la lista
    password = "".join(password) # "".join() va a concatenar cada elemento de la lista y lo convierte en un string
    return password  


def run():
    password=generar_password()
    print("Tu constraseña es: " + password)
    
    
if __name__ == '__main__':
    run()