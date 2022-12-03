from datetime import datetime



class Solution:
    def topKFrequent(self, nums, k):
        hash = {}
        ans = ''

        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        lst = [[key, freq] for key, freq in hash.items()]
        lst.sort(key=lambda x: (-x[1]))

        return [x[0] for x in lst[:k]]


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.topKFrequent([1,2,1,2,3,4,3,2,3],2))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))