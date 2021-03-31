def Digit(No) :
    Digit = 0
    i = 0
    
    while No != 0:
        Digit = No % 10
        if Digit < 6 :
            i = i + 1
        No = No // 10

    return i 