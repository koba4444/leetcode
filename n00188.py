from datetime import datetime
import collections


class Solution():
    def maxProfit(self, k, prices) -> int:
        if k ==0: return 0
        cost = [-1000000000]*k
        #cost = [-1000000000]*k
        profit = [0]*k
        #profit = [0]*k


        for p in prices:
            for i in range(k):
                if i == 0:
                    cost[i] = max(cost[i], -p)
                else:
                    cost[i] = max(cost[i], -p + profit[i - 1])
                profit[i] = max(profit[i], p + cost[i])

        return profit[k-1]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.maxProfit(2,[3,2,6,5,0,3]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))