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
        temp = self.Head
        while temp != None :
            print("|",temp.Data,"|","->",end = " ")
            temp = temp.Next
        print("None")
    
    def Prime(self) :
        temp = self.Head
        sum = 0
        while temp != None :
            for i in range(1,temp.Data) :
                if temp.Data % i == 0 :
                    sum = sum + i

            if sum == 1 :
                print(temp.Data,end = " ")
            temp = temp.Next
            sum = 0
def main() :
    print("Jay Ganesh......")
    obj = LinkedList()

    print("Enter Number of Elements You Want in Linked List")
    No = int(input())

    for i in range(No):
        print("Enter ELement Number",i + 1)
        obj.Insert(int(input()))
    
    #obj.Display()
    obj.Prime()
if __name__ == "__main__" :
    main()