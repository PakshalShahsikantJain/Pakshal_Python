def Display(Row,Col) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            if i == j or i == 1 or j == 1 or i == Row or j == Col :
                print(j," ",end = " ")
            else :
                print(" "," ",end = " ")
        print("\r")