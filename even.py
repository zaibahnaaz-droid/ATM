z=[1,2,3,4,2,3,4,2,4]
n=len(z)
a=0
for i in z:
    if(i%2==0):
        a+=1
print("the count of even num:",a)
