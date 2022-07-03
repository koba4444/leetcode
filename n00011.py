from datetime import datetime

class Solution:
    def maxArea(self, height) -> int:
        l = len(height)
        left = 0
        right = l - 1
        vmax = min(height[0], height[-1]) * (l - 1)

        def squize(height, left, right, vmax):
            edgeMoved = False
            if height[left] <= height[right - 1]:
                for l in range(left + 1, right - 1):
                    if height[l] > height[left]:
                        if min(height[l], height[right - 1]) * (right - l - 1) > vmax:
                            vmax = min(height[l], height[right - 1]) * (right - l - 1)
                            vmax_improved = True

                        left = l
                        vmax = squize(height, left, right, vmax)
                        #print("l", vmax, left, right)
                        break
            else:
                for r in range(right - 2, left, -1):
                    if height[r] > height[right - 1]:
                        if min(height[left], height[r]) * (r - left) > vmax:
                            vmax = min(height[left], height[r]) * (r - left)
                            vmax_improved = True
                            #print("r", vmax, left, right)
                        right = r + 1
                        vmax = squize(height, left, right, vmax)
                        break
            #if vmax_improved == True: vmax = squize(height, left, right, vmax)
            #print("return", vmax)
            return vmax

        vmax = squize(height, 0, l, vmax)
        return vmax

if __name__ == "__main__":
    sol = Solution()

    start_time = datetime.now()
    print(sol.maxArea([1,2,3,4,5,25,24,3,4]))

    print(sol.maxArea([1, 3, 1, 4, 1, 5, 10]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))