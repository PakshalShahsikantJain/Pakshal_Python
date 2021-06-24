class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = [] 
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1)
            self.arr.append(int(input()))

    def Display(self) :
        i = 0
        print("Entered Data is : ")
        for i in range(self.size) :
            print(self.arr[i],end = " ")
    
    def Difference(self) :
        i = 0
        Even = 0
        ODD = 0

        for i in range(self.size) :
            if self.arr[i] % 2 == 0 :
                Even = Even + 1
            else :
                ODD = ODD + 1

        return Even - ODD 
def main() :
    No = 0
    ret = 0

    print("Jay Ganesh.......")
    print("Enter Number of Elements You Want In LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.Difference()
    print("\nDifference is :",ret)

if __name__ == "__main__" :
    main()
