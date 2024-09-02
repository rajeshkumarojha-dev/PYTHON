
# REMOVING ONE LETTER IN WORDS

n=input("Enter Words: ")

for i in n:
    if i == 't':
        continue
    print(i,end=" ")
else:
    print()
    print("For loop execution ended...")

# REMOVING ONE LETTER IN WORDS USE PASS KEYWORDS

s = input("Enter Words using pass: ")

for i in s:
    if i=="t":pass
    else:
        print(i,end=" ")
else:
    print()
    print("For loop execution ended...")

# REMOVING ONE LETTER IN WORDS USING WHILE LOOP

r = input("Enter words Using while loop: ")

i=0
while(i<len(s)):
    if(s[i] == 't'):
        i=i+1

    else:  
        print(s[i], end=" ")
        i+=1
else:
    print()
    print("While loop execution ended...")


# REMOVING TWO LETTER IN WORDS USING For LOOP

x = input("Enter words for remove two letter: ")

for i in x:
    if i == "t" or i=="o":
        continue
    else:
        print(i,end=" ")
else:
    print()
    print("For loop ended")
