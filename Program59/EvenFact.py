def Fact(No) :
    i = 0
    
    Mult = 1

    if No < 0 :
        No = -No
    
    i = No

    while i > 0 :
        if i % 2 == 0 :
            Mult = Mult * i
        i = i - 1
    
    return Mult