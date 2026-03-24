     
stack=[]
def push():
    z=int(input("Enter ele to push:"))
    stack.append(z)
    print("work done",z)
def pop():
    if len(stack)==0:
        print("khali")
    else:
        re_ele=stack.pop()
        print("popping done",re_ele)
def peek():
    if len(stack)==0:
        print("khali")
    else:
        print("element is",stack[-1])
def display1():
    if len(stack)==0:
        print("khali")
    else:
        print("elements are(from top to bottom):")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
def display2():
    if len(stack)==0:
        print("khali")
    else:
        print("elements are(from bottom to top):")
        for i in range(len(stack)-1,-1,1):
            print(stack[i])
def length():
    print("num of ele in stack:",len(stack))
while True:
    print("\n----stack menu=----")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display1")
    print("4.display2")
    print("5.length")
    print("6.exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display1()
    elif choice==5:
        display2()
    elif choice==6:
        print("khallas")
        break
    else:
        print("ni hai")
          



