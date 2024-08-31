


n = int(input("Enter number: "))
if(n<1):
    print("{} is invalid".format(n))
res = "prime"
for i in range(2,n):
    if(n%i==0):
        res = "not Prime"
        break
    
print("{} is {}".format(n,res))