class Parent:
    def show(self):
        print("this is parent class")
class child(Parent):
    def res(self):
        print("this is child class")
p=Parent()
p.show()
c=child()
c.res()
c.show()
