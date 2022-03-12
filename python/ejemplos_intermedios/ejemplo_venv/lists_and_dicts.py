def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"first_name": "Juan", "last_name": "Martinez" }
    # Lista de diccionarios
    super_list = [ 
        {"first_name": "Juan", "last_name": "Martinez" },
        {"first_name": "Sebastian", "last_name": "Valbuena" },
        {"first_name": "Joselito", "last_name": "Porras" }
    ]
    #Diccionario de listas
    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1.1, 4.5 ,6.3]
    }
    for key, value in super_dict.items():
        print(key, "-", value) # la coma funciona como si se le suma un espacio (+ " ") 

    for item in super_list:
        print( item["first_name"] , "-",  item["last_name"] , " .. ")

# Entry point 
if __name__ == "__main__": 
    run()