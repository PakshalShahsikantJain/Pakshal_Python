class Binary :
    def __init__(self) :
        self.Value = 0
        self.Mask = 0X00000001
        self.Res = 0
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter One Number")
        self.Value = int(input())

    def CountBit(self):
        iCnt = 0
        while self.Value :
            iCnt += self.Value & 1 
            self.Value = self.Value >> 1
            continue
        print(iCnt)
def main() :
    print("Jay Ganesh....")
    ret = 0

    obj1 = Binary()
    obj1.Accept()
    obj1.CountBit()

    obj2 = Binary()
    obj2.Accept()
    obj2.CountBit()

    del obj1
    del obj2
    
if __name__ == "__main__" :
    main()