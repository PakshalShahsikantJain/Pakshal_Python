class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = [] 
        self.No = 0
 
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1)
            self.arr.append(int(input()))

        print("Enter Number You Want To Check")
        self.No = int(input())
    
    def Display(self) :
        i = 0
        print("Entered Data is :")
        for i in range(self.size) :
            print(self.arr[i],end = " ")
    
    def Check(self) :
        i = 0
        for i in range(self.size) :
            if self.arr[i] == self.No :
                break
        
        if self.arr[i] == self.No :
            return True 
        else :
            return False

def main() :
    No = 0
    bret = 0

    print("Jay Ganesh......")
    
    print("Enter Number of Elements in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    bret = obj.Check()

    if bret == True :
        print("\nEnterd Element is Present in LIST")
    else :
        print("\nEntered Element is Not Present in LIST")

if __name__ == "__main__" :
    main()
