class Binary :
    def __init__(self) :
        self.Value = 0
        self.Pos = 0
        self.Mask = 0X00000001
        self.Result = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())
        
        print("Enter Position To OFF That Bit")
        self.Pos = int(input())
    
    def OFFBit(self) :
        if self.Pos < 0 or self.Pos > 32 :
            return -1

        self.Mask = self.Mask << self.Pos
        self.Result = self.Value ^ self.Mask

        return self.Result 

def main() :
    print("Jay Ganesh.....")
    ret = 0

    obj1 = Binary()
    obj1.Accept()
    ret = obj1.OFFBit()
    print("Modified Number is :",ret)

    obj2 = Binary()
    obj2.Accept()
    ret = obj2.OFFBit()
    print("Modified Number is :",ret)

    del obj1
    del obj2
    
if __name__ == "__main__" :
    main()