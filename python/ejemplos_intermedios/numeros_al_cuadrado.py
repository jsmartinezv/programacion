
def run():
    max = int(input("Ingrese el numero maximo al que le va a hallar su cuadrado: "))
    list_power_nums=[]
    for i in range(0, max):
        print("El cuadrado de" , str(i), "es", str(i**2))
        list_power_nums.append(i**2)
    print("la lista" + str(list_power_nums))
    
if __name__ == "__main__":
    run()   