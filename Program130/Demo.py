class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = [] 
    
    def Accept(self) :
        print("Please Enter Your String")
        self.str = input()
        self.arr = list(self.str)
    
    def Display(self) :
        print(self.arr)
    
    def Convert(self) :
        i = 0
        brr = [] 

        for i in range(len(self.str)) :
            k = ord(self.arr[i])

            if self.arr[i] >= 'A' and self.arr[i] <= 'Z' :
                self.arr[i] = chr(k + 32)
                brr.append(self.arr[i])
            else :
                brr.append(self.arr[i])
        
        return brr

def main() :
    print("Jay Ganesh......")
    obj = LIST()
    obj.Accept()
    obj.Display()
    brr = obj.Convert()
    print("Converted LIST is :")
    print(brr)

if __name__ == "__main__" :
    main()