def fact(No) :
    i = 1
    sum = 0
    sum2 = 0

    diff = 0

    while i < No :
        if No % i == 0 :
            sum = sum + i
        
        else :
            sum2 = sum2 + i

        i = i + 1

    diff = sum - sum2

    return diff