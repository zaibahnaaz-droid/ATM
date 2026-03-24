class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_begin (self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        print("Node inserted at begining")

    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            print("node inserted as first node")
            return
        temp=self.head

        while temp.next:
            temp=temp.next
        temp.next=new_node
        print("node inserted at end")

    def delete(self,key):
        temp=self.head

        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            print("node deleted")
            return
        prev=None

        while temp and temp.data !=key:
            prev=temp
            temp=temp.next

        if temp is None:
            print("value not found")
            return
        prev.next=temp.next
        temp=None
        print("node deleted")


    def  search(self,key):
        temp=self.head

        while temp:
            if temp.data==key:
                print("element found")
                return
            temp=temp.next
        print("element not found")


    def display(self):
        temp=self.head
        if temp is None:
            print("list is empty")
            return

        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("none")

L1=linkedlist()

while True:
    print("\n--------Linked List Menu------")
    print("1. insert begining")
    print("2. Insert at end")
    print("3. Delete Node")
    print("4. Search Element")
    print("5. Display List")
    print("6. Exit")
    choice=int(input("Enter choice:"))


    if choice==1:
        value=int(input("Enter value:"))
        L1.insert_begin(value)
    elif choice==2:
        value=int(input("Enter value:"))
        L1.insert_end(value)
    elif choice==3:
        value=int(input("Enter value:"))
        L1.delete(value)
    elif choice==4:
        value=int(input("Enter value:"))
        L1.search(value)
    elif choice==5:
        L1.display()
    elif choice==6:
         print("program ended")
    else:
        print("invalid option")
        
        
        
        
