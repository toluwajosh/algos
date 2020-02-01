"""n-th number in fibonacci series"""


def rec_fib(n, fibs):
    """Recursive fibonacci function
    
    Arguments:
        n {int} -- nth position of the sequence
        fibs {dictionary} -- dictionary of already calculated positions
    
    Returns:
        int -- final fibonacci number
    """
    if n < 2:
        fibs[n] = n
        return n
    if n - 1 in fibs.keys():
        fib_n1 = fibs[n - 1]
    else:
        fib_n1 = rec_fib(n - 1, fibs)
    if n - 2 in fibs.keys():
        fib_n2 = fibs[n - 2]
    else:
        fib_n2 = rec_fib(n - 2, fibs)
    fibs[n - 1] = fib_n1
    fibs[n - 2] = fib_n2
    return fib_n1 + fib_n2


def iter_fib(n):
    """Iterative fibonacci function
    
    Arguments:
        n {int} -- position of fibonacci number
    
    Returns:
        int -- final output
    """
    if n < 2:
        return n
    pre_last = 0
    last = 1
    for _ in range(n - 1):
        fib = pre_last + last
        pre_last = last
        last = fib
    return fib


def get_fib(n):
    fibs = {}
    return rec_fib(n, fibs), iter_fib(n)


if __name__ == "__main__":
    print(get_fib(112))
