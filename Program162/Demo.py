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

        print("Enter Position To Toggel Bit")
        self.Pos = int(input())

    def OffBit(self) :
        if self.Pos < 0 or self.Pos > 32 :
            return -1
        
        self.Mask = self.Mask << self.Pos 
        self.Res = self.Value ^ self.Mask

        return self.Res
def main() :
    print("Jay Ganesh....")
    ret = 0

    obj1 = Binary()
    obj1.Accept()
    ret = obj1.OffBit()
    print("Modified Number is :",ret)

    obj2 = Binary()
    obj2.Accept()
    ret = obj2.OffBit()
    print("Modified Number is :",ret)

    del obj1
    del obj2
    
if __name__ == "__main__" :
    main()