words = input("Enter any Words: ")
result = 'oval' if any(char in 'aeiou' for char in words) else 'not oval'

print("{} word is : {}".format(words,result))