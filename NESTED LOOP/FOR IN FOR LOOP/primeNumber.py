

n= int(input("Enter how many number u want: "))

lst = []
for i in range(1,n+1):
    num = int(input("Enter {} value: ".format(i)))
    lst.append(num)
else:
    print(lst)

    ps=[]
    res=True
    for n in lst:
        for i in range(1,n):
            if(n%i==0):
                res = False
                break
        # print(num,res)
        # if(res):
        ps.append(n)

    else:
        print(ps)

# else:
#     print(ps)


# #Program for Obtaining List of Primes from List of Numbers
# #InnerLoopEx6.py
# n=int(input("Enter How Many Numbers u want:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     lst=[] # creating an empty list
#     for i in range(1,n+1):
#         num=int(input("Enter {} Number:".format(i)))
#         lst.append(num)
#     else:
#         print("Given Numbers:{}".format(lst)) # [4, 5, 9, 7, 2]
#         print("-----------------------------------")
#         ps=[]
#         for num in lst: # outer loop--supply the value
#             if(num<=1):pass
#             else:
#                 res=True
#                 for i in range(2,num): # inner loop
#                     if(num%i==0):
#                         res=False
#                         break # makes the PVM to come-out-off inner Loop
#                 if(res):
#                     ps.append(num)
#         else:
#             print("Primes Numbers")
#             print(ps)



# for num in range(2,n+1):
#     res=True
#     for i in range(2,num): # inner loop
#         if(num%i==0):
#             res=False
#             break
#     if(res):
#         # print("Prime numbers are: ")
#         print(num,end=",")