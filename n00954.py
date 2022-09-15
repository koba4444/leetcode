from datetime import datetime
import collections


class Solution:
    def canReorderDoubled(self, changed):

        def check(changed, k, hashmap):
            if hashmap[k] == 0:
                return True
            else:
                if 2 * k not in hashmap or hashmap[k] > hashmap[2 * k]:
                    return False
                else:
                    hashmap[2 * k] -= hashmap[k]
                    hashmap[k] = 0
                    return True

        def check_zero(changed, sorted_keys_zero, hashmap):
            if not sorted_keys_zero: return True
            if hashmap[0] % 2 == 0:
                return True
            else:
                return False


        l = len(changed)
        if l % 2 > 0: return False
        ans = []
        hashmap = {}
        for i in changed:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_keys = sorted(hashmap.keys())
        sorted_keys_neg = [i for i in sorted_keys if i<0][::-1]
        sorted_keys_zero = True if (0 in sorted_keys) else False
        sorted_keys_pos = [i for i in sorted_keys if i>0]
        for k in sorted_keys_pos:
            if not check(changed, k, hashmap): return False
        for k in sorted_keys_neg:
            if not check(changed, k, hashmap): return False
        if not check_zero(changed, sorted_keys_zero, hashmap): return False
        return True

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.canReorderDoubled([4,-2,2,-4,1,1]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))