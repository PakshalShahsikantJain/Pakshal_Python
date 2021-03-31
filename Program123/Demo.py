class Alphabet :
    def __init__(self) :
        self.ch = " "
    
    def Accept(self) :
        print("Enter Starting Character")
        self.ch = input()
  
    def Check(self) :
        if self.ch >= '!' and self.ch <= '/' :
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
        print("Enter Character is Special Chracter")
    else :
        print("Enter Character is not a special  Character")

if __name__ == "__main__" :
    main()
