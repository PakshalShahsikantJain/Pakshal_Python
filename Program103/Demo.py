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
        
        print("Enter Element You Want To Check")
        self.No = int(input())

    def Display(self) :
        print("Entered Elements are :")
        for i in range(self.size) :
            print(self.arr[i],end = " ") 

    def Frequency(self) :
        i = 0
        iCnt = 0

        for i in range(self.size) :
            if self.arr[i] == self.No :
                iCnt = iCnt + 1
        
        return iCnt

def main() :
    No = 0
    ret = 0

    print("Ganapati Bappa Morya............")
    print("Enter Number of Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.Frequency()

    print("\nFrequency of 11 is :",ret)

if __name__ == "__main__" :
    main()