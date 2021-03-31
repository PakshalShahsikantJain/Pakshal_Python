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
        while self.Head != None :
            print("|",self.Head.Data,"|","->",end = " ")
            self.Head = self.Head.Next
        print("None")

    def SearchFirstOCC(self,Value) :
        i = 0
        temp = self.Head

        while temp != None :
            if temp.Data == Value :
                break
            temp = temp.Next
            
            i = i + 1
        
        return i
def main() :
    print("Jay Ganesh.......")
    obj = LinkedList()
    obj.Insert(13)
    obj.Insert(12)
    obj.Insert(11)
    obj.Display()

    obj.Insert(13)
    obj.Insert(12)
    obj.Insert(11)
    print("Enter One Number You Want To Search")
    No = int(input())
    ret = obj.SearchFirstOCC(No)
    print("First Occurance is at",ret)

if __name__ == "__main__" :
    main()