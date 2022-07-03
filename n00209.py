from datetime import datetime
import numpy as np


class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        a_num = np.array(nums)
        l = a_num.size
        #y = a_num.sum() - x
        h_s = dict()
        answer = 0
        left = 0
        right = -1
        s = 0
        s1 = 0
        running = True
        def check_answer():
            nonlocal left, right, a_num, s, s1, answer, h_s, running
            if s - s1 >= target and (answer == 0 or right - left + 1 < answer):
                answer = right - left + 1

        def move_right():
            nonlocal left, right, a_num, s, s1, answer, h_s, running
            while right + 1 < l:
                next_sum = s + a_num[right + 1]
                right += 1
                s = next_sum
                #h_s[s] = right
                check_answer()
                if s - s1 > target:
                    return
            running = False


        def move_left():
            nonlocal left, right, a_num, s, s1, answer, h_s, running

            while left < right:
                next_sum1 = s1 + a_num[left]
                left += 1
                s1 = next_sum1
                check_answer()
                if s - s1 < target:
                    break



        while running:
            check_answer()
            move_right()
            move_left()

        return answer

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(sol.minSubArrayLen(11, [1,2,3,4,5]))

    #print(sol.minSubArrayLen(134365, [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]))
    #print(sol.minSubArrayLen([1,1,4,2,3], 5))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))