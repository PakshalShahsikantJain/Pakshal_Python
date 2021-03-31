class Node :
    def __init__(self) :
        self.Data = None
        self.Next = None

class LinkedList(Node) :
    def __init__(self) :
        self.Head = None
        Node.__init__(self) 
    
    def Insert(self,No) :
        newn = 0

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
        while self.Head != None :
            print("|",self.Head.Data,"|","->",end = " ")
            self.Head = self.Head.Next
        print("None")

    def LastOccurance(self,value) :
        i = 0
        iCnt = 0

        while self.Head != None :
            if self.Head.Data == value :
                iCnt = i
            self.Head = self.Head.Next
            i = i + 1

        return iCnt
def main() :
    print("Jay Ganesh........")
    obj = LinkedList()
    ret = 0
    print("Enter Number of Elements You Want in Linked List")
    no = int(input())

    for i in range(no) :
        print("Enter First Elements",i + 1)
        obj.Insert(int(input()))
    
    obj.Display()
    
    for i in range(no) :
        print("Enter First Elements",i + 1)
        obj.Insert(int(input()))
    print("Enter Which Number You Want To Search LastOccurance of")
    No = int(input())
    ret = obj.LastOccurance(No)
    print("Last Occurance is at Index Number",ret)
if __name__ == "__main__" :
    main()