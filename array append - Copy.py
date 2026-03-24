z=[1,2,3,4]
r=int(input("enter row:"))
c=int(input("enter col:"))
l=[]
for i in range(0,r,1):
     m=[]
     for i in range(0,c,1):
         ele=int(input("ele:"))
         m.append(ele)
     l.append(m)
for i in range(0,r,1):
    print(l[i])
