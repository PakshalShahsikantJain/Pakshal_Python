def check(No) :
    if No < 0 :
        No = -No

    if No < 50 :
        print("Small")
    elif (No > 50) & (No < 100) :
        print("Medium")
    else :
        print("Large") 