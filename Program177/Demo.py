def Pattern(str,arr) :
    i = 0
    j = 0

    for i in range(len(str)) :
        for j in range(len(str)) :
            print(arr[j],end = " ")
        print("\r")
def main() :
    arr = [] 
    print("Jay Ganesh.........")
    print("Enter One String")
    str = input()
    arr = list(str)
    print(arr)

    Pattern(str,arr)
    
if __name__ == "__main__" :
    main()