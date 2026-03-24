class calci:
    def add(self):
        a=5
        c=7
        print(a+c)
class cal(calci):
    def sub(self):
        a=100
        c=78
        print(a-c)
class cal1(calci):
    def prod(self):
        a=6
        c=6
        print(a*c)
class cal2(calci):
    def expo(self):
        a=10
        c=8
        print(a**c)
a=calci()
a.add()
b=cal()
b.sub()
h=cal1()
h.prod()
z=cal2()
z.expo()
