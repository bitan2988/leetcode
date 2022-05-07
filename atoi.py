
# https://leetcode.com/problems/string-to-integer-atoi/


def solution(s):
    INT_MAX = pow(2,31)-1
    INT_MIN = pow(2,31)

    i = 0
    sign = 1
    while s[i]==' ' and i<len(s):
        i +=1
    
    if s[i]=='-':
        sign  = -1
        i+=1
    elif s[i]=='+':
        sign = 1
        i+=1

    nums = []
    res = 0

    while( i<len(s) and s[i].isdigit()):
        digit = int(s[i])
    
        if ((res > INT_MAX // 10) or (res == INT_MAX // 10 and digit > INT_MAX % 10)):  
            return INT_MAX if sign == 1 else INT_MIN
        
        res = res*10 + digit
        i+=1
        
    return sign*res

        



    