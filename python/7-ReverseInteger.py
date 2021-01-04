'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


def reverse(self, x: int) -> int:
    if x > 0:
        a = int(str(x)[::-1])
    else:
        a = int(str(x * (-1))[::-1]) * (-1)
    mina = -2 ** 31
    maxa = 2**31
    if a not in range(mina, maxa):
        return 0
    else:
        return a
