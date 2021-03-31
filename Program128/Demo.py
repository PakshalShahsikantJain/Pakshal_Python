class LIST :
    def __init__(self) :
        self.str = " "
        self.arr = []
    
    def Accept(self) :
        print("Enter String")
        self.str = input()
        self.arr = list(self.str)
    
    def Display(self) :
        print(self.arr)

    def Check(self) :
        i = 0

        for i in range(len(self.str)) :
            if self.arr[i] == 'a' or self.arr[i] == 'e' or self.arr[i] == 'i' or self.arr[i] == 'o' or self.arr[i] == 'u' or self.arr[i] == 'A' or self.arr[i] == 'E' or self.arr[i] == 'I' or self.arr[i] == 'O' or self.arr[i] == 'U' :
                break
        
        if self.arr[i] == 'a' or self.arr[i] == 'e' or self.arr[i] == 'i' or self.arr[i] == 'o' or self.arr[i] == 'u' or self.arr[i] == 'A' or self.arr[i] == 'E' or self.arr[i] == 'I' or self.arr[i] == 'O' or self.arr[i] == 'U' :
            return True
        else :
            return False

def main() :
    bret = False 

    print("Jay Ganesh......")
    obj = LIST()
    obj.Accept()
    obj.Display()
    bret = obj.Check()

    if bret == True :
        print("String Contains Vowels")
    else :
        print("String Does Not Contains Vowels")

if __name__ == "__main__" :
    main()