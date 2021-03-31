def Display(Row,Col) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            if i % 2 == 1:
                print("",j,end = " ")
            else :
                print(-j,end = " ")

        print("\r")
