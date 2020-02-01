"""longest_substring
"""

def rep_present(string):
    seg_dict = {}
    for s in string:
        if s in seg_dict:
            return True
        seg_dict[s] = s
    return False

def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    tail = 0
    cur_len = 0
    seen = {s[0]:0}
    longest = 1
    for head in range(1, len(s)):
        if s[head] in seen:
            tail = max(seen[s[head]] + 1, tail)
        seen[s[head]] = head
        cur_len = head - tail + 1
        if cur_len > longest:
            longest = cur_len
    return longest

if __name__ == "__main__":
    print(lengthOfLongestSubstring("baaaccb"))