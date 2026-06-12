class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        sett = set()
        l = 0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            sett.add(s[r])
            ans = max(ans,r-l+1)
                
        return ans

       