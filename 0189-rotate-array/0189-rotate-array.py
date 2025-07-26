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

        # Note: If rotating by left then the next element would
        # be available at (curr_idx + d or k) % n
        # If rotating by right then next element will be
        # available at (curr_idx + n - d or n - k) % n
        # Length of cycle will be equal to the smallest m
        # that satisfies the multiple of n let's suppose if we
        # had k = 3 and n = 7 then the smallest m would be 7
        # cause k * m % n should be 0 => 7 * 3 => 21 which is divisible
        # Number of cycles will be derived by the length of the cycle
        # let's generalize it:
        # so we have k * m % n to figure out the length of the cycle
        # so if I want to make both sides equal then I would need 
        # some integer x to balance both the sides, right
        # (k * m) = (x * n): here m is the smallest m that satisfies
        # (k * m) % n == 0 && x is the values that makes both sides equal
        # so x can be calculated as (k * m) // n
        # Now, we have this equation (k * m) == (x * n)
        # then we can say smallest m = (x * n) // k
        # (x * n) is the least common multiple of n and k
        # i.e length of one cycle = LCM(n, k) / k
        # Total cycles => total number of elements divided by length of one cycle
        # Total Cycles => n // LCM(n, k) / k
        # or total_cycles => (n * k) // LCM(n, k)
        # since Multple of (a, b) / LCM(a, b) is nothing but GCD so
        # Total_Cycles => GCD(n, k)
        from math import gcd
        n = len(nums)

        k = k % n # to keep k within bounds;

        # Juggling Algo; Rotate elements in cycles;
        for cycle_idx in range(gcd(n, k)):
            curr_idx = cycle_idx
            cycle_strt_el = nums[curr_idx]

            while True:
                next_idx = (curr_idx + n - k) % n

                if next_idx == cycle_idx:
                    break

                # rotate the next_idx element to its kth pos to the right;
                nums[curr_idx] = nums[next_idx]
                curr_idx = next_idx
            
            # rotate the strt_el to its kth pos to the right;
            nums[curr_idx] = cycle_strt_el
        
        # return nums; but we are doing it in-place so no need;

