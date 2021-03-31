class LIST :
    def __init__(self) :
        self.str = " "
        self.str2 = " "
        self.arr = []
        self.brr = []
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter String You Want")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Another String")
        self.str2 = input()
        self.brr = list(self.str2)

    def Display(self) :
        print("Entered Data is :",self.arr)
        print("2nd Entered Data is :",self.brr)

    def ConCatStr(self) :
        i = 0

        for i in range(len(self.str2)) :
            self.arr.append(self.brr[i])

        return self.arr
        
def main() :
    print("Jay Ganesh........")
    brr = []

    obj1 = LIST()
    obj1.Accept()
    obj1.Display()
    brr = obj1.ConCatStr()
    print("Concated String is :",brr)
    
    obj2 = LIST()
    obj2.Accept()
    obj2.Display()
    brr = obj2.ConCatStr()
    print("Concated String is :",brr)

    del obj1
    del obj2

if __name__ == "__main__" :
    main()