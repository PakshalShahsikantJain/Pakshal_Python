from Area import *

def main() :
    PI  = 0.0

    print("Jay Ganesh.......")

    print("Enter Radius")
    
    No = float(input())

    print("Enter Value of PI")

    PI = float(input())

    ret = Area(No,PI) 

    print("Radius of Circle is :",ret)

if __name__ == "__main__" :
    main()