#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Count of Digits Less Than From Entered Number 
# Example : Input = 40262 Output = Frequecy(Count) of Digits Less Than 6 is : 4  
# Date : 30/02/2021 
#
######################################################################################

from Digits import *

def  main() :
    print("Jay Ganesh.......")

    print("Enter Number")
    No = int(input())

    ret = Digit(No)

    print("Frequency of Digits Less Than 6 is :",ret)

if __name__ == "__main__" :
    main()