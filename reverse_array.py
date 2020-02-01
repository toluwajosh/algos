"""Array reverse techniques
"""


def python_reverse(array):
    return reversed(array)


def slicing_reverse(array):
    return array[::-1]


def loop_reverse(array):
    assert isinstance(array, str)
    index = len(array)
    reversed_array = ""
    while index > 0:
        reversed_array += array[index - 1]
        index -= 1
    return reversed_array


def reverse_int(self, x: int) -> int:
        x_reversed = str(x)[::-1]
        if x < 0:
            x_reversed = -1 * int(x_reversed[:-1])
        else:
            x_reversed = int(x_reversed)
        if x_reversed <= 2**31-1 and x_reversed >= -2**31:
            return x_reversed
        return 0

if __name__ == "__main__":
    # print("".join(python_reverse("abc")))
    # print(slicing_reverse("abc"))
    print(int(loop_reverse(str(1234))))
