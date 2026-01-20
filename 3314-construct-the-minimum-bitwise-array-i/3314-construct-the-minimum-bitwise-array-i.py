class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def findMin(target):
            minVal = -1
            for i in range(1, target):
                if i | (i + 1) == target:
                    minVal = i
                    break
            
            return minVal
        
        for i in range(len(nums)):
            nums[i] = findMin(nums[i])

        return nums
        