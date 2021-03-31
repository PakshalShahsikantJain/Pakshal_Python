class Binary :
    def __init__(self) :
        self.Value = 0
        self.Pos = 0
        self.No = 0
        self.List = []
        self.Mask = 0X00000001
        self.Result = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter How Many Number of Postion's You Want To Check,Bit is ON or OFF")
        self.No = int(input())

        print("Enter Postion's")
        for i in range(self.No) :
            print("Enter Position Number :",i + 1)
            self.Pos = int(input())
            self.List.append(self.Pos)
    
    def Check(self) :
        if self.Value < 0 :
            self.Value = -self.Value
        
        if self.Pos < 0 or self.Pos > 32 :
            return False
        
        for i in range(self.No) :
            self.Mask = self.Mask << self.List[i]
            self.Result = self.Value & self.Mask
            if self.Result == self.Mask :
                break
        
        if self.Result == self.Mask :
            return True 
        else :
            return False

def main() :
    print("Jay Ganesh......")
    bret = False

    obj1 = Binary()
    obj1.Accept()
    bret = obj1.Check()
    if bret == True :
        print("Bits are ON")
    else :
        print("Bits are OFF")

    obj2 = Binary()
    obj2.Accept()
    bret = obj2.Check()
    if bret == True :
        print("Bits are ON")
    else :
        print("Bits are OFF")

    del obj1
    del obj2
if __name__ == "__main__" :
    main()