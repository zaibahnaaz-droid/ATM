l=[1,2,1,3,2,1]
n=int(input("enter ele to find:"))
c=0
for i in range (0,len(l),1):
    if(l[i]==n):
        c=c+1
print("the count of ele in list is:",c)
