from Check import * 

def main() :
    print("Jay Ganesh..........")

    print("Enter Number")

    No =  int(input())

    ret = Check(No)
    if ret == True :
        print("Less Than Hundred")
    else :
        print("Greater Than Hundred")

if __name__ == "__main__" :
    main()