class Alphabet :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Starting Character")
        self.ch = input()
  
    def Display(self) :
        k = ord(self.ch)

        print(self.ch,ord(self.ch),hex(k),oct(k))

def main():
    print("Jay Ganesh.....")
    obj = Alphabet()
    obj.Accept()
    obj.Display()

if __name__ == "__main__" :
    main()
