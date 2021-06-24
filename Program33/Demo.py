#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Count of Odd Digits From Entered Number 
# Example : Input = 45326 Output = Frequecy(Count) of Odd Digits is : 2  
# Date : 30/02/2021 
#
######################################################################################

from Digits import *

def main() :
    ret  = 0

    print("Jay Ganesh.......")

    print("Enter Number")
    No = int(input())

    ret = Digit(No)

    print("COunt OF ODD Digits is :",ret)

if __name__ == "__main__" :
    main()