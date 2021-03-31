from Area import *

def main() :
    No = 0.0
    No2 = 0.0
    ret = 0

    print("Jay Ganesh........")
    print("Enter Width of Rectangle")
    No = float(input())

    print("Enter Height of Rectangle")
    No2 = float(input())

    ret = Area(No,No2)
    
    print("Area of Recatngle is :",ret)

if __name__ == "__main__" :
    main()