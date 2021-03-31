class Alphabet :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Character You Want To Check")
        self.ch = input()

    def Check(self) :
        if self.ch >= 'A' and self.ch <= 'Z' :
            return True 
        elif self.ch >= 'a' and self.ch <= 'z' :
            return True
        else :
            return False

def main():
    bret = False

    print("Jay Ganesh.....")
    obj = Alphabet()
    obj.Accept()
    bret = obj.Check()
    if bret == True :
        print("Character is Alphabet")
    else :
        print("Character is Not Alphabet")

if __name__ == "__main__" :
    main()