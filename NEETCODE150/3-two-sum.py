class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,j in enumerate(nums):
            if target - j in hashmap:
                return [ hashmap[target-j] ,i ]
            
            hashmap[j] = i 
        return
