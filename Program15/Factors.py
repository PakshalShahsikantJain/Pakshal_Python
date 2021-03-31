def fact(No) :
    i = 1

    while(i < No) :
        if (No % i == 0) & (i % 2 == 0):
            print(i,"\t",end = "")
        i = i + 1