class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            # If The first element is a duplicate we skip
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two Sum II => Two Pointer Squezee
            l ,r = i+1 , n-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ == 0:
                    ans.append([nums[i],nums[l],nums[r]])

                    # Move the pointer and skip duplicates for l , r
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return ans
            

        