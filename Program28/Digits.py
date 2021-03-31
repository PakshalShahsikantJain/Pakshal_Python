def digit(No) :
    while No != 0 :
        Digit = No % 10
        print(Digit)
        if (Digit >= 0) & (Digit <= 0.9) :
            break
        No = No / 10

    if Digit == 0:
        return True
    else :
        return False