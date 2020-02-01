"""Given a mapping such that a->1, b->2 ... z->26,
Find how many ways to decode a message given in digits.
Assume that the data only has digits 0-9
"""
import string

alphas = string.ascii_lowercase
a_nums = list(range(1, 27))

mapping = {}
for i in range(26):
    mapping[a_nums[i]] = alphas[i]
print(mapping)


def num_ways(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == "0":
        return 0
    if memo[k] != None:
        return memo[k]
    result = num_ways(data, k - 1, memo)
    if k >= 2 and int(data[s : s + 2]) <= 26:
        result += num_ways(data, k - 2, memo)
    memo[k] = result
    return result


def decode_num_ways(string):
    memo = [None]*len(string)
    return num_ways(string, len(string), memo)


if __name__ == "__main__":
    pass
