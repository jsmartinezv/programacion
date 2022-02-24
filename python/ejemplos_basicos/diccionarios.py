#Programa que ejemplifica los diccionarios, el recorrido y la extraccion de sus claves y valores
def run():
    poblacion_paises = {
        'Argentina' : 49000000,
        'Brazil' : 210000000,
        'Colombia' : 50000000
    }
    #print(poblacion_paises['Argentina']) #devuelve el valor almacenado y relacionado con la key 'Argentina'
    for pais in poblacion_paises.keys():
        print(pais)
    for poblacion in poblacion_paises.values():
        print(str(poblacion))
    for pais, poblacion in poblacion_paises.items():
        print(pais + " posee una población de " + str(poblacion) + " Habitantes")


if __name__ =='__main__':
    run()