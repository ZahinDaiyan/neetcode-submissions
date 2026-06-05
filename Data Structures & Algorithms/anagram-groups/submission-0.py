class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for i in strs:
            count = [0] * 26

            for j in i:
                ind = ord(j) - ord('a')
                count[ind] += 1

                
            ans[tuple(count)].append(i)
        
        return list(ans.values())