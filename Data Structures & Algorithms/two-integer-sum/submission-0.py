class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map
        hmap = {}
        # Now ki korbo ? we see if we have the diff in the map or not
        for i , n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff] , i]   
            else:         
                hmap[n] = i

       