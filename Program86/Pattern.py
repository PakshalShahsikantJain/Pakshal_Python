def Display(Row,Col) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Row + 1) :
            if i > j :
                print(" "," ",end = " ")
            else :
                print(j," ",end = " ")
        print("\r")