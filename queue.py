queue=[]
def insert():
    z=int(input("Enter ele to push:"))
    queue.append(z)
    print("work done",z)
def delete():
    if len(queue)==0:
        print("khali")
    else:
        removed_ele=queue.pop(0)
        print("popping done",removed_ele)
def front():
    if len(queue)==0:
        print("khali")
    else:
        print("element is",queue[0])
def display():
    if len(queue)==0:
        print("khali")
    else:
        print("elements are:")
        for i in queue
            print(i)
def search():
    if len(queue)==0:
        print("khali")
    else:
        h=int(input("enter num"))
        if h in queue:
            print("found",h)
        else:
            print("not found")
def length():
    print("num of ele in queue:",len(queue))
while True:
    print("\n----queue menu=----")
    print("1.insert")
    print("2.delete")
    print("3.front")
    print("4.display")
    print("5.search")
    print("6.length")
    print("7.exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        insert()
    elif choice==2:
        delete()
    elif choice==3:
        front()
    elif choice==4:
        display()
    elif choice==5:
        search()
    elif choice==6:
        length()
    elif choice==7
        print("khallas")
        break
    else:
        print("ni hai")
          




    
    
