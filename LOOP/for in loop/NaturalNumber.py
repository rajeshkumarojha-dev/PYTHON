
n = int(input("Enter Factorial number: "))
fact= 1
for i in range(1,n+1):
    fact = fact*i
else:
    print("factorial{} = {}".format(n,fact))