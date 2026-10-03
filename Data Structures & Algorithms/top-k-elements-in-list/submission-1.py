class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        for i in range(k):
            max = 0
            ke = 0
            for key in d:
                if d[key] > max:
                    ke = key
                    max = d[key]
            l.append(ke)
            del d[ke]
        return l
            
            
        
