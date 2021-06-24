class LIST :
    def __init__(self,no = 10) :
        self.size = no 
        self.arr = []
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter ELement NUmber :",i + 1)
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Entered Data is :",self.arr)

    def ODD(self) :
        i = 0
        Mult = 1

        for i in range(self.size) :
            if self.arr[i] % 2 != 0 :
                Mult = Mult * self.arr[i]
            else :
                Mult = 0
        
        return Mult 

def main() :
    No = 0
    ret = 0

    print("Jay Ganesh.....")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No) 
    obj.Accept()
    obj.Display()
    ret = obj.ODD()
    print("Product of ODD Element is :",ret)

if __name__ == "__main__" :
    main()
