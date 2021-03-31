from Hotel import *

def main() :
    No = 0
    ret = 0

    print("Jay Ganesh.........")
    print("----------------Welcome To Hotel SK-------------------")
    print("Please Enter Your Total Bill Amount")
    No = int(input())

    ret = Bill(No)
    print("Your Final Bill Amount is :",ret)

    print("----------------Thank You Visit Again!!!!!-------------")

if __name__ == "__main__" :
    main()