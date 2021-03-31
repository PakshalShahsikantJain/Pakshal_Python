def fact(No) :
    i = 1
    Sum = 0

    while i < No :
        if No % i > 0 :
            Sum = Sum + i
        i = i + 1
    
    print(Sum)