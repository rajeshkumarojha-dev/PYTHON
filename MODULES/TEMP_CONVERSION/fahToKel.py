def fahToKel():
    print("FAH TO KEL")
    fah = int(input("Enter temp in term of Fah: "))
    k = (fah-32)*(5/9)+273.15
    print('-'*40)
    print("Equi. temp in Kel: %0.1f" %(k))
# fahToKel()