class Binary :
    def __init__(self) :
        self.Value = 0
        #self.No = 0
        self.Pos = 0
        #self.List = [] 
        self.Mask = 0X00000001
        self.Res = 0
    
    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

        print("Enter Position Which You Want To OFF Bit")
        self.Pos = int(input())

    def OffBit(self) :
        self.Mask = self.Mask << self.Pos
        self.Res = self.Value ^ self.Mask

        return self.Res

def main() :
    print("Jay Ganesh.......")
    ret = 0

    obj1 = Binary()
    obj1.Accept()
    ret = obj1.OffBit()
    print("Modified Number is :",ret)
    
if __name__ == "__main__":
    main()