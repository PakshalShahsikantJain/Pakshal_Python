def Display(Row,Col,Value) :
    i = 0
    j = 0

    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            if i % 2 == 1:
                print(Value * 2,end = " ")
            else :
                print(Value * 2 - 1,end = " ")
            Value = Value + 1
        Value = 1       
        print("\r")
        