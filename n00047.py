from datetime import datetime

class Solution:
    def permuteUnique(self, nums):
        def dfs(nums, curr):
            if not nums:
                res.append(curr)
            for x in nums:
                rem = list(nums)
                rem.remove(x)
                dfs(rem, curr + [x])
        res = []
        dfs(nums, [])
        s = set()
        for i in res:
            s.add(tuple(i))
        answer = []
        for i in s:
            answer.append(list(i))
        return answer






if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.permuteUnique([1,1,2]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))