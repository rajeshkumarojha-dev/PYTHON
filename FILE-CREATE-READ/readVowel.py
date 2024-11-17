# def read_vowel(files):
#     vowels = {'a','e','i','o','u'}
#     try:
#         with open(files,"r") as file:
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     if(word[0] in vowels):
#                         print(word)
#     except FileNotFoundError:
#         print("Wrong Input")

# files = "Hello"
# read_vowel(files)

def read_vowel_words(file_path):
    # Define vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    try:
        # Open and read the file
        with open(file_path, 'w') as file:
            for line in file:
                # Split each line into words
                words = line.split()
                # Check and print words that start with a vowel
                for word in words:
                    if word[0].lower() in vowels:
                        print(word)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify your file path here
file_path = "sample.txt"  # Replace with the path to your file
read_vowel_words(file_path)