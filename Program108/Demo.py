class LIST :
    def __init__(self,no = 0) :
        self.size = no 
        self.arr = [] 
        self.start = 0
        self.end = 0
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1 )
            self.arr.append(int(input()))
        
        print("Enter Number To Start")
        self.start = int(input())
        print("Enter Number To End")
        self.end = int(input())

    def Display(self) :
        print("Entered Data is :",self.arr)
    
    def Display2(self) :
        print("Elements In Entered Range are :")
        for i in range(self.size) :
            if self.arr[i] >= self.start and self.arr[i] <= self.end :
                print(self.arr[i],end = " ")

def main() :
    No = 0

    print("Jay Ganesh..........")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    obj.Display2()

if __name__ == "__main__" :
    main()