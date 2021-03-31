def Display(Row,Col,Value) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            print(Value,end = " ")
            Value = Value + 1
            if Value > 9 :
                Value = 1
        print("\r")
        