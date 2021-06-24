#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Summation of Numbers Between Entered Range 
# Date : 30/02/2021 
#
######################################################################################

from Display import *

def main() :
    ret = 0
    print("Jay Ganesh.......")

    print("Enter First Number")
    No = int(input())

    print("Enter Second Number")
    No2 = int(input()) 

    ret = display(No,No2)

    print("Addition of numbers Between That RAnge is :",ret)

if __name__ == "__main__" :
    main()