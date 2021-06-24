#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Difference Between Even and ODD Elements Entered In List 
# Date : 3/03/2021 
#
######################################################################################

class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = []
    
    def Accept(self) :
        print("Enter Elements in LIST")
        for i in range(self.size) :
            print("Enter Element Number",i + 1)
            self.arr.append(int(input()))
    def Display(self) :
        print("Entered Elements are :")
        for i in range(self.size) :
            print(self.arr[i],end = " ")
    
    def Difference(self) :
        i = 0
        Even = 0
        odd = 0

        for i in range(self.size) :
            if self.arr[i] % 2 == 0 :
                Even = Even + self.arr[i]
            else :
                odd = odd + self.arr[i]
        
        return Even - odd
def main() :
    No = 0
    ret = 0

    print("Jay Ganesh....")
    print("Enter How Many Elements You Want in Array")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()

    ret = obj.Difference()
    print("\nDifference is :",ret)

if __name__ == "__main__" :
    main()