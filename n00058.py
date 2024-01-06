 from datetime import datetime
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = len(s)
        ans = 0
        i = 0
        while i < l:
            if s[-1-i] == " ":
                return ans
            else:
                ans += 1
            i += 1
        return ans



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.lengthOfLastWord("hello ll " ))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))