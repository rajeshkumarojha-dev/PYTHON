

n = int(input("Enter number want to print natural numbers: "))

if(n<0):
    print("{}is invalid number".format(n))
else:
    sum=0
    
    for i in range(1,n+1):
        sum += i
        print(i)
    else:
        print('-'*20)
        print(sum)
