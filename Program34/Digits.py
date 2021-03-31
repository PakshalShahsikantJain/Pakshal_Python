def Digit(No) :
    Digits = 0
    Cnt = 0
    
    while(No != 0) :
        Digits = No % 10 
        if (Digits > 3) & (Digits < 7) :
            Cnt = Cnt + 1
        No = No // 10
    
    return Cnt