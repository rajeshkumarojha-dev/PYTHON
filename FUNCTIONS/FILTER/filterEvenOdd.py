
print("Enter numbers")

numbers = [ int(val) for val in input().split()]

EvenNumber = list(filter(lambda values: values%2 == 0,numbers))
OddNumber = list(filter(lambda values: values%2 != 0,numbers))

print("-"*40)
print("Given numbers of list")
print(numbers)
print("-"*40)

print("Enen numbers of list")
print("-"*40)
print(EvenNumber)
print("-"*40)
print("Odd numbers of list")
print("-"*40)
print(OddNumber)
print("-"*40)
