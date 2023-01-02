#!/usr/bin/env python3

import random
import string

dig = [i for i in "0123456789"]
lit = [i for i in "abcdefghijklmnopqrstuvwxyz"]
big = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def generate_password(length):
    text = ''
    for l in range(length):
        text += str(random.sample(big, 1)[0]) + str(random.sample(lit, 1)[0]) + str(random.sample(dig, 1)[0])
    text = [i[0] for i in text][:length]

    random.shuffle(text)
    return ''.join(text)

def generate_passwords(count, digits):
    for i in range(count):
        print(generate_password(digits))

n, m = int(input()), int(input())

generate_passwords(n,m)
