class Binary :
    def __init__(self) :
        self.Value = 0
        self.Pos = 0
        self.Mask = 0X00000001
        self.Res = 0
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter Position You Want To Check")
        self.Pos = int(input())
    
    def Check(self) :
        if self.Pos < 1 or self.Pos > 32 :
            return False
        
        self.Mask = self.Mask << self.Pos
        self.Res = self.Value & self.Mask

        if self.Res == self.Mask :
            return True 
        else :
            return False
         
def main() :
    print("Jay Ganesh.......")
    bret = False 

    obj1 = Binary()
    obj1.Accept()
    bret = obj1.Check()
    if bret == True :
        print("Bit is ON")
    else :
        print("Bit is OFF")

    obj2 = Binary()
    obj2.Accept()
    bret = obj2.Check()
    if bret == True :
        print("Bit is ON")
    else :
        print("Bit is OFF")

    del obj1
    del obj2
if __name__ == "__main__" :
    main()