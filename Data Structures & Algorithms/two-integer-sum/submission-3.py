class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        seen = {}
        for i , n in enumerate(nums):
            x = target - n
            if x in seen:
                return [seen[x],i]
            seen[n] = i

      