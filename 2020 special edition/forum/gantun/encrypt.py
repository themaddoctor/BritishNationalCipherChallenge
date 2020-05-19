#!/usr/bin/env python

# based on Gantun from https://susec.tf/tasks/gantun_229621efd1dcc01ef8851254affd1326887ec58e.txz

#from random import randint
randint = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(p):
    global randint
    numbers = []
    for char in p.upper():
        numbers.append(alphabet.index(char)+26)
    while len(numbers) > 1:
        n = randint[0]; randint = randint[1:] # randint(0,len(numbers)-2)
        x = numbers[n]
        y = numbers[n+1]
        if x > y:
            z = x*x + x + y
        else:
            z = y*y + x
        numbers = numbers[:n] + [z] + numbers[n+2:]
    return numbers[0]

p = open("plaintext.txt","r").read().upper().replace(" ","").replace("\n","").replace("\r","")

# the random choices made in encryption have been stored in random.txt, so that you can reproduce the ciphertext
random = open("random.txt","r").read().replace("\n","").replace("\r","").split(",")
randint = [int(x) for x in random]

print encrypt(p)
