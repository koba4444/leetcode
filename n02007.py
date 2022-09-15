from datetime import datetime
import collections


class Solution:
    def findOriginalArray(self, changed):
        l = len(changed)
        if l % 2 > 0: return []
        ans = []
        hashmap = {}
        for i in changed:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_keys = sorted(hashmap.keys())
        for ind in range(len(sorted_keys)):
            if hashmap[sorted_keys[ind]] > 0:
                val2 = sorted_keys[ind] * 2
                if ((val2 in hashmap.keys()) and hashmap[val2] > 0):
                    if val2 == 0:
                        while hashmap[val2] > 0:
                            if hashmap[val2] % 2 == 0:
                                ans.append(sorted_keys[ind])
                                hashmap[val2] -= 2
                            else:
                                return []
                    else:
                        while hashmap[sorted_keys[ind]] > 0 and hashmap[val2] > 0:
                            ans.append(sorted_keys[ind])
                            hashmap[sorted_keys[ind]] -= 1
                            hashmap[val2] -= 1
                        if hashmap[sorted_keys[ind]] > 0: return []
                else:
                    return []

            else:
                continue

        return ans



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.findOriginalArray([5,7,2,10,4,2,7,14]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))