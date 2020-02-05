"""pow
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]


1.00000
2147483647 -> 1.0


0.00001
2147483647 -> 0.0
"""


def myPow(x, n):
    if n > 0:
        prod = x
        for i in range(1, n):
            prod *= x
    else:
        prod = (1 / x)
        for i in range(1, abs(n)):
            prod *= (1 / x)
    return prod


if __name__ == "__main__":
    print(myPow(2.0, 10))
    print(myPow(2.1, 4))
    print(myPow(2.0, -2))
