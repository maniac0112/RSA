"""
This file provides a brief description of all the basic-blocks in this directory

main.py => It is made for demostrating the entire working of this RSA algorithm. 

First, it converts an image into a binary sequence. This binary sequence is then encrypted using RSA to generate
ciphertext.txt. Later this ciphertext is converted back into image (decrypted.jpg)

The key generator generates the public/private key as well as the number n=p*q.

In order to generate large p and q, we use prime_generator.py which involves a probabilistic prime number generation 
using miller rabin test.

The RSA_encrypt in rsa.py file divided the message into blocks and encrypted each of the block sequentially 
using public key. 

The RSA_decrypt in rsa.py converts the ciphertext back to the orignal message
"""