def Display(Row,Col,ch) :
    i = 0
    j = 0

    ch2 = ord(ch)
    for i in range(1,Row + 1) :
        for j in range(1,Col+1):
            if i % 2 == 1 :
                l = chr(ch2)       
                print(l,end = " ")
            else :
                l = chr(ch2 + 32)
                print(l,end = " ")
            ch2 = ch2 + 1
        ch2 = ord(ch)
        print("\r")