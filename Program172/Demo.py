class String :
    def __init__(self) :
        self.str = " "
        self.str2 = " "
        self.No = 0
        self.arr = []
        self.brr = []
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter First String")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Second String")
        self.str2 = input()
        self.brr = list(self.str2)

        print("Enter One Number Till You Want To iterate")
        self.No = int(input())
    
    def Check(self) :
        i = 0
        for i in range(self.No) :
            if self.arr[i] == self.brr[i] :
                continue 
            else :
                break
        
        if self.arr[i] == self.brr[i] :
            return True 
        else :
            return False
def main() :
    print("Jay Ganesh......")
    bret = 0

    obj1 = String()
    obj1.Accept()
    bret = obj1.Check()
    if bret == True :
        print("Both String are Equal")
    else :
        print("Both Strings are Not Equal")

    obj2 = String()
    obj2.Accept()
    bret = obj2.Check()
    if bret == True :
        print("Both String are Equal")
    else :
        print("Both Strings are Not Equal")

if __name__ == "__main__" :
    main()