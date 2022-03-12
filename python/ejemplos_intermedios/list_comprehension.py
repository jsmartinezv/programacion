def run():
    max = int(input("Ingrese el numero maximo al que le va a hallar su cuadrado: "))
    # list_power_nums=[]
    # for i in range(0, max):
    #     if (i**2 % 3) != 0:
    #         list_power_nums.append(i**2)    
    list_power_nums=[i**2 for i in range(0,max) if i**2 % 3 != 0]        
    print("la lista" + str(list_power_nums))
    # nums_2 una lista de todos los multiplos de 4 que a su vez sean multiplos de 6 y 9 y sean menores a 10 mil
    # nums_2=[i for i in range(0,10000) if i%4 == 0 and i%6==0 and i%9==0 ]
    # print(str(nums_2))

if __name__ == "__main__":
    run()   