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
        Data = self.Head 
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

    def Reverse(self) :
        temp = self.Head

        print("Reversed Data is :")
        while temp != None :
            Digi = 0
            print("|",end = "")
            while temp.Data != 0 :
                Digi = temp.Data % 10
                print(Digi,end = "")
                temp.Data = temp.Data // 10
            print("|->",end = "")
            temp = temp.Next
        print("None",end = " ")

def main() :    
    print("Jay Ganesh..........")
    print("Enter How Many Number of Elements You Want in Linked List")
    value = int(input())
    obj = LinkedList()

    print("Enter Elements in Linked List")
    for i in range(value) :
        print("Enter ELement Number",i + 1)
        obj.Insert(int(input()))
    
    #obj.Display()
    obj.Reverse()

if __name__ == "__main__" :
    main()