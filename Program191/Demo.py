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
    
    def Perfect(self) :
        temp = self.Head
        sum = 0
        while temp != None :
            for i in range(1,temp.Data) :
                if temp.Data % i == 0 :
                    sum = sum + i
                    #print(sum)
            
            if sum == temp.Data :
                print(temp.Data,end = " ")
            temp = temp.Next
            sum = 0

def main() :
    print("Jay Ganesh.......")
    print("Enter How Many Number of Elements You Want in Linked List")
    no = int(input())
    obj = LinkedList()
    for i in range(no) :
        print("Enter Element Number",i + 1)
        obj.Insert(int(input()))
    #obj.Display()
    obj.Perfect()
if __name__ == "__main__" :
    main()