from SFtoSM import *

def main() :
    ret = 0
    print("Jay Ganesh........")

    print("Enter Square Feet")

    No = int(input())

    ret = SFtoSM(No)

    print("SF Converted To SM is :",ret)


if __name__ == "__main__" :
    main()