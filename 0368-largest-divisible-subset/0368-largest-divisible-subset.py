class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array to ensure divisibility chains can be checked in order
        nums.sort()
        
        # Step 2: Create a cache to memoize results
        cache_obj = {}

        # Step 3: Define the recursive DFS function
        def dfs(curr_idx, prev_el):
            # Base Case: Reached the end of array
            if curr_idx == len(nums):
                return []

            # Memoization Check            
            if (curr_idx, prev_el) in cache_obj:
                return cache_obj[(curr_idx, prev_el)]
            
            # Option 1: Skip current number
            result = dfs(curr_idx + 1, prev_el) # skip current element 

            # Option 2: Take current number if divisible by prev_el
            if nums[curr_idx] % prev_el == 0:
                temp = [nums[curr_idx]] + dfs(curr_idx + 1, nums[curr_idx])
                # Choose the larger subset
                result = temp if len(temp) > len(result) else result

            # Save in cache and return
            cache_obj[(curr_idx, prev_el)] = result
            return result
        
        # Step 4: Start DFS from index 0 with prev_el as 1 (1 divides all numbers)
        return dfs(0, 1)
        