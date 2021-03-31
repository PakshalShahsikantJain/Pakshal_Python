def Display(No) :
    i = 0
    if No < 0:
        No = -No
        
    for i in range(No) :
        print("*"," ",end = " ")

    for i in range(No) :
        print("#"," ",end = " ")