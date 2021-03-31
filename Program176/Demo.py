def LargeWord(str,arr) :
    i = 0
    iMax = 0

    for i in range(len(arr)) :
        if len(arr[i]) > iMax :
            iMax = len(arr[i])
    
    return iMax
def main() :
    arr = [] 
    print("Jay Ganesh......")
    print("Enter One String") 
    str = input()

    arr = str.split()
    print(arr)

    ret = LargeWord(str,arr)
    print("Length of Largest Word is :",ret)

if __name__ == "__main__" :
    main()