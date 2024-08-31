
n = int(input("Enter Number: "))

if(n<1):
    print("{} is invalid".format(n))
i=2
res = 'prime'
while(i<n):
    if(n%i == 0):
        res = "not prime"
    i+=1
print("{} is {}".format(n,res))