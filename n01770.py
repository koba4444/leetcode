from datetime import datetime
import collections


class Solution:


    def maximumScore(self, nums, multipliers):

        global hashmap
        hashmap = {}
        def dp(nums, multipliers, max_score, cutleft, cutright):
            global hashmap
            if len(multipliers) == 1:
                if (cutleft, cutright) not in hashmap:
                    hashmap[(cutleft, cutright)] = max_score + max(multipliers[0] * nums[0], multipliers[0] * nums[-1])
                return hashmap[(cutleft, cutright)]
            else:
                if (cutleft, cutright) not in hashmap:
                    mleft = dp(nums[1:],
                            multipliers[1:],
                            max_score + multipliers[0] * nums[0],
                            cutleft + 1,
                            cutright)
                    mright = dp(nums[:-1],
                            multipliers[1:],
                            max_score + multipliers[0] * nums[-1],
                            cutleft,
                            cutright + 1)
                    hashmap[(cutleft, cutright)] = max(mleft, mright)
                return hashmap[(cutleft, cutright)]
        ans = dp(nums, multipliers, 0, 0, 0)
        a = 0
        return ans



    def maximumScore1(self, nums, multipliers):
        m = len(multipliers)
        n = len(nums)
        s = 0
        dp = [[0] * (m + 1) for i in range(m + 1)]
        for j in range(m - 1, -1, -1):
            for low in range(j, -1, -1):
                first = nums[low] * multipliers[j] + dp[j + 1][low + 1]
                last = nums[n - 1 - (j - low)] * multipliers[j] + dp[j + 1][low]
                dp[j][low] = max(first, last)
        return dp[0][0]

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.maximumScore([555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10], [783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521]))
    #print(sol.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))