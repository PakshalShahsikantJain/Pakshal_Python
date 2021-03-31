class Binary :
    def __init__(self,i,j) :
        self.No = i
        self.Position = j
        self.Res = 0

    def Check(self) :
        iMask = 0X00000001

        if self.Position < 1 or self.Position > 32 :
            return False
        
        iMask = iMask << self.Position
        self.Res = self.No & iMask

        if self.Res == iMask :
            return True
        else :
            return False

def main() :
    print("Jay Ganesh........")
    No = 0
    pos = 0
    bret = False

    print("Enter one Number")
    No = int(input())

    print("Enter Postion You Want To Check")
    pos = int(input())
    
    obj1 = Binary(No,pos)
    bret = obj1.Check()

    if bret == True :
        print("Bit is On")
    else :
        print("Bit is OFF")

    print("Enter one Number")
    No2 = int(input())

    print("Enter Postion You Want To Check")
    pos2 = int(input())
    
    obj2 = Binary(No,pos)
    bret = obj2.Check()

    if bret == True :
        print("Bit is On")
    else :
        print("Bit is OFF")

if __name__ == "__main__" :
    main()