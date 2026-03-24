class p1:
    def p1(self):
        print("xyz")
class p2:
    def p2(self):
        print("abc")
class son(p1,p2):
    def r(self):
        print("zna")
h=son()
h.r()
h.p1()
h.p2()
