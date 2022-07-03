from datetime import datetime
import collections
import numpy as np

class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        a_num = np.array(nums)
        l = a_num.size
        h_s = dict()
        ss = np.array([0]*10**5)
        answer = 0
        left = -1
        right = -1
        running = True

        def check_answer():
            nonlocal left, right, a_num, ss, answer, h_s, running
            if answer == 0 or ss[right] - (ss[left] if left >=0 else 0) > answer:
                answer = ss[right] - (ss[left] if left >=0 else 0)

        def move_right():
            nonlocal left, right, a_num, ss, answer, h_s, running
            while right + 1 < l:
                ss[right + 1] = ss[right] + a_num[right + 1]
                if a_num[right + 1] in h_s.keys() and left < h_s[a_num[right + 1]] and h_s[a_num[right + 1]] != -1:
                    left = h_s[a_num[right + 1]]
                    h_s[a_num[right + 1]] = right + 1

                else:
                    h_s[a_num[right + 1]] = right + 1

                right += 1
                check_answer()
            running = False


        while running:

            move_right()
        return answer


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    #print(sol.maximumUniqueSubarray([4,2,4,5,6]))
    print(sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
    #print(sol.maximumUniqueSubarray([1,2,3,2,5]))
    print(sol.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))