class Test:
    def __init__(self,x,y):
        self.no=x
        self.name=y
        print(self.no)
        print(self.name)
class Test2:
    def __init__(self,k=20,name="Travis"):
        self.a=k
        self.b=name


eco = Test(20,"Liza")
# print("content of test",eco.__dict__)

c = Test2("30","Rajesh")
# print("content of Test2",c.__dict__)