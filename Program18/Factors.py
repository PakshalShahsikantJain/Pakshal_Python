def fact(No) :
    i = No - 1

    while(i > 0) :
        if No % i == 0 :
            print(i,"\t",end = " ")
        i = i - 1