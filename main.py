import key_generator
import rsa
import cv2
import numpy as np 
import os
import matplotlib
import sys


def convert(s):
    arr=s.flatten()
    output=""
    for i in range(arr.shape[0]):
        t="0"*(8-len(bin(arr[i]))+2)+bin(arr[i])[2:]
        output+=t
    return output
        
def retrieve(arr,shape):
    output=[]
    for i in range(shape[0]):
        output.append([])
        for j in range(0,shape[1]):
            rgb=arr[(i)*shape[1]*24+j*24:(i)*shape[1]*24+j*24+24]
            r=int(rgb[0:8],2)
            g=int(rgb[8:16],2)
            b=int(rgb[16:24],2)
            z=[r,g,b]
            output[i].append(z)
    op=np.array(output)
    return op

def main(image):

    print("Please Wait...")
    print("It may take some time")

    s=cv2.imread(image)
    shape=s.shape
    x=convert(s)
    t=len(x)
    
    key=key_generator.key_generator(256)
    while(len(x)%128!=0):
        x+="0"
    ciphertext=rsa.RSA_encrypt(x, key[0])

    #simply writing ciphertext in a txt file    
    f=open("ciphertext.txt","w")
    f.write(ciphertext)
    f.close()

    decrypted=rsa.RSA_decrypt(ciphertext,key[1])
    decrypted=decrypted[:t]
    z=retrieve(decrypted, shape)
    cv2.imwrite('decrypted.jpg',z)  

main("sample.jpg")
