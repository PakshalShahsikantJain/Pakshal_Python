class Binary :
    def __init__(self) :
        self.Value = 0
        self.Value2 = 0
    
    def __del__(self) :
        print("\nDeallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter First Number")
        self.Value = int(input())

        print("Enter Second Number")
        self.Value2 = int(input())
    
    def Display(self) :
        Rem = 0
        Rem2 = 0
        iCnt = 0
        iCnt2 = 0
        i = 0

        while self.Value != 0 and self.Value2 != 0 :
            Rem = self.Value % 2
            Rem2 = self.Value2 % 2 
            
            if Rem == 1 :
                iCnt = iCnt + 1
            elif Rem2 == 1 :
                iCnt2 = iCnt + 1
            
            if iCnt == iCnt2 :
                print(i,end = " ")
            i = i + 1
            
            self.Value = self.Value // 2
            self.Value2 = self.Value2 // 2
    

def main() :
    print("Jay Ganesh.....")
    obj = Binary()
    obj.Accept()
    obj.Display()

if __name__ == "__main__" :
    main()