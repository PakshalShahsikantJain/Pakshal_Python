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