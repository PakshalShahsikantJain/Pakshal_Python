class School :
    def __init__(self) :
        self.No = 0
    
    def Accept(self) :
        print("Please Enter Your Standard")
        self.No = int(input())

    def Display(self) :
        if self.No == 1 :
            print("Fees For 1st Standard is :",8900) 
        elif self.No == 2 :
            print("Fees For 2nd Standard is :",12790)
        elif self.No == 3 :
            print("Fees For 3rd Standard is :",21000)
        elif self.No == 4 :
            print("Fees For 4th Standard is :",23450)
        else :
            print("Wrong Input.....") 

def main() :
    print("Jay Ganesh.....")
    print("-------------------Welcome To SK School----------------")
    
    obj = School()
    obj.Accept()
    obj.Display()

if __name__ == "__main__" :
    main()