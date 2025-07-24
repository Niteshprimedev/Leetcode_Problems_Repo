class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Solution using Kadane's Algo:
        # Slightly Tricky way: Use the Kadanes Algo to find the 
        # maxi1 by traversing from left to right and 
        # find the maxi2 by traversing from right to left;
        # the maximum of maxi1 and maxi2 will be the maxiSubArrProduct

        # Logic: The whole concept lies: As we can see there is only 1 negative no.
        # and if we consider that number, then the final answer can never be positive
        # therefore to avoid this situtation we also traverse from right to left to 
        # get the maximum subarray product;

        max_subarr_product = float('-inf')
        curr_subarr_product = 1

        # Left To Right Traverse to find the max:
        for idx_i in range(len(nums)):
            num = nums[idx_i]

            curr_subarr_product *= num
            max_subarr_product = max(max_subarr_product, curr_subarr_product)

            if curr_subarr_product == 0:
                curr_subarr_product = 1

        # Right To Left Traverse to find the max:
        curr_subarr_product = 1
        for idx_i in range(len(nums) - 1, -1, -1):
            num = nums[idx_i]

            curr_subarr_product *= num
            max_subarr_product = max(max_subarr_product, curr_subarr_product)

            if curr_subarr_product == 0:
                curr_subarr_product = 1
        
        return max_subarr_product