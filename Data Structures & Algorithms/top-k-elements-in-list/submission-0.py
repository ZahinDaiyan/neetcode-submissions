class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # what dose it return a dict ?

        # Made a array
        b = []

        # Making a 2D Array so we can store how many times a element appear
        # Here the index is the how many times it appred
        # 2 elemnets can appear same amount of times so we use a list of list
        for i in range(len(nums) + 1):
            b.append([])

        # Now to actually fill up the list :
        for key , value in count.items(): # Still confuses me 
            b[value].append(key)
            
        res = []
        for i in range(len(b) - 1, 0 , -1): #still confused 
            for num in b[i]:
                res.append(num)
                if len(res) == k:
                    return res

# i did not understand the question




        
