"""
Output all the permutations and compute the code time complexity if your code is good enough,
the time complexity should be n!
but when i was interviewing with the two interviewers, i wrote a n^n solution.
Actually, there are recursive and iterative solutions in n! time complexity.
The best solution should call next permutation function n! times.

Hint:
Permutations, nPr = n!/(n-r)!

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class NumsPerm:
    perms_dict = {}

    def array_perm(self, nums):
        if str(nums) in self.perms_dict:
            return self.perms_dict[str(nums)]
        if len(nums) == 2:
            return [nums[1], nums[0]]
        permutations = []
        for i, ele in enumerate(nums):
            loc_nums = nums[:]
            loc_nums.pop(i)
            if len(loc_nums) > 2:
                permutations = permutations + [
                    [ele] + outs for outs in self.array_perm(loc_nums)
                ]
            else:
                permutations.append([ele] + self.array_perm(loc_nums))
        self.perms_dict[str(nums)] = permutations
        return permutations


def unique_permutations(nums):
    num_perm = NumsPerm()
    return num_perm.array_perm(nums)


if __name__ == "__main__":
    print(unique_permutations([0, 1, 2, 3, 5]))
