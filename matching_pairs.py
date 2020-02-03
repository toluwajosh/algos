"""Matchin Pairs
Find 2 numbers in a list (no duplicates) that sum up to a give value
assume input list is a valid list of whole positive numbers
"""


def matching_pair(num_list, pair_sum):
    nums_dict = {num: num for num in num_list}
    for num in num_list:
        compliment = pair_sum - num
        print("compliment: ", compliment)
        if compliment in nums_dict:
            return num, compliment
    return "no valid pair"


if __name__ == "__main__":
    num_list = [14, 13, 6, 7, 8, 10, 1, 2]
    print(matching_pair(num_list, 10))

