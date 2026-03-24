class Gf:
    def p(self):
        print("xyz")
class dad(Gf):
    def q(self):
        print("abc")
class son(dad):
    def r(self):
        print("zna")
h=son()
h.p()
h.q()
h.r()
