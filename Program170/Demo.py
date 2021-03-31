class String :
    def __init__(self) :
        self.str = " "
        self.str2 = " "
        self.arr = []
        self.brr = [] 
        self.No = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")
        
    def Accept(self) :
        print("Enter First String")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Another String")
        self.str2 = input()
        self.brr = list(self.str2)

        print("Enter Number of Characters You Want To Concat")
        self.No = int(input())
    
    def ConStr(self) :
        i = 0
        
        if self.No > len(self.str2) :
            self.arr.append(self.brr)
        else :
            for i in range(self.No) :
                self.arr.append(self.brr[i])
        
        return self.arr
def main() :
    print("Jay Ganesh.....")
    brr = [] 
    
    obj1 = String()
    obj1.Accept()
    brr = obj1.ConStr()
    print("Modified String is :",brr)

if __name__ == "__main__" :
    main()