class factorial:
    def fact(self):
        while(True):
            try:
                self.n=int(input("Enter number: "))
            except ValueError:
                print("Doesn't take symbol, number and alphabet")
            else:
                if(self.n<0):
                    print("Invalid Input")
                else:
                    f=1
                    for i in range(1,self.n+1):
                        f= f*i
                    else:
                        print(f"factorial {self.n} value is: {f}")

f=factorial()
f.fact()
                
