from datetime import datetime
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        l = len(nums)
        if l == 1: return 0
        if l == 2: return 2 * int(nums[0] > nums[1])
        left, right = None, None
        left_done, right_done = False, False
        for i in range(1, l):
            if nums[i] < nums[i-1] and not left_done:
                left_done = True
                left = i-1
            if nums[l-i] < nums[l-i-1] and not right_done:
                    right_done = True
                    right = l - i
        if left is None or right is None:
            return 0
        else:
            new_left = left
            new_right = right
            min = None
            max = None
            for i in range(left, right + 1):
                if min is None: min = nums[i]
                if max is None: max = nums[i]
                if nums[i] > max: max = nums[i]
                if nums[i] < min: min = nums[i]
            for i in range(left + 1):
                if min < nums[left - i]:
                    new_left = left - i
            for i in range(l - right):
                if max > nums[right + i]:
                    new_right = right + i

        return new_right - new_left + 1

if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.findUnsortedSubarray([2,7,8,9,4,1,5,0,6,3]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))