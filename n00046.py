from datetime import datetime

class Solution:
    def permute(self, nums):
        def permute_detailed(l, s):
            answer = []
            if l == 1:
                return s
            else:
                for y in permute_detailed(1, s):
                    ss = s.copy()
                    ss.remove(y)
                    for x in permute_detailed(l - 1, ss):
                        ans = [y]
                        if isinstance(x, list):
                            ans.extend(x)
                        else:
                            ans.extend([x])
                        answer.append(ans)
                return answer
        answer = permute_detailed(len(nums), nums)
        if not isinstance(answer[0], list):
            answer = [answer]
        return answer




if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.permute([1]))
    print(len(sol.permute([1,2,3])))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))