def Digit(No) :
    Cnt = 0
    Digit = 0

    while No != 0 :
        Digit = No % 10
        if Digit % 2 == 1 :
            Cnt = Cnt + 1
        No = No // 10
    
    return Cnt

