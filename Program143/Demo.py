class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = []
        self.brr = []
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter String You Want")
        self.str = input()
        self.arr = list(self.str)

    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def CopyStr(self) :
        i = 0

        for i in range(len(self.str)) :
            if self.arr[i] >= 'a' and self.arr[i] <= 'z' :
                self.brr.append(self.arr[i])
            elif self.arr[i] == ' ' :
                self.brr.append(self.arr[i])
                
        return self.brr
def main() :
    print("Jay Ganesh........")
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