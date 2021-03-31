class LIST :
    def __init__(self) :
        self.str = " "
        self.ch = " "
        self.arr = []
    
    def Accept(self) :
        print("Enter String")
        self.str = input()

        print("Enter Character You Want To Check")
        self.ch = input()

        self.arr = list(self.str)
    
    def Display(self) :
        print(self.arr)

    def Check(self) :
        i = 0

        for i in range(len(self.str)) :
            if self.arr[i] == self.ch :
                break

        if self.arr[i] == self.ch :
            return True 
        else :
            return False

def main() :
    bret = False

    print("Jay Ganesh...")
    obj = LIST()
    obj.Accept()
    obj.Display()
    bret = obj.Check()
    if bret == True  :
        print("Entered Character is Present in String")
    else:
        print("Entered Character is Not Present in String")
        
if __name__ == "__main__" :
    main()
