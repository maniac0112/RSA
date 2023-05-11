def multiplicative_inverse(x,n):
    if n==1:
        return 0
    else:
        a=n
        b=0
        c=1
        while (x>1):
            # we use extended division alorithm in reverse to find bezout's coefficient
            quotient=x // n
            temp=n
            n=x % n
            x=temp
            temp=b
            b=c-quotient*b
            c=temp
        if (c<0):
            c=c+a
        return c