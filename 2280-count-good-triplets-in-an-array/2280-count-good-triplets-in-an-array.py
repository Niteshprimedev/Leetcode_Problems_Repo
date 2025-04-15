class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # solution ref: https://leetcode.com/problems/count-good-triplets-in-an-array/solutions/6653459/beats-100-algorithm-pattern-reverse-iteration-with-binary-search-python3
        count = 0

        indices = [0] * len(nums1)

        for i, num in enumerate(nums1):
            indices[num] = i

        for i, num in enumerate(nums2):
            nums1[i] = indices[num]

        arr = SortedList()

        for i, num in enumerate(nums1[::-1]):
            idx = arr.bisect(num)

            count += (i - idx) * (num - idx)
            arr.add(num)
        
        return count