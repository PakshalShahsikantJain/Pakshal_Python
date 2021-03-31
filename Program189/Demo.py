class Node :
    def __init__(self) :
        self.Data = None
        self.Next = None

class LinkedList(Node) :
    def __init__(self) :
        Node.__init__(self)
        self.Head = None
    
    def Insert(self,No) :
        newn = None

        newn = Node()
        Data = self.Data
        Next = self.Next

        newn.Next = None
        newn.Data = No

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
        temp = self.Head 
        max = 0
        while temp != None :
            if temp.Data > max :
                max = temp.Data
            temp = temp.Next
        
        return max

def main() :
    print("Jay Ganesh........")
    ret = 0
    print("Enter How Many Number of Elements You Want In Linked List")
    No = int(input())
    
    obj = LinkedList()

    for i in range(No) :
        print("Enter ELement Number :",i + 1)
        obj.Insert(int(input()))
    
    #obj.Display()
    ret = obj.Max()
    print("Maximum Number is :",ret)
    
if __name__ == "__main__" :
    main() 