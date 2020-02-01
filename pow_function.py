"""pow function
"""

def pow_func(number, pow):
    powered = number
    for i in range(pow-1):
        powered *=number
    return powered

if __name__ == "__main__":
    print(10**4)
    print(pow_func(10, 4))