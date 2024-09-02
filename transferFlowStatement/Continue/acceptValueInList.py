n = int(input("number of line want to print: "))

lst =[]
for i in range(1,n+1):
    val = int(input("Enter {} value: ".format(i)))
    # print("Enter {} value: ".format(i))
    lst.append(val)
print(lst)

sum=0
for g in lst:
    sum+=g
    div = sum/len(lst)
print(sum)
print(div)