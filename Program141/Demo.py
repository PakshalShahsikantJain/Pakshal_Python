class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = []
        self.brr = []
        self.No = 0
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter Your String")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Index Number Till You Want Ti Copy String")
        self.No = int(input())
    
    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def CopyStr(self) :
        i = 0

        for i in range(self.No) :
            self.brr.append(self.arr[i])
        
        return self.brr

def main() :
    print("Jay Ganesh.......")
    brr = [] 

    obj1 = LIST()
    obj1.Accept()
    obj1.Display()
    brr = obj1.CopyStr()
    print("Copied String is :",brr)

    obj2 = LIST()
    obj2.Accept()
    obj2.Display()
    brr = obj2.CopyStr()
    print("Copied String is :",brr)

    del obj1
    del obj2

if __name__ == "__main__" :
    main()