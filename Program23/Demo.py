#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Check Whether Entered Number is Greater Than Hundred or Not 
# Date : 30/02/2021 
#
######################################################################################

from Check import * 

def main() :
    print("Jay Ganesh..........")

    print("Enter Number")

    No =  int(input())

    ret = Check(No)
    if ret == True :
        print("Less Than Hundred")
    else :
        print("Greater Than Hundred")

if __name__ == "__main__" :
    main()