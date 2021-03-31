def StringToggle(arr) :
    i = 0

    brr = []

    for i in range(len(arr)) :
        brr = list(arr[i])
        j = 0
        while j != len(brr) :
            if j == 0 :
                if brr[j] >= 'a' and brr[j] <= 'z' :
                    k = ord(brr[j])
                    k = k - 32
                    print(chr(k),end = " ")
                else :
                    print(brr[j],end = " ")
            else :
                print(brr[j],end = " ")
            j = j + 1
        print(" ",end = " ")
def main() :
    print("Jay Ganesh......")
    arr = []
    
    print("Enter One String")
    str = input()
    arr = str.split()
    print(arr)

    StringToggle(arr)

if __name__ == "__main__" :
    main()