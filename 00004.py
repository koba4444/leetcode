class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        cur = []
        n = len(nums1)
        m = len(nums2)
        if max(m, n) == 0: return .0
        not_even = (m + n) % 2
        i1 = 0
        i2 = 0
        while i1 + i2 < (m + n + 1) // 2:
            if i1 == n:
                cur.append(nums2[i2])
                i2 += 1
            elif i2 == m:
                cur.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                cur.append(nums1[i1])
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                cur.append(nums2[i2])
                i2 += 1
            elif nums1[i1] == nums2[i2]:
                cur.append(nums1[i1])
                i1 += 1
        if not_even:
            return float(cur[-1])
        else:
            if i1 == n:
                cur.append(nums2[i2])
                i2 += 1
            elif i2 == m:
                cur.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                cur.append(nums1[i1])
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                cur.append(nums2[i2])
                i2 += 1
            elif nums1[i1] == nums2[i2]:
                cur.append(nums1[i1])
                i1 += 1
            return float((cur[-1] + cur[-2])/2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1], [5, 6]))