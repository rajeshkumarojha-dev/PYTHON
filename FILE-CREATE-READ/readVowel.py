def read_vowel(files):
    vowels = {'a','e','i','o','u'}
    try:
        with open(files,"r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if(word[0] in vowels):
                        print(word)
    except FileNotFoundError:
        print("Wrong Input")

files = "Hello"
read_vowel(files)