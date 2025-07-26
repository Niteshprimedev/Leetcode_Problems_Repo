class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        # Observation: K times clockwise rotation meaning
        # your resultant array will start from the kth element
        # from end till (k - 1)th element;
        # so if your array is [1, 2, 3, 4, 5] & k = 2 then
        # [4, 5, 1, 2, 3] as the clockwise kth rotation
        
        # K-times Anti-Clockwise Rotation
        # your resultant array will start from the (k + 1)th element
        # from start till (k)th element;
        # so if your array is [1, 2, 3, 4, 5] & k = 2 then
        # [3, 4, 5, 1, 2] as the anti-clockwise kth rotation

        # Logic: Solution using two pointers reverse array technique
        # When reversing to the right by k steps
        # First need to reverse the entire array,
        # then reverse the first k steps & then the last k steps

        # When reversing to the left by k steps
        # First need to reverse the first k steps & then last k steps
        # Finally, need to reverse the entire array;

        n = len(nums)
        k = k % n

        if k == 0:
            return nums
        
        def reverse(strt_idx, end_idx):
            while strt_idx < end_idx:
                nums[strt_idx], nums[end_idx] = nums[end_idx], nums[strt_idx]
                strt_idx += 1
                end_idx -= 1
            
            return
        
        # reverse the entire array;
        reverse(0, n - 1)

        # reverse first k elements;
        reverse(0, k - 1)

        # reverse last k elements
        reverse(k, n - 1)

        return nums
        '''
        
        '''
        # Solution 2: Using Extra Space - 
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
        '''

        # Solution 3: Juggling Algorithm Space Optimized
        # One Pass Solution:

        n = len(nums)
        k %= n

        def nexti(i):
            dist = n - k
            return (i + dist) % n
        
        for s in range(gcd(k, n)):
            first = nums[s]
            i, j = s, nexti(s)
            while j != s:
                nums[i] = nums[j]
                i, j = nexti(i), nexti(j)
            nums[i] = first