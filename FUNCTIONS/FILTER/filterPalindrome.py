# FilterFunEx5.py
print("Enter List of Words separated by Comma:")

words=[word for word in input().split(",")] # words=[LIRIL,PYTHON,MADAM,JAVA,MOM]

palwords=list(filter(lambda word:word==word[::-1],words))

print("Given Words={}".format(words))
print("List of palindrome words={}".format(palwords))




