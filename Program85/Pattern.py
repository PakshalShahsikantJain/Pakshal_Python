def Display(Row,Col) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Row + 1) :
            if i == j :
                print("*"," ",end = " ")
            elif i == 1 or j == 1 :
                print("*"," ",end = " ")
            elif i == Row or j == Col :
                print("*"," ",end = " ")
            else :
                print(" "," ",end = " ")
        print("\r")