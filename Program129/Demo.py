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

    def Reverse(self) :
        i = 0
        brr = []

        for i in range(len(self.str) - 1 ,-1,-1) :
            brr.append(self.arr[i])

        return brr    

def main() :
    print("Jay Ganesh......")
    obj = LIST()
    obj.Accept()
    obj.Display()
    brr = obj.Reverse()
    print("Rversed LIST is :")
    print(brr)

if __name__ == "__main__" :
    main()