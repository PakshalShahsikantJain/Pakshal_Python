class String :
    def __init__(self) :
        self.str = " "
        self.str2 = " "
        self.arr = []
        self.brr = []
    
    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter First String :")
        self.str = input()
        self.arr = list(self.str)

        print("Enter Second String :")
        self.str2 = input()
        self.brr = list(self.str2)
    
    def Check(self) :
        if self.arr == self.brr :
            return True 
        else :
            return False
    
def main() :
    print("Jay Ganesh......")
    bret = False 

    obj1 = String()
    obj1.Accept()
    bret = obj1.Check()

    if bret == True :
        print("Both String are Same")
    else :
        print("Both Strings are Different")

    obj2 = String()
    obj2.Accept()
    bret = obj2.Check()

    if bret == True :
        print("Both String are Same")
    else :
        print("Both Strings are Different")

    del obj1
    del obj2

if __name__ == "__main__" :
    main()