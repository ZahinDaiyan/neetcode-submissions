class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        n = len(heights)
        l ,r = 0 , n-1
        while(l < r):
            h = min(heights[l] , heights[r])
            area = (r-l) * h
            maxx = max (maxx,area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxx

        