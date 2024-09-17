

print("Enter salery amount")

salery = [float(sal) for sal in input().split()]

IncreaseSal = list(map(lambda sal : sal*0.5,salery))
TotalIncrease = list(map(lambda sal: sal*0.5+sal,salery))

print("-"*40)
print("Given salery in List")
print("-"*40)
print(salery)

print("-"*40)
print("Increase salery in 50% hike")
print("-"*40)
print(IncreaseSal)
print("-"*40)
print("TotalIncrease salery in List")
print("-"*40)
print(TotalIncrease)

print("#"*40)
print("OR")
print("#"*40)

for salery,IncreaseSal,TotalIncrease in zip(salery,IncreaseSal,TotalIncrease):
    print("-"*80)
    print("\tsalery""\t\tIncreaseSal""\tTotalsalery")
    print("-"*80)

    print("\t{}\t--->\t{}\t--->\t{}".format(salery,IncreaseSal,TotalIncrease))