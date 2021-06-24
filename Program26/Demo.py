#############################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Remove Percentage of Entered Total Marks(Percentage Can Be in Decimal) 
# Date : 30/02/2021 
#
##############################################################################################

from Division import *

def main() :
    print("Jay Ganesh.......")

    print("Total Marks")

    No = float(input())

    print("Total Marks Obtained")

    No2 = float(input())

    ret = div(No,No2)

    print("Percentage is :",ret,"%")

if __name__ == "__main__" :
    main()
