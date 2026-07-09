class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # IMP: left partion should be smaller than right partition;
        # Logic: Solution using symmetry partition; Revised on June 13

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums2_len < nums1_len:
            return self.findMedianSortedArrays(nums2, nums1)

        total_els_partition = (nums1_len + nums2_len + 1) // 2

        left = 0
        right = nums1_len
        median_val = 0

        while left <= right:
            # determine the elements from the array1
            mid1 = left + (right - left) // 2

            # determine the remaining elements from the array2
            mid2 = total_els_partition - mid1

            left1_val = float('-inf') # last element of arr1
            left2_val = float('-inf') # last element of arr2
            right1_val = float('inf') # first element of arr1
            right2_val = float('inf') # first element of arr2

            if mid1 > 0 and mid1 <= nums1_len:
                left1_val = nums1[mid1 - 1]

            if mid2 > 0 and mid2 <= nums2_len:
                left2_val = nums2[mid2 - 1]

            if mid1 >= 0 and mid1 < nums1_len:
                right1_val = nums1[mid1]

            if mid2 >= 0 and mid2 < nums2_len:
                right2_val = nums2[mid2]

            # determine if we need to take less elements from array1:
            if left1_val > right2_val:
                right = mid1 - 1
            # determine if we need to take more elements from array1:
            elif left2_val > right1_val:
                left = mid1 + 1
            else:
                # found the valid partition, now calculate median
                # 2 IMP Cases
                # Even Case:
                if (nums1_len + nums2_len) % 2 == 0:
                    average = max(left1_val, left2_val) + min(right1_val, right2_val)
                    median_val = average / 2
                else:
                    median_val = max(left1_val, left2_val)
                
                break
        
        return median_val
