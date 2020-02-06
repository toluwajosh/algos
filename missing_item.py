"""Find missing items"""


def reverse_string(s):
    if s == "":
        return ""
    elif len(s) == 1:
        return s
    elif len(s) == 2:
        return s[1] + s[0]
    return s[-1] + reverse_string(s[:-1])


"""write a function that takes two arguments (list, list)
and returns a missing element in one of the arguments.
Example:
    [4, 12, 9, 5, 6]
    [4, 9, 12, 6]
    => 5
"""


def find_missing_with_set(full_set, partial_set):
    missing_items = set(full_set) - set(partial_set)
    return list(missing_items)


def find_missing_with_xor(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num
    return xor_sum


def find_missing_with_hash(full_set, partial_set):
    partial_set_dict = {x: x for x in partial_set}
    for ele in full_set:
        if ele not in partial_set_dict:
            return ele
    return False


if __name__ == "__main__":
    # print(reverse_string("ab"))
    # print(find_missing_with_set([4, 12, 9, 5, 6], [4, 9, 12, 6])[0])
    # print(find_missing_with_xor([4, 12, 9, 5, 6], [4, 9, 12, 6]))
    print(find_missing_with_hash([4, 12, 9, 5, 6], [4, 9, 12, 6]))

    # using set on non numeric elements
    # thisset = {"apple", "banana", "cherry", "apple", "banana", "cherry"}
    # thatset = set(("apple", "banana", "cherry", "apple", "banana", "cherry", "toy"))
    # print(thisset)
    # print(thatset)
    # print(thisset == thatset)
    # print(list(thatset - thisset))
