from datetime import datetime

class Solution:
    def maxOperations(self, nums, k: int) -> int:
        answer = 0
        answer1 = 0
        hash = {}
        for i in nums:
            if i in hash.keys():
                hash[i] += 1
            else:
                hash[i] = 1
        for i in hash.keys():
            if i == k // 2 and k % 2 == 0:
                answer1 += hash[i] // 2
            else:
                if k - i in hash.keys():
                    answer += min(hash[i], hash[k - i])
        return answer // 2 + answer1



if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.maxOperations([1,2,3,4, 3, 3, -9, 15, 1],6))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))