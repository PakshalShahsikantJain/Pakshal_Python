def Display(No) :
    i = 0

    if No < 0:
        No = -No

    while i <= No :
        if i % 2 == 1 :
            print(i,end = " ")
        i = i + 1