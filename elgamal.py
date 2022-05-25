# Python program to illustrate ElGamal encryption

import random
from math import pow

a = random.randint(2, 10)
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# Generating large random numbers
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c


# Asymmetric encryption
def encrypt(msg, q, h, g):
    en_msg = []

    k = gen_key(q)  # Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg


# Driver code
def main(msg):
    message_recieved = dict.fromkeys(range(1, 7))  # print the message first
    message_recieved[1] = (gen_key(q))  # Private key for sender
    key = gen_key(q)
    message_recieved[2] = (power(g, key, q))  # Public key of sender

    # Private key for receiver
    h = power(g, key, q)

    # Encryption key gen
    message_recieved[3] = g

    # Private key
    message_recieved[4] = h

    en_msg, p = encrypt(msg, q, h, g)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)

    # Encrypted message
    message_recieved[5] = en_msg

    # Decrypted message
    message_recieved[6] = dmsg
    return message_recieved
