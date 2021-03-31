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
    
    def Display(self):
        temp = self.Head
        while temp != None : 
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")
    
    def Min(self) :
        temp = self.Head 
        Digi  = 0
        Min = 0

        print("Smallest digits of all element from singly linear linked list")
        while temp != None :
            Min = temp.Data
            while temp.Data != 0 :
                Digi = temp.Data % 10
                if Digi < Min :
                    Min = Digi
                temp.Data = temp.Data // 10
            print(Min," ",end = " ")
            temp = temp.Next
            Min = 0
def main() :
    print("Jay Ganesh......")
    obj = LinkedList()

    print("Enter How Many Number of ELements You Want in Linked List")
    value = int(input())

    print("Enter Elements in Linked List")
    for i in range(value) :
        print("Enter Element Number",i + 1)
        obj.Insert(int(input()))
    
    #obj.Display()
    obj.Min()

if __name__ == "__main__" :
    main()