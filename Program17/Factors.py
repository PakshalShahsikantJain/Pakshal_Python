def factMult(No) :
    i = 1
    Mult = 1

    while i < No :
        if No % i == 0 :
            Mult = Mult * i
        
        i = i + 1

    print(Mult)
