class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = [] 
    
    def Accept(self) :
        print("Enter String")
        self.str = input()
        self.arr = list(self.str)
    
    def Display(self) :
        print(self.arr)

    def Count(self) :
        i = 0
        iCnt = 0

        for i in range(len(self.str)) :
            if self.arr[i] >= 'a' and self.arr[i] <= 'z' :
                iCnt = iCnt + 1

        return iCnt                    
def main() :
    ret = 0

    print("Jay Ganesh......")
    obj = LIST()
    obj.Accept()
    obj.Display()
    ret = obj.Count()
    print("Count of Small Character is :",ret)
    
if __name__ == "__main__" :
    main()