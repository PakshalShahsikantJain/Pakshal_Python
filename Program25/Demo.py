#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Multiplication of Three Entered Number(Zero Should Be Depricated if There) 
# Example : Input = 12 * 0 * 2       Output = 24
# Date : 30/02/2021 
#
######################################################################################

from Multiplication import *

def main() :
    No = 0
    No2 = 0
    No3 = 0

    print("Jay Ganesh......")

    print("Enter First Number")
    No = int(input())

    print("Enter Second Number")
    No2 = int(input())

    print("Enter Third Number")
    No3 = int(input())

    ret = mult(No,No2,No3)

    print("Multiplication is :",ret) 

if __name__  == "__main__" :
    main() 