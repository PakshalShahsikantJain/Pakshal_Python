class Binary :
    def __init__(self) :
        self.Value = 0
        self.Pos = 0
        self.List = []
        self.No = 0
        self.Mask = 0X00000001
        self.Res = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter How Many Poition You Want To Check")
        self.No = int(input())

        print("Enter Poition's") 
        for i in range(self.No) :
            print("Enter Poition Number ",i + 1)
            self.Pos = int(input())
            self.List.append(self.Pos)
    
    def Check(self) :
        if self.Pos < 0 and self.Pos > 32 :
            return False
        for i in range(self.No) :
            self.Mask = self.Mask << self.List[i]
            self.Res = self.Value & self.Mask
            if self.Res == self.Mask :
                break
            self.Mask = 0X00000001
        
        if self.Res == self.Mask :
            return True 
        else :
            return False

def main() :
    print("Jay Ganesh.....")
    bret = False 

    obj = Binary()
    obj.Accept()
    bret = obj.Check()
    if bret == True :
        print("One or More Bits are On")
    else :
        print("Bits are OFF")

    obj2 = Binary()
    obj2.Accept()
    bret = obj2.Check()
    if bret == True :
        print("Bits are On")
    else :
        print("Bits are OFF")

if __name__ == "__main__" :
    main()
