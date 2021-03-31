class Node :
    def __init__(self) :
        self.Data = None
        self.Next = None

class LinkedList(Node) :
    def __init__(self) :
        self.Head = None
        Node.__init__(self) 

    def Insert(self,No) :
        newn = None

        newn = Node()
        Data = self.Data
        Next = self.Next

        newn.Data = No
        newn.Next = None

        if self.Head == None :
            self.Head = newn
        else :
            newn.Next = self.Head
            self.Head = newn
        
    def Display(self) :
        temp = self.Head
        while temp != None :
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")

    def Max(self) :
        Max = 0
        Max2 = 0

        temp = self.Head

        while temp != None :
            if temp.Data > Max :
                Max2 = Max
                Max = temp.Data
            elif temp.Data > Max2 and temp.Data != Max :
                Max2 = temp.Data

            temp = temp.Next
        
        return Max2
def main() :
    print("Jay Ganesh.......")
    
    obj = LinkedList()

    print("Enter How Many Number of Elements You Want In Linked List")
    No = int(input())

    print("Enter Elements in Linked List")
    for i in range(No) :
        print("Enter Element Number",i + 1)
        obj.Insert(int(input()))

    #obj.Display()
    ret = obj.Max()
    print("Second Maximum Number is :",ret)
if __name__ == "__main__" :
    main()