from datetime import datetime
import collections


class Solution:
    def recoverArray(self, nums):

        def check(hashmap, sorted_keys, k):
            ans = []
            for s in sorted_keys:
                if hashmap[s] == 0: continue
                if (s + 2 * k) in hashmap:
                    if hashmap[s] > hashmap[s + 2 * k]:
                        return []
                    else:
                        ans.extend([s + k] * hashmap[s])
                        hashmap[s + 2 * k] -= hashmap[s]
                        hashmap[s] = 0
                        continue
                else:
                    return []
            return ans
        answer = []
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_keys = sorted(hashmap.keys())
        k_max = (sorted_keys[-1] - sorted_keys[0]) // 2 + 1
        poss_k = []
        for k in sorted_keys:
            if ((k - sorted_keys[0]) % 2 == 0) and(0 < k - sorted_keys[0] <= k_max * 2):
                poss_k.append((k - sorted_keys[0]) // 2)
        for k in poss_k:
            hm = hashmap.copy()
            answer = check(hm, sorted_keys, k)
            if len(answer) > 0: return answer
        return answer



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.recoverArray([1,50,99,101,150,199]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))