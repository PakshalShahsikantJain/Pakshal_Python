#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Count of Digits Between Entered Range From Entered Number 
# Example : Input = 40262 Output = Frequecy(Count) of Digits Between Entered Range is : 2  
# Date : 30/02/2021 
#
######################################################################################

from Digits import *

def main() :
    ret = 0

    print("Jay Ganesh....")

    print("Enter Number")
    No = int(input())

    ret = Digit(No)

    print("Count of Digits Between 3 and 7 is :",ret)

if __name__ == "__main__" :
    main()