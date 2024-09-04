#StudentMarksReportEx.py
#Accept Student Number and Validate
while(True):
    sno=input("Enter Student Number:")
    if(sno.isdigit()) and (int(sno) in range(100,201)):
        break
    print("\t{} is Invalid Student Number-try again".format(sno))
#accept name and Validation of name
while(True):
    name=input('Enter Ur Name:') # Guido V2an Rossum
    namewords=name.split() # ['Guido', 'V2an', 'Rossum']
    if(len(namewords)==0):
        print("\tDon't Enter Space---enter Ur Name")
    else:
        res=True
        for word in namewords:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            break
        else:
            print("\t{} is Invalid Name-try again".format(name))

#Accept C Lang Marks and Validate
while(True):
    cm=input("Enter Marks in C:")
    if (cm.isdigit()) and (int(cm) in range(0, 101)):
        break
    print("\t{} is Invalid Marks in C Lang-try again".format(cm))
#Accept C++ Lang Marks and Validate
while(True):
    cppm=input("Enter Marks in C++:")
    if (cppm.isdigit()) and (int(cppm)>=0 and int(cppm)<=100):
        break
    print("\t{} is Invalid Marks in C Lang-try again".format(cppm))
#Accept Python Lang Marks and Validate
while(True):
    pym=input("Enter Marks in Python:")
    if (pym.isdigit()) and (0<=int(pym)<=100):
        break
    print("\t{} is Invalid Marks in C Lang-try again".format(pym))
#Calculate totam Marks and Percentage of Marks
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
#Code for getting Fail student
if(int(cm)<40) or (int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
    if(totmarks in range(250,301)):
        grade="DISTINCTION"
    elif(200<=totmarks<=249):
        grade = "FIRST"
    elif(totmarks>=150 and totmarks<=199):
        grade="SECOND"
    elif(totmarks in range(120,150)):
        grade="THIRD"
print("="*50)
print("STUDENT MARKS REPORT")
print("="*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(name))
print("\tStudent Marks in C :{}".format(cm))
print("\tStudent Marks in C++ :{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pym))
print("-"*50)
print("\tStudent total Marks:{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percent))
print("\tStudent Grade:{}".format(grade))
print("="*50)