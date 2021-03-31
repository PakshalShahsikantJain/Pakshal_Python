class LIST :
    def __init__(self,no = 10) :
        self.size = no 
        self.arr = []

    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element NUmber :",i + 1)
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Elements which are Multiples of 11 are :")
        for i in range(self.size) :
            if self.arr[i] % 11 == 0:
                print(self.arr[i],end = " ")

def main() :
    No = 0
    print("Jay Ganesh......")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())
    
    obj = LIST(No)
    obj.Accept()
    obj.Display()

if __name__ == "__main__" :
    main()