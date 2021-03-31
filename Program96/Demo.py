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
        print("Enterd Data is :")
        for i in range(self.size) :
            print(self.arr[i],end = " ")
    
    def Display2(self) :
        i = 0
        
        print("\nNumber Divisible By 5 are :")
        for i in range(self.size) :
            if self.arr[i] % 5 == 0 :
                print(self.arr[i],end = " ")
def main() :
    No = 0
    print("Jay Ganesh.........")
    print("Enter Number of Elements You Want in LIST")
    No = int(input())

    obj = LIST(No) 
    obj.Accept()
    obj.Display()
    obj.Display2()

if __name__ == "__main__" :
    main()