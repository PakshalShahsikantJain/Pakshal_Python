class String :
    def __init__(self) :
        self.str = " "
        self.arr = []
        self.brr = []

    def __del__(self) :
        print("Deallocating Memory of Objects")
    
    def Accept(self) :
        print("Enter One String")
        self.str = input()
        self.arr = list(self.str)

    def Display(self) :
        print("Entered Data is :",self.arr)

    def Check(self) :
        i = 0
        for i in range(len(self.str) - 1,-1,-1) :
            self.brr.append(self.arr[i])
        
        if self.arr == self.brr :
            return True 
        else :
            return False 
def main() :
    print("Jay Ganesh....")
    bret = False 

    obj1 = String()
    obj1.Accept()
    obj1.Display()
    bret = obj1.Check()
    if bret == True :
        print("String is Pallindrome")
    else :
        print("String is Not Pallindrome")

    obj2 = String()
    obj2.Accept()
    obj2.Display()
    bret = obj2.Check()
    if bret == True :
        print("String is Pallindrome")
    else :
        print("String is Not Pallindrome")
if __name__ == "__main__" :
    main()