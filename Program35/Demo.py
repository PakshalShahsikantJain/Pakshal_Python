#########################################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Multiplication of Digits of Entered Number(Deprecate 0 if there in Number)
# Example : Input = 40262 Output = Multiplication is : 96  
# Date : 30/02/2021 
#
##########################################################################################################

from Digits import *

def main() :
    ret = 0

    print("Jay Ganesh....")

    print("Enter Number")
    No = int(input())

    ret = Digit(No)

    print("Multiplication of Digits is:",ret)

if __name__ == "__main__" :
    main()