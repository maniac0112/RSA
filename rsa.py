#encrypt the data using public key
#decrypt it back using private key!


def RSA_encrypt(message,public_key):
    #message is a sequence of integers!
    #assume that message is a multiple of ||n||//2
    n=public_key[1]
    block_size=(len(bin(public_key[1]))-2)//2
    cipher_block=(len(bin(public_key[1]))-2)
    start=0
    ciphertext=""
    while(start<len(message)):
        m=message[start:start+block_size]
        x=int(m,2)
        c=pow(x,public_key[0],n)
        cipher=(cipher_block-len(bin(c)[2:]))*"0"+ bin(c)[2:] #this ensures that cipher is of n length
        ciphertext+=cipher
        start+=block_size
    return ciphertext

def RSA_decrypt(ciphertext,private_key):
    block_size=len(bin(private_key[1]))-2
    start=0
    message=""
    while(start<len(ciphertext)):
        cipher=ciphertext[start:start+block_size]
        x=int(cipher,2)
        m=pow(x,private_key[0],private_key[1])
        str_m=(block_size//2-len(bin(m)[2:]))*"0"+ bin(m)[2:]
        message+=str_m
        start+=block_size
    return message