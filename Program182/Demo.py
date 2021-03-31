class Node :
    def __init__(self) :
        self.Data = None 
        self.Next = None

class LinkedList(Node) :
    def __init__(self) :
        Node.__init__(self)
        self.Head = None

    def Insert(self,No) :
        #print("\nInside Insert")
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
        #print("Inside Display")
        #iCnt = 0
        while self.Head != None :
            print("|",self.Head.Data,"|","->",end = " ")
            #iCnt = iCnt + 1
            self.Head = self.Head.Next
        print("Null",end = " ")

    def Count(self) :
        iCnt = 0  
        while self.Head != None :
            #print("|",self.Head.Data,"|","->",end = " ")
            self.Head.Data
            iCnt = iCnt + 1
            self.Head = self.Head.Next
        
        return iCnt
def main() :
    print("Jay Ganesh.....")
    obj = LinkedList()

    obj.Insert(200)
    obj.Insert(111)
    obj.Insert(101)
    obj.Insert(100)
    obj.Insert(200)
    obj.Insert(200)
    ret = obj.Count()
    print("Count is :",ret)

if __name__ == "__main__" :
    main()