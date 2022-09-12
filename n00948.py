from datetime import datetime
import collections


class Solution:
    def bagOfTokensScore(self, tokens, power) -> int:
        tokens.sort()
        score = 0
        ans = 0
        left = 0
        right = len(tokens)-1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                ans = max(ans, score)
                left += 1
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    #print(sol.bagOfTokensScore([100,200,300,400],200))
    print(sol.bagOfTokensScore([71, 55, 82], 54))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))