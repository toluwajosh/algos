"""print_factors
Write a program that takes an integer and prints out all ways to multiply smaller integers that equal the original number,
without repeating sets of factors.
In other words, if your output contains 4 * 3, you should not print out 3 * 4 again as that would be a repeating set.
Note that this is not asking for prime factorization only. 
Also, you can assume that the input integers are reasonable in size; correctness is more important than efficiency.
PrintFactors(12) 12 * 1 6 * 2 4 * 3 3 * 2 * 2
"""


def print_factors(number):
    factors = {}
    for i in range(1, number + 1):
        if number % i == 0 and i not in factors:
            print(i, number // i)
            factors[number // i] = number // i


def print_factors_while(number):
    factors = {1: number}
    print(1, number)
    current = 1
    last_factor = number
    while current < last_factor:
        if number % current == 0 and current not in factors:
            last_factor = number // current
            print(current, last_factor)
            factors[last_factor] = last_factor
        current += 1


if __name__ == "__main__":
    # print_factors(169999999999)
    print_factors_while(169999999999)
