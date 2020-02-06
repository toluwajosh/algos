"""palindrome_break
Break the palindrome
"""


class Pal:
    seen = {}

    def is_pal(self, s):
        if s in self.seen:
            return self.seen[s]
        reversed_s = ""
        for sub in s:
            reversed_s = sub + reversed_s
        return reversed_s == s


# longes palindromic substring
def is_palindrome(s):
    reversed_s = ""
    for sub in s:
        reversed_s = sub + reversed_s
    return reversed_s == s


def longestPalindrome_1(self, s: str) -> str:
    seen = {}
    tail = 0
    best_top = 0
    best_tail = 0
    longest = 0
    for top, char in enumerate(s):
        if char in seen:
            tail = seen[char]
            pal_length = top - tail
            if pal_length > longest and is_palindrome(s[tail : top + 1]):
                best_top = top
                best_tail = tail
        seen[char] = top
    return s[best_tail : best_top + 1]


def longestPalindrome_2(s):
    best_top = 0
    best_tail = 0
    longest = 0
    pal = Pal()
    for i, char in enumerate(s):
        top = i
        tail = i + 1
        while tail >= 0 and top <= len(s) and pal.is_pal(s[tail:top]):
            # print(top, tail, s[tail:top],  pal.is_pal(s[tail:top]))
            if (top - tail) > longest:
                best_top = top
                best_tail = tail
                longest = top - tail
            top += 1
            tail -= 1
        top = i
        tail = i + 2
        while tail >= 0 and top <= len(s) and pal.is_pal(s[tail:top]):
            print(top, tail, s[tail:top], pal.is_pal(s[tail:top]))
            if (top - tail) > longest:
                best_top = top
                best_tail = tail
                longest = top - tail
            top += 1
            tail -= 1
    return s[best_tail:best_top]


if __name__ == "__main__":
    # pal = Pal()
    # print(pal.seen)
    print(longestPalindrome_2("ccd"))
