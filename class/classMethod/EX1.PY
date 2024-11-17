class employee:
    @classmethod
    def readData(cls,objinfo):
        print('*'*50)
        print(f'Enter {objinfo} details')
        print('*'*50)
        cls.course=input("Enter course name: ")
        cls.fees = int(input("Enter course fee: "))
    @classmethod
    def dispData(cls,objinfo):
        print('*'*50)
        print(f'Enter {objinfo} details')
        print('*'*50)
        print(f"course name: {cls.course}")
        print(f"course Fee: {cls.fees}")

t1 = employee()
t2 = employee()
t1.readData("first")
t2.readData("second")
t1.dispData("first")
t2.dispData("second")