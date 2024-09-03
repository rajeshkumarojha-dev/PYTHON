
n = int(input("Enter how many table want to print: "))

lst=[]
for i in range(1,n+1):
    # print(i)
    num = input("Enter value {}: ".format(i))
    for val in num:
        lst.append(val)
        # print("{}X{}={}".format(val,i))
    else:
        print(lst)
    for number in lst:
        # print(num)
        for i in range(1,11):
            print(i)
            print("{}X{}={}".format(number,i,number*i))

        #Program for Generating Mul Tables for n random numbers where n is +ve
#InnerLoopEx6.py
# n=int(input("Enter How Many Mul Tables u want:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     lst=[] # creating an empty list
#     for i in range(1,n+1):
#         num=int(input("Enter {} Number:".format(i)))
#         lst.append(num)
#     else:
#         print("Given Numbers:{}".format(lst)) # lst=[11, -12, 14, 19, 0]
#         print("-----------------------------------")
#         for num in lst: # Outer Loop
#             if(num<=0):
#                 print("{} Is Invalid Input:".format(num))
#             else:
#                 print("-"*50)
#                 print("Mul Table for :{}".format(num))
#                 print("-" * 50)
#                 for i in range(1,11): # Inner loop
#                     print("\t{} x {}={}".format(num,i,num*i))
#                 else:
#                     print("-" * 50)