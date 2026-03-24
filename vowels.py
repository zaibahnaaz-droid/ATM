g="zaiba@5654"
s=['a','e','i','o','u']
c=0
oval=0
const=0
char=0
digit=0
splch=0

for h in g:
    if (h in s):
        c+=1
        print("vowels",h)
        oval+=1
    else:
        print("consonents",h)
        const+=1

    if(h.isalpha()):
        print("alphabet",h)
        char+=1
    elif(h.isdigit()):
            print("integer",h)
            digit+=1
    else:
        print("spl char",h)
        splch+=1
print("oval",oval ,"consonent",const ,"alpha",char ,"inte",digit ,"naaz",splch)
