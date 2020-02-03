"""Repeating DNA Sequences
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


def repeatingSeqeunces(string):
    seen_dict = {}
    seen_list = []
    for i in range(len(string)-9):
        if string[i:i+10] in seen_dict and string[i:i+10] not in seen_list:
            seen_list.append(string[i:i+10])
        seen_dict[string[i:i+10]] = string[i:i+10]
    return seen_list


if __name__ == "__main__":
    print(repeatingSeqeunces("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
