from datetime import datetime
import collections



class Solution:
    def searchRange(self, nums , target) :
        a,b = 0,0
        left_do = True
        right_do = True
        l = len(nums)+1
        for i in range(1, l):
            if (nums[i-1] == target):
                a = i
                left_do = False
                break
        for i in range(1, l):
            if (nums[-i] == target):
                b = l-i
                right_do = False
                break
        if  not(left_do or right_do):
            return([a-1, b-1])
        else:
            return([-1,-1])


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))