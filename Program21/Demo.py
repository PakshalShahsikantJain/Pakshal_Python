################################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Difference Between Summation of Factors and Non-Factors of A Given Number
# Date : 30/02/2021 
#
#################################################################################################

from Factors import * 

def main() :
    print("Jay Ganesh........")

    print("Enter Number")
    No = int(input())

    ret = fact(No)

    print("Difference is Fact",ret)

if __name__ == "__main__" :
    main()