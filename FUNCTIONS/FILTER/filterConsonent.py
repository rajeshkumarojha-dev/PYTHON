print("Enter word separeted by comma")

words = [ word for word in input().split(',')]

vowelWord = list(filter(lambda word: any(char in 'bcdfghjklomnpqrstvwxyz' for char in word),words))

print("normal words",words)

print("vowel words",vowelWord)