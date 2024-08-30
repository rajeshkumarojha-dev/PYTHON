n = input("Enter Words: ")

count = 0
for i in n:

    if (i.isalpha()):
        print(i)
        count = count+1
else:
    print(len(n))
    print(count)

# for s in n:      
#     if (s.isupper()):
#         print(s)
# else:
#     print(len(s))