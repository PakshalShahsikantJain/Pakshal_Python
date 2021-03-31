class Node :
    def __init__(self) :
        self.Data = None
        self.Next = None
        self.Prev = None

class DLinkedList(Node) :
    def __init__(self) :
        self.Head = None
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

        if self.Head == None :
            self.Head = newn
        else :
            newn.Next = self.Head
            self.Head.Prev = newn.Next
            self.Head = newn

    def InsertLast(self,No) :
        newn = None
        newn = Node()
        temp = self.Head
        Data = self.Data
        Next = self.Next
        Prev = self.Prev

        newn.Data = No
        newn.Next = None
        newn.Prev = None

        if self.Head == None :
            self.Head = newn
        else :
            while temp.Next != None :
                temp = temp.Next
            temp.Next = newn
            newn.Prev = temp.Next

    def DeleteFirst(self) :
        print("Inside DeleteFirst")
        if self.Head == None :
            return 
        elif self.Head.Next == None :
            self.Head = None
            return 

        self.Head = self.Head.Next
        self.Head.Prev = None
    
    def InsertAtPos(self,No,Pos) :
        newn = None
        newn = Node()
        temp = self.Head

        Data = self.Data 
        Next = self.Next
        Prev = self.Prev

        newn.Data = No
        newn.Next = None
        newn.Prev = None

        if self.Head == None :
            InsertFirst(No)
        elif self.Head.Next == None :
            InsertLast(No)
        else :
            for i in range(Pos - 1) :
                temp = temp.Next
            
            newn.Next = temp.Next
            temp.Next = newn

    def DeleteLast(self) :
        print("Iniside DeleteLast")
        temp = self.Head

        if self.Head == None :
            return 
        elif self.Head.Next == None :
            self.Head = None
            return
        else :
            while temp.Next.Next != None :
                temp = temp.Next
            temp.Next = None

    def DeleteAtPos(self,Pos) :
        temp = self.Head

        if self.Head == None :
            DeleteFirst()
        elif self.Head.Next == None :
            DeleteLast()
        else :
            for i in range(Pos - 1) :
                temp = temp.Next
            temp2 = temp.Next
            temp.Next = temp2.Next
            temp2 = None

    def Display(self) :
        temp = self.Head

        while temp != None :
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")

def main() :
    print("Jay Ganesh......")
    print("Enter How Many Number of ELements You Want in LinkedList")
    value = int(input())

    obj = DLinkedList()
    print("Enter ELements in Linked List")
    for i in range(value) :
        print("Enter ELement Number",i + 1)
        obj.InsertFirst(int(input()))
    obj.Display()
    
    for i in range(value) :
        print("Enter ELement Number",i + 3)
        obj.InsertLast(int(input()))
    obj.Display()

    print("Enter Position To Insert Element")
    No = int(input())

    print("Enter Element You Want To insert At Given Position")
    Value = int(input())

    obj.InsertAtPos(Value,No)
    obj.Display()

    obj.DeleteFirst()
    obj.Display()
    obj.DeleteLast()

    obj.Display()

    print("Enter Position You Want To Delete")
    value2 = int(input())

    obj.DeleteAtPos(value2)
    obj.Display()
if __name__ == "__main__" :
    main()