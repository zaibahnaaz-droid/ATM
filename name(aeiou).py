H=["zaiba","sharon","hasan","enosh"]
for name in H:
    c=0
    for char in name:
        if(char=='a' or char=='e' or char=='i' or char=='o' or  char=='u'):
            c+=1
    print(name,"=",c)
