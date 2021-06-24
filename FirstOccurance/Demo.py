class LIST :
    def __init__(self,no = 10) :
        self.size = no 
        self.arr = [] 
        self.No = 0

    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1)
            self.arr.append(int(input()))
        print("Enter Element You Want To Check")
        self.No = int(input())

    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def FirstOccurance(self) :
        i = 0
        Index = 0

        for i in range(self.size) :
            if self.arr[i] == self.No :
                Index = i 
                break

        if self.arr[i] == self.No :
            return Index 
    
def main() :
    No = 0
    ret = 0

    print("Jay Ganesh......")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())
    
    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.FirstOccurance() 

    print("First Occurance of Entered Element is at Index Number : ",ret)

if __name__ == "__main__" :
    main()
    
