class Alphabet :
    def __init__(self) :
        self.ch = " "
        self.ch2 = " "
    
    def Accept(self) :
        print("Enter Starting Character")
        self.ch = input()
        print("Enter Ending Character")
        self.ch2 = input()
    
    def Display(self) :
        i = 0

        k = ord(self.ch) 

        if self.ch >= 'A' and self.ch <= 'Z' :
            for i in range(k,ord(self.ch2) + 1,1) :
                print(chr(k),end = " ")
                k = k + 1
        elif self.ch >= 'a' and self.ch <= 'z' :
            for i in range(k,ord(self.ch2) - 1,-1) :
                print(chr(k),end = " ")
                k = k - 1
        else :
            return -1
            

def main():
    print("Jay Ganesh.....")
    obj = Alphabet()
    obj.Accept()
    obj.Display()

if __name__ == "__main__" :
    main()
