def Bill(No) :
    Discount = 0
    FinalAM = 0

    if No <= 500 :
        print("---------Sorry There is No Discount For This Bill Amount-----------")
        return No
    elif No > 500 and No < 1500 :
        print("---------You Get Discount of 10 %--------------")
        Discount = No * 10 / 100
        FinalAM = No - Discount
        return FinalAM
    else :
        print("---------You Get Discount of 15 %--------------")
        Discount = No * 15 / 100
        FinalAM = No - Discount
        return FinalAM
