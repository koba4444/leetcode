from datetime import datetime
import numpy as np


class Solution:
    def longestStrChain(self, words) -> int:
        def count_predecessors(n, ind):
            nonlocal curr_sum
            def part(pre, post):
                count_errors = 0
                for i in range(len(pre)):
                    if pre[i] != post[i]:
                        count_errors = i
                        break
                for i in range(count_errors, len(pre)):
                    if pre[i] != post[i+1]:
                        return False
                return True


            if hash[n][ind][1] and n-1 in hash.keys():
                for pre in hash[n-1]:
                    if pre[1] and part(pre[0],hash[n][ind][0]):
                        pre[1] = False
                        curr_sum += 1
                        if curr_sum > answer
                            answer = curr_sum
                        


            else:
                return



        hash = dict()
        #h = np.empty((1000, 1000, 16), dtype=np.str_)
        #print(h)
        answer = 0
        max_len = 0

        for i in words:
            if len(i) not in hash.keys():
                hash[len(i)] = [[i,True]]
                max_len = max(max_len, len(i))
            else:
                hash[len(i)].append([i,True])
        curr = max_len
        for k in range(max_len):
            if max_len - k in hash.keys():
                for ind, val in enumerate(hash[max_len - k]):
                    curr_sum = 0
                    count_predecessors(max_len - k, ind)


        return answer


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.minDistance("alewetb", "lewet",))
    print(sol.longestStrChain(["a","b","ba","bca","bda","bdca"]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))