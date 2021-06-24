#####################################################################################
#
# Author : Pakshal Shahsikant Jain
# Problem_Statement : Display Factorial of Entered Number 
# Date : 30/02/2021 
#
######################################################################################

from Fact import * 

def main() :
    ret = 0
    print("Jay Ganesh.........")

    print("Enter Number")
    No = int(input())

    ret = fact(No) 
    print("Factorial of Number :",ret)



if __name__ == "__main__" :
    main()