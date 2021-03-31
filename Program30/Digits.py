def Digit(No) :
    Digit = 0
    i = 0
    
    while No != 0:
        Digit = No % 10
        print(Digit)
        if (Digit >= 4) & (Digit <= 4.9) :
            i = i + 1
        No = No / 10

    return i 