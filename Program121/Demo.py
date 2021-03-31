class Alphabet :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Character You Want To Check")
        self.ch = input()
    
    def Convert(self) :

        k = ord(self.ch)

        if self.ch >= 'A' and self.ch <= 'Z' :
            print(chr(k + 32))
        elif self.ch >= 'a' and self.ch <= 'z':
            print(chr(k - 32))
        else :
            print(self.ch)
        

def main() :
    print("Jay Ganesh......")
    obj = Alphabet()
    obj.Accept()
    obj.Convert()

if __name__ == "__main__" :
    main()