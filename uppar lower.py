t=input("enter=")
print("the given string is",t)
for h in t:
    if(h.isupper()):
       print(h.lower(),end=" ")
    else:
        print(h.upper(),end=" ")


