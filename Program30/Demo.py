#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Count of 4 From Entered Number 
# Example : Input = 40262 Output = Frequecy(Count) of 4 is : 1  
# Date : 30/02/2021 
#
######################################################################################

from Digits import *

def  main() :
    print("Jay Ganesh.......")

    print("Enter Number")
    No = int(input())

    ret = Digit(No)

    print("Frequency of Four is :",ret)

if __name__ == "__main__" :
    main()