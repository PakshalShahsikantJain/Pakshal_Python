class Node  :
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
    def Display(self) :
        temp = self.Head 

        while temp != None :
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")

    def Mult(self) :
        mult = 1
        Digi = 0
        temp = self.Head 

        print("Product of all Digits of all Elemets from singly Linear Linked List is :")
        while temp != None :
            while temp.Data != 0  :
                Digi = temp.Data % 10
                if Digi == 0 :
                    Digi = 1
                mult = mult * Digi
                temp.Data = temp.Data // 10
            print(mult," ",end = " ")
            temp = temp.Next
            mult = 1
def  main() : 
    print("Jay Ganesh......")   
    print("Enter How Number of Elements You Want in Linked List")
    value = int(input())
    obj = LinkedList()

    print("Enter Elements in Linked List")
    for i in range(value) :
        print("Enter Element Number",i + 1)
        obj.Insert(int(input()))
    
    #obj.Display()
    obj.Mult()
if __name__ == "__main__" :
    main()