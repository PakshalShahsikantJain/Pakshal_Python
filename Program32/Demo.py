#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Count of Even Digits From Entered Number 
# Example : Input = 45362 Output = Frequecy(Count) of Even Digits is : 3  
# Date : 30/02/2021 
#
######################################################################################

from Digit import * 

def main() :
    ret = 0

    print("Jay Ganesh........")
    print("Enter Number")

    No = int(input())

    ret = digit(No) 

    print("Count Even Digits is :",ret)


if __name__ == "__main__":
    main()