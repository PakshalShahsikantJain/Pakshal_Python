def Digit(No) :
    Digits = 0
    Mult = 1
    
    while(No != 0) :
        Digits = No % 10 
        Mult = Mult * Digits
        No = No // 10
    
    return Mult