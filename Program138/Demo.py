class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = []
        self.ch = " "
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter String You Want")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Character You Want")
        self.ch = input()

    def Display(self) :
        print("Enter Data is :",self.arr)
    
    def LastOccurance(self) :
        i = 0

        for i in range(len(self.str) - 1,-1,-1) :
            if self.arr[i] == self.ch :
                break
        
        if self.arr[i] == self.ch :
            return i

def main() :
    print("Jay Ganesh.......")
    
    ret = 0

    obj1 = LIST()
    obj1.Accept()
    obj1.Display()
    ret = obj1.LastOccurance()
    print("Last Occurance is at index Number :",ret)

    obj2 = LIST()
    obj2.Accept()
    obj2.Display()
    ret = obj2.LastOccurance()
    print("Last Occurance is at index Number :",ret)

    del obj1
    del obj2
if __name__ == "__main__" :
    main()