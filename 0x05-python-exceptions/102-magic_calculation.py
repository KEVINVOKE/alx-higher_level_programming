#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            else:
                res += (a ** b) / i
        except:
            res = b + a
            break
    return (result)
