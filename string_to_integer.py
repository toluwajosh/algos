"""string to integer
"""


def myAtoi(str):
    if str == "":
        return 0
    prefixes = {a: a for a in "+-"}
    numbers = {a: a for a in "0123456789"}
    # non-numerical in the beginning
    if str[0] not in prefixes and str[0] not in numbers and str[0] != " ":
        return 0
    # normal string
    int_string = ""
    seen_number = False
    seen_sign = False
    for s in str:
        if seen_number and s not in numbers:
            break
        if not seen_number and s not in numbers and s not in prefixes and s != " ":
            break
        if seen_sign and s not in numbers:
            break
        if s in prefixes or s in numbers:
            if s in numbers:
                seen_number = True
            if s in prefixes:
                seen_sign = True
            int_string += s
    if int_string == "" or int_string in prefixes:
        return 0
    int_string = int(int_string)

    if int_string >= 2 ** 31 - 1:
        return 2 ** 31 - 1
    if int_string <= -(2 ** 31):
        return -(2 ** 31)
    return int_string


if __name__ == "__main__":
    print(myAtoi("   e3-14159"))
