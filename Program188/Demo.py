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

    def Display(self) :
        while self.Head != None  :
            print("|",self.Head.Data,"|","->",end = " ")
            self.Head = self.Head.Next
        print("None")
    
    def Addition(self) :
        temp = self.Head
        sum = 0
        while temp != None :
            sum = sum + temp.Data
            temp = temp.Next

        return sum 

def main() :
    print("Jay Ganesh......")
    ret = 0
    obj = LinkedList()

    print("Enter Number of Elemensts You Want in Linked List")
    no = int(input())

    for i in range(no) :
        print("Enter Element Number",i + 1)
        obj.Insert(int(input()))

    #obj.Display()
    ret = obj.Addition()
    print("Addition is :",ret)

if __name__ == "__main__" :
    main()