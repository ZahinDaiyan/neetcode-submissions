class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i],0) + 1

        res = max(counts, key=counts.get)



        return res