from abc import ABC,abstractmethod
class  calci(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def multi(self):
        pass
    @abstractmethod
    def div(self):
        pass
    @abstractmethod
    def mod(self):
        pass
    @abstractmethod
    def expo(self):
        pass
class cal(calci):
    def __init__(self):
        self.a=10
        self.b=15
    def add(self):
        print("sum is:",self.a+self.b)
    def sub(self):
        print("diff is:",self.a-self.b)
    def multi(self):
        print("prod is:",self.a*self.b)
    def div(self):
        print("rem is",self.a/self.b)
    def mod(self):
        print("quo is:",self.a%self.b)
    def expo(self):
        print("power is:",self.a**self.b)
z=cal()
while True:
    print("=====cal menu=====")
    print("1.add")
    print("2.sub")
    print("3.multi")
    print("4.div")
    print("mod")
    print("1.expo")
    choice=int(input("enter choice:"))
    if choice==1:
        z.add()
    elif choice==2:
        z.sub()
    elif choice==3:
        z.multi()
    elif choice==4:
        z.div()
    elif choice==5:
        z.mod()
    elif choice==6:
        z.expo()
    elif choice==7:
        print("ntg")
        break
    else:
        print("invalid choice")
        
    
    
    
    
