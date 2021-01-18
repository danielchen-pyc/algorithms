'''
Given two integers dividend and divisor, divide two integers without using multiplication,
division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional
part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that
your function returns 231 − 1 when the division result overflows.
'''


# This question is honestly kinda lame tho LOL
# Other Solution (Runtime 91.02%)
def divide(self, dividend: int, divisor: int) -> int:
    if (dividend == -2147483648 and divisor == -1): return 2147483647
    a, b, res = abs(dividend), abs(divisor), 0
    for x in range(32)[::-1]:
        if (a >> x) - b >= 0:
            res += 1 << x
            a -= b << x
    return res if (dividend > 0) == (divisor > 0) else -res
