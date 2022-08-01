from datetime import datetime
import collections


class Solution:
    global h
    h = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    def letterCombinations(self, digits: str):
        if digits == '': return []
        if len(digits) == 1:
            return [s for s in h[digits]]

        ans = []
        first = digits[0]
        tail = self.letterCombinations(digits[1:])

        for d in h[first]:
            for t in tail:
                ans.append(d+t)
        return ans



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.letterCombinations("772"))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))