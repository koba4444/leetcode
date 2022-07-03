def work_substring(s, n):
    ss = s[:n]
    l = n
    for char in s[n:]:
        if char not in ss:
            ss += char
            l += 1
        else:
            return l
    return l

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_max = 0
        s_len = len(s)
        ss_len = None
        for char_ind in range(s_len):
            if char_ind + l_max >= s_len: return l_max
            ss_len = work_substring(s[char_ind:], (ss_len - 1) if ss_len else 0)
            if ss_len > l_max:
                l_max = ss_len
        return l_max

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abacdae"))