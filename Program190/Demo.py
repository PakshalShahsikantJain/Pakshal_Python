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

        newn.Data = No
        newn.Next = None

        if self.Head == None :
            self.Head = newn 
        else :
            newn.Next = self.Head
            self.Head = newn
    
    def Display(self)  :
        temp = self.Head
        while temp != None :
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")
    
    def Mini(self) :
        temp = self.Head
        Min = 0

        Min = temp.Data
        while temp != None :
            if temp.Data < Min :
                Min = temp.Data
            temp = temp.Next
        
        return Min
def main() :
    print("Jay Ganesh.......")
    ret = 0;
    print("Enter Number of Elements You Want in Linked List")
    No = int(input())
    
    obj = LinkedList()

    for i in range(No) :
        print("Enter Element Number",i + 1) 
        obj.Insert(int(input()))

    #obj.Display()
    ret = obj.Mini()
    print("Smallest Number is :",ret);
    
if __name__ == "__main__" :
    main()