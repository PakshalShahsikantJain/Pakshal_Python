from Check import *

def main() :
    No = 0
    No2 = 0
    print("Ganapati Bappa Morya")

    print("Enter First Number")
    No = int(input())

    print("Enter Second Number")
    No2 = int(input())

    ret = check(No,No2)

    if ret == True :
        print("Number's Are Equal")
    else :
        print("Number's Are Different")

if __name__ == "__main__" :
    main()