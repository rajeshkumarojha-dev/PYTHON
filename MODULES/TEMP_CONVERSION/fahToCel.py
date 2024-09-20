
def fahToCel():
    print("FAH TO CEL")
    fah = int(input("Enter temp in term of Fah: "))
    c = (fah-32)*(5/9)
    print('-'*40)
    print("Equi. temp in cel: %0.1f" %(c))
# fahToCel()