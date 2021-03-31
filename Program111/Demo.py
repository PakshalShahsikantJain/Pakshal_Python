class LIST :
    def __init__(self,no = 10) :
        self.size = no 
        self.arr = [] 

    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter ELement Number",i + 1)
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Entered Data is :",self.arr)

    def Min(self) :
        i = 0
        Min = 0

        Min = self.arr[i] 
        for i in range(self.size) :
            if self.arr[i] < Min :
                Min = self.arr[i]

        return Min

def  main() :
    No = 0
    ret = 0

    print("Jay Ganesh......")
    print("Enter How Many Elements You Wnat in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.Min()

    print("Smallest Number is :",ret)
    
if __name__ == "__main__" :
    main()
