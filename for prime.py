n=int(input("Enter num:"))
for i in range(1,n+1,1):
    if(n%i==0):
        print(i,end="  ")
