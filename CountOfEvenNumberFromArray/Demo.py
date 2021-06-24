class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = []
    def Accept(self) :
        print("Enter Elements in LIST") 
        for i in range(self.size) :
            print("Enter ELement Number",i + 1)
            self.arr.append(int(input()))

    def Display(self) :
        i = 0
        for i in range(self.size) :
            print(self.arr[i],end = " ") 
    
    def Frequency(self) :
        i = 0
        iCnt = 0

        for i in range(self.size) :
            if self.arr[i] % 2 == 0 :
                iCnt = iCnt + 1
        
        return iCnt

def main() :
    No = 0
    ret = 0

    print("Jay Ganesh......")
    print("Enter Number of Elements You Want in array")
    No = int(input())

    obj = LIST(No) 
    obj.Accept()
    obj.Display()
    ret = obj.Frequency()
    print("\nFrequency of Even Number is",ret)

if __name__ == "__main__" :
    main()
