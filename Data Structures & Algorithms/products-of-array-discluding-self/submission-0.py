class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        # Pass one : Compute Prefix Left Products !
        prefix = 1
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        
        # Pass two : Compute Prefix Right Products !
        suffix = 1
        for i in range(length-1,-1 , -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res