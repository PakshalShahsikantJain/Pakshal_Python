class LIST :
    def __init__(self) :
        self.str =  " "
        self.arr = [] 
        self.brr = []
    
    def __del__(self) :
        print("Deallocating Memory of Object")
    
    def Accept(self) :
        print("Enter String Which You Want")
        self.str = input()
        self.arr = list(self.str)
    
    def Display(self) :
        print("Entered Data is  :",self.arr)

    def CopyStrSmall(self) :
        i = 0

        for i in range(len(self.str)) :
            if self.arr[i] >= 'A' and self.arr[i] <= 'Z' :
                ch = ord(self.arr[i])
                ch = ch + 32
                self.brr.append(chr(ch))
            else :
                self.brr.append(self.arr[i])
        
        return self.brr

def main() :
    print("Jay Ganesh.....")
    brr = [] 

    obj1 = LIST()
    obj2 = LIST()

    obj1.Accept()
    obj1.Display()
    brr = obj1.CopyStrSmall()
    print("Copied String is :",brr)

    obj2.Accept()
    obj2.Display()
    brr = obj2.CopyStrSmall()
    print("Copied String is :",brr)

if __name__ == "__main__" :
    main()