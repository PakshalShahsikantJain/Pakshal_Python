def display(No,No2) :
    i = 0

    i = No
    if No > No2 :
        print("Invalid Range")
        
    while i <= No2 :
        if i % 2 == 0 :
            print(i,end = " ")
        i = i + 1