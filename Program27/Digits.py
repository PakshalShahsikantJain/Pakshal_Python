def digit(No) :
    Digits = 0
    
    while No != 0 :
        Digits = No % 10 
        print(Digits)
        No = No / 10
