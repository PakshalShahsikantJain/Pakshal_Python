class Binary :
    def __init__(self) :
        self.Value = 0
        self.Pos = 0
        self.No = 0
        self.List = []
        self.Mask = 0X00000001
        self.Res = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter How Many Number of Postion's You Want To off The Bit")
        self.No = int(input())

        print("Enter Position's")
        for i in range(self.No) :
            print("Enter Position Number",i + 1)
            self.Pos = int(input())
            self.List.append(self.Pos)
    
    def OffBit(self) :
        if self.Value < 0 :
            self.Value = -self.Value
        
        if self.Pos < 0 or self.Pos > 32 :
            return -1
        
        for i in range(self.No) :
            self.Mask = self.Mask << self.List[i]
            self.Res = self.Value ^ self.Mask 
            self.Mask = 0X00000001
            self.Value = self.Res
            
        return self.Res

def main() :
    print("Jay Ganesh......")
    ret = 0

    obj1 = Binary()
    obj1.Accept()
    ret = obj1.OffBit()
    print("Modied Number is :",ret)

    obj2 = Binary()
    obj2.Accept()
    ret = obj2.OffBit()
    print("Modied Number is :",ret)

    del obj1
    del obj2

if __name__ == "__main__" :
    main()