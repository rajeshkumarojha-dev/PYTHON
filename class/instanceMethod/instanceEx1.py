class student:
    def readData(self,objinfo):
        print("*"*50)
        print(f'Enter {objinfo} student details')
        self.no = int(input("enter student Number: "))
        self.sname = input("enter student Name: ")
        self.marks = int(input("enter student marks: "))
        print("*"*50)

    def displayData(self,objinfo):
        print("*"*50)
        print(f"{objinfo} details")
        print(f"student Number: {self.no}")
        print(f"student Name: {self.sname}")
        print(f"student Marks: {self.marks}")
        print("*"*50)


c = student()
c1 = student()
c.readData("first")
c.displayData("first")

c1.readData("second")
c1.displayData("second")