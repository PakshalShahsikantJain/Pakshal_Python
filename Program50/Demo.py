from FtoC import *

def main() :
    ret = 0
    print("Jay Ganesh........")

    print("Enter Temperature in Fahrenheit")
    No = int(input())

    ret = FtoC(No)

    print("Temparature Converted From Fahrenheit To Celcius is :",ret)


if __name__ == "__main__" :
    main()