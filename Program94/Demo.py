#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Total Charge of Vechicle Driven BY Customer
#
######################################################################################

class Tourist_Company :
    def __init__(self) :
        self.KM = 0
        self.Charge = 0

    def Accept(self) :
        print("Enter Running(Total KM) of Car")
        self.KM = int(input())
    
    def Display(self) :
        if self.KM <= 100 :
            self.Charge = self.KM * 25
        else :
            self.Charge = self.KM * 15
        return self.Charge

def main() :
    ret = 0

    print("Jay Ganesh....")
    obj = Tourist_Company()
    obj.Accept()

    ret = obj.Display()
    print("Charge is :",ret)

if __name__ == "__main__" :
    main()