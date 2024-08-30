
n = input("enter words: ")

Uppercount = 0
lowerCount = 0
Symbolcount = 0
Numbercount = 0
for i in n:
    if(i.isupper()):
        print(i)
        Uppercount+=1
    if(i.islower()):
        print(i)
        lowerCount+=1
    if not(i.isalnum()):
        print(i)
        Symbolcount+=1
    if(i.isdigit()):
        print(i)
        Numbercount+=1
    # print(i) 
else:
    print("{} TotalLetterInWords".format(len(n)))
    print("{} UpperCount".format(Uppercount))
    print("{} LowerCount".format(lowerCount))
    print("{} Symbols".format(Symbolcount))
    print("{} Numbers".format(Numbercount))