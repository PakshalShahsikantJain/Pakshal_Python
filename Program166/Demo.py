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
        print("Enter One Number You Want")
        self.Value = int(input())

        print("Enter How Many Poisition You Want To Toogle")
        self.No = int(input())

        print("Enter Poisitions")
        for i in range(self.No) :
            print("Enter Poition Number",i + 1)
            self.Pos = int(input())
            self.List.append(self.Pos)
    
    def Toggle(self) :
        if self.Pos < 0 and self.Pos > 32 :
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
    ret = obj1.Toggle()
    print("Modified Number is :",ret)

    obj2 = Binary()
    obj2.Accept()
    ret = obj2.Toggle()
    print("Modified Number is :",ret)

    del obj1
    del obj2

if __name__ == "__main__" :
    main()