class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # code here
        # Binary Search Solution:
        # Intuition:
        # While traversing we try to create multiple 
        # LIS forms and then later on figure out the max one
        # But instead of tracking the multiple instances
        # of LIS, we can overwrite the existing LIS whenever 
        # we find any element which is smaller than the last element
        # in our current LIS
        # This way, we ensure the length of longest increasing subsequence
        # Note: we overwrite the currEl with our existing element in LIS
        # at the position where the element is found or at the next greater
        # element position; 
        
        def binary_search_idx(sorted_arr, target):
            left_idx = 0
            right_idx = len(sorted_arr) - 1
            
            while(left_idx < right_idx):
                middle_idx = left_idx + (right_idx - left_idx) // 2
                
                if sorted_arr[middle_idx] >= target:
                    right_idx = middle_idx
                else:
                    left_idx = middle_idx + 1
                    
            return left_idx
        
        longest_els_len = []
        longest_inc_subseq_len = 1
        
        longest_els_len.append(nums[0])
        
        for curr_idx in range(1, len(nums)):
            last_idx = len(longest_els_len) - 1
            
            if nums[curr_idx] > longest_els_len[last_idx]:
                longest_els_len.append(nums[curr_idx])
                longest_inc_subseq_len += 1
            else:
                # Binary Search: 
                # If the element exists then it's index
                # else the index of the next greater element;
                found_idx = binary_search_idx(longest_els_len, nums[curr_idx])
                longest_els_len[found_idx] = nums[curr_idx]
        
        return longest_inc_subseq_len