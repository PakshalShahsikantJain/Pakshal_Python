class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = [] 
        self.ch = " "
    
    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter String")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Character You Want To Check")
        self.ch = input()

    def Display(self) :
        print(self.arr)
    
    def Frequency(self) :
        i = 0
        iCnt = 0
        for i in range(len(self.str)) :
            if self.arr[i] == self.ch :
                iCnt = iCnt + 1

        return iCnt

def main() :
    iret = 0
    print("Jay Ganesh........")
    obj1 = LIST()

    obj1.Accept()
    obj1.Display()
    iret = obj1.Frequency()
    print("Frequency of Entered Character is :",iret)
    
    obj2 = LIST()

    obj2.Accept()
    obj2.Display()
    iret = obj2.Frequency()
    print("Frequency of Entered Character is :",iret)

    del obj1
    del obj2

if __name__ == "__main__" :
    main()
