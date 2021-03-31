class Binary :
    def __init__(self) :
        self.Value = 0
        self.No = 0
        self.Pos = 0
        self.Mask = 0X00000001
        self.Res = 0
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter How Many Bits You Want To ON")
        self.No = int(input())

    def OnBit(self) :
        i = 0

        for i in range(self.No) :
            self.Mask = self.Mask << i
            self.Res = self.Value | self.Mask

            self.Mask = 0X00000001
            self.Value = self.Res
        
        return self.Res
def main() :
    ret = 0
    print("Jay Ganesh......")
    obj1 = Binary()
    obj1.Accept()
    ret = obj1.OnBit()
    print("Modified Number is :",ret)

if __name__ == "__main__" :
    main()