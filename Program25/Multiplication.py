def mult(No,No2,No3) :
    ans = 0

    if No == 0 :
        ans = No2 * No3
    elif No2 == 0:
        ans = No * No3
    elif No3 == 0:
        ans = No * No2
    else :
        ans = No * No2 *No3

    return ans
