#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Difference Between Max and Min Number Enterend in List 
# Date : 30/02/2021 
#
######################################################################################

class LIST :
    def __init__(self,no = 10) :
        self.size = no
        self.arr = []
    
    def Accept(self) :
        print("Enter Elements in LIST") 
        for i in range(self.size) :
            print("Enter Element Number :",i + 1)
            self.arr.append(int(input()))
    
    def Display(self) :
        print("Entered Data Is :",self.arr)
    
    def Difference(self) :
        i = 0
        Max = 0
        Min = 0

        Min = self.arr[i]
        for i in range(self.size) :
            if self.arr[i] > Max :
                Max = self.arr[i]
            elif self.arr[i] < Min :
                Min = self.arr[i]
        
        return Max - Min
def main() :
    No = 0
    ret = 0
    print("Jay Ganesh.........")
    print("Enter How Many Elements You Want in LIST")
    No = int(input())

    obj = LIST(No)
    obj.Accept()
    obj.Display()
    ret = obj.Difference()
    print("Difference is :",ret)
    
if __name__ == "__main__" :
    main()
