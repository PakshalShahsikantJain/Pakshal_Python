def Display(Row,Col,ch,Value) :
    i = 0
    j = 0

    ch2 = ord(ch)
    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            k = chr(ch2)
            if i % 2 == 1 :
                print(k,end = " ")
                ch2 = ch2 + 1
            else :
                print(Value,end = " ")
                Value = Value + 1
        ch2 = ord(ch)
        Value = 1
        print("\r")
