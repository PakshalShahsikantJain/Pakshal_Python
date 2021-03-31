def display(No,No2) :
    i = 0
    sum = 0

    i = No
    if No < 0 :
        print("Invalid Range")
        return 
    if No > No2 :
        print("Invalid Range")
        return
        
    while i <= No2 :
        if i % 2 == 0 :
            sum = sum + i    
        i = i + 1

    return sum