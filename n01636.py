from datetime import datetime
import collections



class Solution:
    def frequencySort(self, nums):
        hash = {}
        ans = []
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        lst = [[key,freq] for key, freq in hash.items()]
        lst.sort(key=lambda x: (x[1],-x[0]))
        for l in lst:
            ans.extend([l[0]] * l[1])
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.frequencySort([1,3,2,1,3,2,2]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))