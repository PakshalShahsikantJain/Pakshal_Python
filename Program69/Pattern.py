def Display(Row,Col) :
    i = 0
    j = 0
    
    if Row < 0 or Col < 0 :
        Row = -Row
        Col = -Col
    print("Output :")
    for i in range(1,Row + 1) :
        for j in range(Col,0,-1):
            print(j," ",end = " ")
        print("\r")