class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = [] 
        self.ch = " "
    
    def __del__(self) :
        print("Deallocating Memory of objects")
    
    def Accept(self) :
        print("Enter Your String")
        self.str = input()
        self.arr = list(self.str)

        print("Enter one Character You Want Find First Occurance of :")
        self.ch = input()
    
    def Display(self) :
        print("Enter String is :",self.arr)
    
    def FirstOccurance(self) :
        i = 0

        for i in range(len(self.str) + 1) :
            if self.arr[i] == self.ch :
                break
        
        if self.arr[i] == self.ch :
            return i
        else :
            return -1
def main() :
    print("Jay Ganesh......")
    iret = 0

    obj1 = LIST()
    obj1.Accept()
    obj1.Display()
    iret = obj1.FirstOccurance()
    print("First Occurance of Entered Character is at Index No :",iret)

    obj2 = LIST()
    obj2.Accept()
    obj2.Display()
    iret = obj2.FirstOccurance()
    print("First Occurance of Entered Character is at Index No :",iret)

    del obj1
    del obj2
    
if __name__ == "__main__" :
    main()
