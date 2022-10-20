from datetime import datetime
import collections



class Solution:
    def numberOfPairs(self, nums):
        hash = {}
        pairs = 0
        leftover = 0
        for n in nums:
            if n in hash:
                if hash[n] == 0:
                    hash[n] += 1
                    leftover += 1
                else:
                    hash[n] = 0
                    pairs += 1
                    leftover -= 1
            else:
                hash[n] = 1
                leftover += 1
        return [pairs, leftover]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.numberOfPairs([1,3,2,1,3,2,2]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))