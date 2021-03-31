def String(str,arr) :
    i = 0
    brr = [] 
    for i in range(len(str)) :
        #print(arr[i],end = " ")
        if arr[i] == ' ' :
            arr[i] = arr[i-1]
        else :
            brr.append(arr[i])

    print(brr)
def main() :
    print("Jay Ganesh.......")
    print("Enter One String")
    str = input()
    arr = list(str)

    print(arr)

    String(str,arr)
if __name__ == "__main__" :
    main()