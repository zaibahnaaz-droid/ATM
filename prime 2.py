n=[12,3,4,5,6,7,1]
for z in n:
    c=0
    if(z==1):
       print("not prime",z)
    else:
           for i in range(1,z+1,1):
               if z%i==0:
                   c+=1
           if c==2:
              print("prime:",z)
