def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    l = len(aStr)
    if l==0 and char=='':
        return True
    elif l==0 and char!='':
        return False
    if l%2 ==   0:
        n=l//2
    else:
        n=(l-1)//2

    if char==aStr[n]:
        return True
    while n>0:
        if char < aStr[n]:
            
            return isIn(char,aStr[0:n])
        elif char > aStr[n]:
            return isIn(char,aStr[n:])
    else:
        return False
    
