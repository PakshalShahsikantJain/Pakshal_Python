class Node :
    def __init__(self) :
        self.Data = None
        self.Next = None
        self.Prev = None 
    
class DCLinkedList(Node) :
    def __init__(self) :
        self.Head = None 
        self.Tail = None
        Node.__init__(self)

    def InsertFirst(self,No) :
        newn = None
        newn = Node()

        Data = self.Data
        Next = self.Next 
        Prev = self.Prev

        newn.Data = No
        newn.Next = None
        newn.Prev = None

        if self.Head == None and self.Tail == None :
            self.Head = newn
            self.Tail = newn
        else :
            newn.Next = self.Head
            self.Head.Prev = newn
            self.Head = self.Head.Prev

        self.Tail.Next = self.Head
        self.Head.Prev = self.Tail

    def InsertLast(self,No) :
        newn = None
        newn = Node()
        
        Data = self.Data
        Next = self.Next
        Prev = self.Prev

        newn.Data = No
        newn.Next = None
        newn.Prev = None 

        if self.Head == None and self.Tail == None :
            self.Head = newn
            self.Tail = newn
        else :
            self.Tail.Next = newn
            newn.Prev = self.Tail.Next
            self.Tail = self.Tail.Next
        
        self.Tail.Next = self.Head
        self.Head.Prev = self.Tail

    def InsertAtPos(self,Pos,No) :
        newn = None
        newn = Node()

        Data = self.Data
        Next = self.Next

        newn.Data = No
        newn.Next = None 

        if self.Head == None and self.Tail == None :
            self.Head = newn
            self.Tail = newn
        elif self.Head.Next == None and self.Tail.Next == None :
            self.Head.Next = newn
            self.Tail.Next = newn
        else :
            temp = self.Head
            for i in range(Pos - 1) :
                temp = temp.Next
            
            newn.Next = temp.Next
            temp.Next = newn

    def DeleteFirst(self) :
        if self.Head == None and self.Tail == None :
            return
        else :
            self.Head = self.Head.Next
            self.Tail = self.Tail.Prev
            self.Head.Prev = None
            self.Tail.Next = None
        
        self.Tail.Next = self.Head
        self.Head.Prev = self.Tail 

    def DeleteLast(self) :
        if self.Head == None and self.Tail == None :
            return
        else :
            self.Head = self.Head.Next
            self.Head.Prev = None
            self.Tail = self.Tail.Prev
            self.Tail.Next = None

        self.Tail.Next = self.Head 

    def DeleteAtPos(self,Pos)   :
        temp = self.Head
        for i in range(Pos - 1) :
            temp = temp.Next
        temp2 = temp.Next 
        temp.Next = temp2.Next
        temp2 = None

        self.Tail.Next = self.Head
        self.Head.Prev = self.Tail

    def Display(self) :
        temp = self.Head
        temp2 = self.Tail

        while True :
            print("|",temp.Data,"|","<=>",end = " ")
            temp = temp.Next
            if temp == temp2.Next :
                print("|",temp2.Next.Data,"|",end = " ")
                break
def main() :
    print("Jay Ganesh.......")
    print("Enter How Many Elements You Want In Linked List")
    Value = int(input())

    obj = DCLinkedList()

    print("Enter Elements in Linked List")
    for i in range(Value) :
        print("Enter Elements Number",i + 1) 
        obj.InsertFirst(int(input()))
    
    print("Enter Elements in Linked List")
    for i in range(Value) :
        print("Enter Elements Number",i + 3) 
        obj.InsertLast(int(input()))
    obj.Display()

    print("\nEnter At Which Position You Want To Insert Element")
    no = int(input())

    print("Enter Element To Insert At Given Position")
    no2 = int(input())

    obj.InsertAtPos(no,no2)
    obj.Display()

    obj.DeleteFirst()
    print("\nAfter Deleting First Element Modified DCLinkedList is :")
    obj.Display()

    obj.DeleteLast()
    print("\nAfter Deleting Last Element Modified DCLinkedList is :")
    obj.Display()

    print("\nEnter One Position You Want To Delete")
    value = int(input())
    obj.DeleteAtPos(value)
    print("After Deleting Enteres Postion Element Modified DCLinkedList is :")
    obj.Display()
if __name__ == "__main__" :
    main()