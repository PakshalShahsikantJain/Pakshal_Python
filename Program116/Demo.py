class Alphabet :
    def __init__(self) :
        self.ch = " "

    def Accept(self) :
        print("Enter Character You Want To Check")
        self.ch = input()

    def Check(self) :
        if self.ch >= 'A' and self.ch <= 'Z' :
            return True 
        else :
            return False

def main() :
    bret = False

    print("Jay Ganesh........")
    obj = Alphabet()
    obj.Accept()
    bret = obj.Check()
    if bret == True :
        print("It is Capital Letter")
    else :
        print("It is Not a Capital Letter")

if __name__ ==  "__main__" :
    main()