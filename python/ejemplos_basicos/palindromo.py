def palindromo(palabra):
    palabra=palabra.replace(" ","")
    palabra=palabra.lower()
    palabra_invertida=palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra=input("Escriba una palabra: ")
    es_palabra=palindromo(palabra)
    if es_palabra==True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ =="__main__":
    run()