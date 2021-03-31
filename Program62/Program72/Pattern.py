def Display(Row,Col,ch) :
    i = 0

    k = ord(ch)
    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            l = chr(k)
            print(l,end = " ")
            k = k + 1
        k = ord(ch)
        print("\r")
