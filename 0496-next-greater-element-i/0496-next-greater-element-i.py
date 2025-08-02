class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force Solution: To find the matching values first and then
        # find the next greater element for that element;

        nums1_len = len(nums1)
        next_greater_els = [-1] * nums1_len

        idx_i = 0
        for num in nums1:
            for idx_j in range(len(nums2)):
                second_num = nums2[idx_j]

                if num == second_num:
                    idx_j += 1
                    while (idx_j < len(nums2) and second_num > nums2[idx_j]):
                        idx_j += 1
                    
                    if idx_j < len(nums2):
                        next_greater_els[idx_i] = nums2[idx_j]
                    else:
                        next_greater_els[idx_i] = -1
                    
                    idx_i += 1
                    break
            
        return next_greater_els

        '''
        # if nums1 is a subset of nums2 then definitely
        # all the elements of nums1 are present in nums2:

        # Logic: Find the next greater element for each element of 
        # nums1 and keep it thier answer in their indices in the results
        # to check if the answer needs to be updated for nums1:
        # we can check if it is present in nums1 and at what index?
        nums1_len = len(nums1)

        nums1_els_map = {}
        next_greater_stack = []
        next_greater_els = [-1] * nums1_len

        for idx_i in range(nums1_len):
            num = nums1[idx_i]
            nums1_els_map[num] = idx_i
        
        for idx_j in range(len(nums2) - 1, -1, -1):
            while next_greater_stack and next_greater_stack[-1] <= nums2[idx_j]:
                next_greater_stack.pop()
            
            if next_greater_stack and nums2[idx_j] in nums1_els_map:
                idx_value = nums1_els_map.get(nums2[idx_j])

                next_greater_els[idx_value] = next_greater_stack[-1]
            
            next_greater_stack.append(nums2[idx_j])
        
        return next_greater_els
        '''
        
        