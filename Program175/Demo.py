class String :
    def __init__(self) :
        self.str = " " 
        self.arr = []
        self.cnt = 0

    def __del__(self) :
        print("Deallocating Memory of Objects")

    def Accept(self) :
        print("Enter One String")
        self.str = input()
        self.arr = list(self.str)
    
    def Display(self) :
        print("Entered String is :",self.arr)

    def Count(self) :
        i = 0

        self.cnt = self.cnt + 1
        for i in range(len(self.str)) :
            if self.arr[i] == ' ' :
                self.cnt = self.cnt + 1
        
        return self.cnt
def main() :
    print("Jay Ganesh.......")
    ret = 0

    obj = String()
    obj.Accept()
    obj.Display()
    ret = obj.Count()
    print("Count of Words is :",ret)

if __name__ == "__main__" :
    main()