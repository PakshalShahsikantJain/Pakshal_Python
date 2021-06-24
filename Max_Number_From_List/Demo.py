class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = [] 
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1) 
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def Max(self) :
        Max = 0

        for i in range(self.size) :
            if self.arr[i] > Max :
                Max = self.arr[i]
        
        return Max

def main() :
    No = 0
    ret = 0

    print("Jay Ganesh.......")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.Max()
    print("Largest Number is :",ret)
    
if __name__ == "__main__" :
    main()
