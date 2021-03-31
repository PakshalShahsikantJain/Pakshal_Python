def fact(No) :
    i = 0 
    
    if No < 0 :
        No = -No
    i = No 
    Mult = 1

    while i > 0 :
        Mult = Mult * i
        i = i - 1
    
    return Mult