class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        left = 0
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            k -= map[nums[i]]
            map[nums[i]] += 1

            while k <= 0:
                map[nums[left]] -= 1
                k += map[nums[left]]
                left += 1
            count += left
        
        return count