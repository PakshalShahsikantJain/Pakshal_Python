def Display(Row,Col,ch) :
    i = 0
    j = 0

    ch2 = ord(ch)

    for i in range(1,Row + 1) :
        k = chr(ch2)
        for j in range(1,Col + 1) :
            print(k,end = " ")
        ch2 = ch2 + 1
        print("\r")
