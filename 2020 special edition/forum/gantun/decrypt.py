#!/usr/bin/env python

# based on Gantun from https://susec.tf/tasks/gantun_229621efd1dcc01ef8851254affd1326887ec58e.txz

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def integer_root(n):
    # Newton's method to find square root of n
    u, s = n, n+1
    while u < s:
        s = u
        t = s + n // s
        u = t // 2
    return s

def decrypt(c):
    numbers = [c]
    while max(numbers) >= 52:
        z = max(numbers)
        n = numbers.index(z)
        x = integer_root(z)
        y = z - x*x
        if y > x:
            y -= x
        else:
            x,y = y,x
        numbers = numbers[:n] + [x,y] + numbers[n+1:]
    p = ""
    for x in numbers:
        p += alphabet[x-26]
    return p

c = int(open("ciphertext.txt","r").read())
print decrypt(c)
