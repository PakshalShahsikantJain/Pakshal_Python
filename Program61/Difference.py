def Diff(Value) :
    i = 0
    Even = 1
    ODD = 1

    if Value < 0:
        Value = -Value

    i = Value

    while i > 0 :
        if i % 2 == 0 :
            Even = Even * i
        else :
            ODD = ODD * i
        i = i - 1
    
    return Even - ODD