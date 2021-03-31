class String :
    def __init__(self) :
        self.str = " "
        self.arr = [] 
        self.brr = []

    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter One String")
        self.str = input()
        self.arr = list(self.str)

    def Display(self) :
        print("Entered Data is :",self.arr)

    def ReverseStr(self) :
        i = 0

        for i in range(len(self.str) - 1,-1,-1) :
            if self.arr[i] >= 'A' and self.arr[i] <= 'Z' :
                k = ord(self.arr[i])
                k = k + 32
                self.brr.append(chr(k))
            elif self.arr[i] >= 'a' and self.arr[i] <= 'z' :
                k = ord(self.arr[i])
                k = k - 32
                self.brr.append(chr(k))
            else :
                self.brr.append(self.arr[i])
        
        return self.brr
def main() :
    print("Jay Ganesh......")
    brr = [] 

    obj1 = String()
    obj1.Accept()
    obj1.Display()
    brr = obj1.ReverseStr()
    print("ModiFied String is :",brr)

    obj2 = String()
    obj2.Accept()
    obj2.Display()
    brr = obj2.ReverseStr()
    print("ModiFied String is :",brr)

    del obj1
    del obj2
if __name__ == "__main__" :
    main()