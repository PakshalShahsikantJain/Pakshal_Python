class Digit :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Number To Check Wheter It One Digit Number or Not")
        self.ch = input()
    
    def Check(self) :
        if self.ch >= '0' and self.ch <= '9' :
            return True 
        else :
            return False

def main() :
    bret = False
    print("Jay Ganesh........")
    obj = Digit()
    obj.Accept()
    bret = obj.Check()
    if bret == True :
        print("Character is Digit")
    else :
        print("Character is Not A Digit")

if  __name__ == "__main__" :
    main()