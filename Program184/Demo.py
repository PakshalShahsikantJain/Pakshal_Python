def ReverseWord(str,arr) :
    i = 0
    j = 0
    brr = []
    crr = []
    for i in range(len(arr)) :
        #print(i,end = " ")
        brr = list(arr[i]) 
       # print(len(brr))
        j = len(brr) - 1
        while j != -1 :
            print(brr[j],end = " ") 
            j = j - 1
        print(" ",end = " ")

def main() :
    arr = []
    print("Jay Ganesh......")
    print("Enter One String")
    str = input()

    arr = str.split()
    print(arr)

    ReverseWord(str,arr)
if __name__ == "__main__" :
    main()