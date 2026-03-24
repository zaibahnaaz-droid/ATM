q=list(map(int,input("enter:").split( )))
x=int(input("enter num"))
for i in range(0,len(q),1):
        if (q[i]==x):
            print("the ele",x,"is  found in",i,"index")
            break
else:
         print("ele not found")
