class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_node=node(data)

        if self.head is not None:
            self.head.prev=new_node
            new_node.next-self.head
        self.head=new_node
        print("Inserted at begining")

    def insert_end(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        new_node.prev=temp
        print("Inserted end")



    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        temp=self.head
        self.head=temp.next


        if   self.head is not None:
            self.head.prev=None
        print("deleed from begining")


    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.next is None:
            self.head=None
            print("deleted last node")
            return

        while temp.next is not None:
            temp=temp.next

        temp.prev.next=None
        print("deleted from end")


    def display_forward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        print("forward traversal")
        while temp is not None:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")


    def display_backward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        print("backward traversal")
        while temp is not None:
            print(temp.data,end="<->")
            temp=temp.prev
        print("None")

Dll=DoublyLinkedList()

while True:

    print("----Doubly LInked List Menu-----")
    print("1. Insert at Begining")
    print("2. Insert at end")
    print("3. Delete from Begining")
    print("4. Delete from end ")
    print("5. Display forward")
    print("6. Display backward")
    print("7. Exit")

    choice = int(input("Enter your choice:"))

    if choice==1:
      val=int(input("Enter value:"))
      Dll.insert_begin(val)
    elif choice==2:
      val=int(input("Enter value:"))
      Dll.insert_end(val)
    elif choice==3:
      Dll.delete_begin()
    elif choice==4:
      Dll.delete_end()
    elif choice==5:
      Dll.display_forward()
    elif choice==6:
      Dll.display_backward()
    elif choice==7:
        print("program ended")
        break
    else:
        print("invalid option")
    
          
    
  
      


         
                  
        
        
