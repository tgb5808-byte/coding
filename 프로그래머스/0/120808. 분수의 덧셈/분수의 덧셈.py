def solution(numer1, denom1, numer2, denom2):

    import math  
    a=denom1*denom2
    b=denom1*numer2+denom2*numer1
    n=math.gcd(a,b) 
            
    return (b//n,a//n)