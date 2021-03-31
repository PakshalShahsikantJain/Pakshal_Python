def Display(No) :
    i = 1
    Mult = 1
    
    if No < 0 :
        No = -No

    while i <= No :
        Mult = i * 2
        print(Mult,end = " ")
        i = i + 1