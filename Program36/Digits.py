def Digit(No) :
    Digits = 0
    Sum1 = 0
    Sum2 = 0
    
    while(No != 0) :
        Digits = No % 10 
        if Digits % 2 == 0:
            Sum1 = Sum1 + Digits
        else :
            Sum2 = Sum2 + Digits
        No = No // 10
    
    return Sum1 - Sum2