#!/usr/bin/env python

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def integer_root(n,k):
    """integer kth root of n"""
    # from https://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots/15979957:
    # Newton's method to find kth root of n
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

def integer_sqrt(n):
    """integer square root"""
    return integer_root(n,2)

def is_prime(n):
    """
        whether an integer is prime
        returns a boolean
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if (n%2) == 0:
        return False
    for i in range(3,integer_sqrt(n)+1,2):
        if (n%i) == 0:
            return False
    return True

def list_primes(n):
    result = []
    i = 1
    while len(result) < n:
        i += 1
        if is_prime(i):
            result.append(i)
    return result

def unpack(x):
    result = ""
    for y in x:
        result += y
    return result

def decode(n):
    primes = list_primes(max(26,integer_sqrt(len(str(n)))+10))
    exponents = []
    for i in range(26):
        exponent = 0
        while n%primes[i] == 0:
            exponent += 1
            n //= primes[i]
        exponents.append(exponent)
    result = [" "]*(integer_sqrt(len(str(n)))+10)
    for i in range(26):
        for j in range(len(result)):
            if (exponents[i]%primes[j] == 0) and (exponents[i] != 0):
                result[j] = alphabet[i]
    while result[-1] == " ":
        result = result[:-1]
    return unpack(result)

ciphertext = open("ciphertext1.txt","r").read().split(" ")
ciphertext = [int(x) for x in ciphertext]
plaintext = ""
for n in ciphertext:
    plaintext += decode(n) + " "
plaintext = plaintext[:-1]
print plaintext
