class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))  # Number of unique elements in the entire array
        n = len(nums)
        count = 0
        left = 0
        freq = Counter()  # Frequency map of elements in the current window

        for right in range(n):
            freq[nums[right]] += 1

            # Shrink the window from the left while it still contains all unique elements
            while len(freq) == total_unique:
                # All subarrays starting from `left` to `right` till end are valid
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count