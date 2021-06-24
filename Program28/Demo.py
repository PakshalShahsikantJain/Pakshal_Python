#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Check Whether Enterd Number Contains Zero or Not in it 
# Example : Input : 4026 Output : True 
# Date : 30/02/2021 
#
######################################################################################

from Digits import * 

def main() :
    print("Jay Ganesh.......")

    print("Enter Number")
    No = int(input())

    ret = digit(No)

    if ret == True :
        print("Number Contains Zero")
    else :
        print("Number Does Not Contains Zero")

if __name__ == "__main__" :
    main()