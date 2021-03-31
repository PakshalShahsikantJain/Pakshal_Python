class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = []
        self.No = 0

    def Accept(self) :
        print("Enter Element in Array")
        for i in range(self.size) :
            print("Enter Element Number ",i + 1)
            self.arr.append(int(input()))
        print("Enter Element You Want To Check")
        self.No = int(input())

    def Display(self) :
        print("Entered Data is :",self.arr)

    def Check(self) :
        for i in range(self.size) :
            if self.arr[i] == self.No :
                break
        
        if self.arr[i] == self.No :
            return True
        else :
            return False

def main() :
    No = 0
    bret = False

    print("Jay Ganesh.......")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    
    bret = obj.Check()
    if bret == True :
        print("Element is Present in LIST")
    else :
        print("Element is Not Present in LIST")
        
if __name__ == "__main__" :
    main()