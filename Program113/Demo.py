class LIST :
    def __init__(self,no = 10) :
        self.size = no 
        self.arr = [] 
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number :",i + 1)
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def Digi(self) :
        i = 0
        iCnt = 0

        print("Output :")
        for i in range(self.size) :
            No = self.arr[i]

            iCnt = 0
            while No != 0 : 
                No = No // 10
                iCnt = iCnt + 1
            
            if iCnt == 3 :
                print(self.arr[i],end = " ")

def main() :
    No = 0

    print("Jay Ganesh........")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    obj.Digi()

if __name__ == "__main__" :
    main()