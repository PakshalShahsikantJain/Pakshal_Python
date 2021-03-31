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

    def Difference(self) :
        i = 0
        small = 0
        capital = 0

        for i in range(len(self.str)) :
            if self.arr[i] >= 'A' and self.arr[i] <= 'Z' :
                capital = capital + 1
            else :
                small = small + 1
        
        return small - capital

def main() :
    ret = 0

    print("Jay Ganesh.......")
    obj = LIST()
    obj.Accept()
    obj.Display()
    ret = obj.Difference()
    print("Difference between Frequency of small and Capital Letter is :",ret)
if __name__ == "__main__" :
    main()