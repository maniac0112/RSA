import prime_generator
import multiplicative_inverse
import math

def key_generator(B):
    #B denotes roughly the size of n (in bits)
    p=prime_generator.generate_prime(B//2)
    q=prime_generator.generate_prime(B//2)
    while(p==q):
        q=prime_generator.generate_prime(B//2)
    #now the totient function of n = pq is simply (p-1)*(q-1)
    n=p*q
    phi_n=(p-1)*(q-1)
    #now we need to generate the public exponent e
    #it should be coprime with phi_n
    start=10
    e=2**start+1
    while(1):     
        if math.gcd(e,p-1)==1 and math.gcd(e,q-1)==1:
            break
        start+=1
        e=2**start+1
    #now we have public key (e,n)
    d=multiplicative_inverse.multiplicative_inverse(e, phi_n)
    private_key=[d,n]
    public_key=[e,n]
    if (len(bin(p*q))-2)!=B:
        return key_generator(B)
    return ((public_key,private_key))
    
    

